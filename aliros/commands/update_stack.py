import json
from aliros.template import Template_YAML
from aliros.stack import find_stack_id, send_request
from aliyunsdkros.request.v20150901.UpdateStackRequest import UpdateStackRequest

import click


@click.command('update-stack')
@click.option('--stack-name', help='Name of stack', required=True)
@click.option('--template-file', help='Path of template file', required=True, type=click.Path(exists=True, dir_okay=False))
@click.option('--timeout-mins', help='Minutes to timeout', type=int, default=60)
def update_stack_command(ctx: click.Context, stack_name: str, template_file: str, timeout_mins: int):
    """Update the specified stack."""

    asc_client = ctx.obj['asc_client']

    template = Template_YAML()
    template.load(template_file)

    body = {
        'Template': json.dumps(template.content),
        'TimeoutMins': timeout_mins,
    }

    request = UpdateStackRequest()

    request.set_StackName(stack_name)
    request.set_StackId(find_stack_id(asc_client, request))

    request.set_content(json.dumps(body))
    request.set_content_type('application/json')

    send_request(asc_client, request)
