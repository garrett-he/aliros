import click
from aliros import __version__
from aliros.commands import command_group


def print_version(ctx: click.Context, _, value: str):
    if not value or ctx.resilient_parsing:
        return

    click.echo(__version__)
    ctx.exit()


@click.group(commands=command_group)
@click.option('--version', help='Show version information.', is_flag=True, callback=print_version, expose_value=False,
              is_eager=True)
@click.pass_context
def cli(ctx: click.Context):
    """A command-line tool to organize resources by Resource Orchestration Service for Alibaba Cloud."""

    ctx.ensure_object(dict)


if __name__ == '__main__':
    cli()
