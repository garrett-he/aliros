import json
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest

import click


@click.command('list-stacks')
@click.option('--stack-id', help='ID of stack', required=True)
@click.option('--name', help='Name of stack', required=True)
@click.option('--status', help='Status of stack', required=True)
@click.option('--page-number', help='Number of page', type=int, default=1, required=False)
@click.option('--page-size', help='Size of pages', type=int, default=10, required=False)
def list_stacks_command(ctx: click.Context, stack_id: str, name: str, status: str, page_number: int, page_size: int):
    """List stacks."""

    asc_client = ctx.obj['asc_client']

    request = DescribeStacksRequest()
    stack_id and request.set_StackId(stack_id)
    name and request.set_Name(name)
    status and request.set_Status(status)
    request.set_PageNumber(page_number)
    request.set_PageSize(page_size)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
