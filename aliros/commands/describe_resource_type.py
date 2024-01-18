import json
from aliyunsdkros.request.v20150901.DescribeResourceTypeDetailRequest import DescribeResourceTypeDetailRequest

import click


@click.command('describe-resource-type')
@click.option('--type-name', help='Name of stack', required=True)
def describe_resource_type_command(ctx: click.Context, type_name: str):
    """Describe details of the specified resource type."""

    asc_client = ctx.obj['asc_client']

    request = DescribeResourceTypeDetailRequest()

    request.set_TypeName(type_name)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
