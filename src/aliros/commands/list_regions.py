from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest

import click

from aliros.stack import send_request

@click.command('list-regions')
def list_regions_command(ctx: click.Context):
    """List available regions."""

    acs_client = ctx.obj['acs_client']
    request = DescribeRegionsRequest()

    send_request(acs_client, request)
