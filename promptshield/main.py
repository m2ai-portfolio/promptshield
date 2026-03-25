"""CLI entry point for PromptShield."""

import sys
import click
from promptshield.validator import validate_prompt, validate_response


@click.group()
def cli():
    """PromptShield - CLI tool to detect LLM prompt injection attacks."""
    pass


@cli.command()
@click.option('--type', 'validation_type', required=True,
              type=click.Choice(['prompt', 'response']),
              help='Type of validation to perform')
@click.argument('text')
def validate(validation_type: str, text: str):
    """
    Validate text for prompt injection or response compromise.

    TEXT can be a string or '-' to read from stdin.
    """
    # Handle stdin input
    if text == '-':
        text = sys.stdin.read().strip()

    # Perform validation based on type
    if validation_type == 'prompt':
        result = validate_prompt(text)
    else:  # response
        result = validate_response(text)

    # Output result
    if result.is_safe:
        click.echo("SAFE")
    else:
        click.echo(f"UNSAFE: {result.reason}")


if __name__ == '__main__':
    cli()
