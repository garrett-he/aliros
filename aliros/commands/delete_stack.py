import click
from aliyunsdkros.request.v20150901.DeleteStackRequest import DeleteStackRequest

from aliros.stack import find_stack_id, send_request


@click.command('delete-stack')
@click.option('--stack-name', help='Name of stack.', required=True)
def delete_stack_command(ctx: click.Context, stack_name: str):
    """Delete the specified stack."""

    acs_client = ctx.obj['acs_client']
    request = DeleteStackRequest()

    request.set_StackName(stack_name)
    request.set_StackId(find_stack_id(acs_client, stack_name))

    send_request(acs_client, request)
