import json
from aliros.template import Template_YAML
from aliros.stack import send_request
from aliyunsdkros.request.v20150901.CreateStacksRequest import CreateStacksRequest

import click


@click.command('create-stack')
@click.option('--stack-name', help='Name of stack.', required=True)
@click.option('--template-file', help='Path of template file.', required=True, type=click.Path(exists=True, dir_okay=False))
@click.option('--parameters-file', help='URL of parameters file.', required=False, type=click.Path(exists=True, dir_okay=False))
@click.option('--timeout-mins', help='Minutes to timeout.', type=int, default=60)
@click.option('--disable-rollback', help='Disable rollback if failed.', required=False, is_flag=True, default=False)
def create_stack_command(ctx: click.Context, stack_name: str, template_file: str, parameters_file: str, timeout_mins: int, disable_rollback: bool):
    """Create a new stack."""

    asc_client = ctx.obj['asc_client']

    template = Template_YAML()
    template.load(template_file)

    body = {
        'Name': stack_name,
        'Template': json.dumps(template.content),
        'TimeoutMins': timeout_mins,
        'DisableRollback': disable_rollback
    }

    if parameters_file is not None:
        parameters = Template_YAML()
        parameters.load(parameters_file)
        body['Parameters'] = parameters.content

    request = CreateStacksRequest()
    request.set_content(json.dumps(body))
    request.set_content_type('application/json')

    send_request(asc_client, request)
