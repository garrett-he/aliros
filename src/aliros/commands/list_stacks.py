import click
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest

from aliros.stack import send_request


@click.command('list-stacks')
@click.option('--stack-id', help='ID of stack.', required=True)
@click.option('--name', help='Name of stack.', required=True)
@click.option('--status', help='Status of stack.', required=True)
@click.option('--page-number', help='Number of page.', type=int, default=1, required=False)
@click.option('--page-size', help='Size of pages.', type=int, default=10, required=False)
def list_stacks_command(ctx: click.Context, stack_id: str, name: str, status: str, page_number: int, page_size: int):
    """List stacks."""

    acs_client = ctx.obj['acs_client']

    request = DescribeStacksRequest()

    if stack_id is not None:
        request.set_StackId(stack_id)

    if name is not None:
        request.set_Name(name)

    if status is not None:
        request.set_Status(status)

    request.set_PageNumber(page_number)
    request.set_PageSize(page_size)

    send_request(acs_client, request)
