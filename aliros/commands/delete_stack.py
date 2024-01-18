from aliros.stack import find_stack_id, send_request
from aliyunsdkros.request.v20150901.DeleteStackRequest import DeleteStackRequest

import click


@click.command('delete-stack')
@click.option('--stack-name', help='Name of stack', required=True)
def delete_stack_command(ctx: click.Context, stack_name: str):
    """Delete the specified stack."""

    asc_client = ctx.obj['asc_client']
    request = DeleteStackRequest()

    request.set_StackName(stack_name)
    request.set_StackId(find_stack_id(asc_client, stack_name))

    send_request(asc_client, request)
