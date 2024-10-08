import click
from aliyunsdkros.request.v20150901.DescribeStackDetailRequest import DescribeStackDetailRequest

from aliros.stack import find_stack_id, send_request


@click.command('describe-stack')
@click.option('--stack-name', help='Name of stack.', required=True)
def describe_stack_command(ctx: click.Context, stack_name: str):
    """Describe the specified stack."""

    acs_client = ctx.obj['acs_client']

    stack_id = find_stack_id(acs_client, stack_name)

    request = DescribeStackDetailRequest()

    request.set_StackName(stack_name)
    request.set_StackId(stack_id)

    send_request(acs_client, request)
