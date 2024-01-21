import json
from aliyunsdkros.request.v20150901.DescribeResourceTypesRequest import DescribeResourceTypesRequest

import click


@click.command('list-resource-types')
@click.option('--support-status', help='Status of support.', required=False)
def list_resource_types_command(ctx: click.Context, support_status: str):
    """List available resource types."""

    asc_client = ctx.obj['asc_client']

    request = DescribeResourceTypesRequest()
    support_status and request.set_SupportStatus(support_status)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
