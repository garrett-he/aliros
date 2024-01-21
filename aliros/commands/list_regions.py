import json
from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest

import click


@click.command('list-regions')
def list_regions_command(ctx: click.Context):
    """List available regions."""

    asc_client = ctx.obj['asc_client']
    request = DescribeRegionsRequest()

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
