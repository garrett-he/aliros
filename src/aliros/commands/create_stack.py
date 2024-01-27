import json

import click
from aliyunsdkros.request.v20190910.CreateStackRequest import CreateStackRequest

from aliros.template import YamlTemplate
from aliros.alicloud import send_request


@click.command('create-stack')
@click.option('--stack-name', help='Name of stack.', required=True)
@click.option('--template-file', help='Path of template file.', required=True, type=click.Path(exists=True, dir_okay=False))
@click.option('--parameters-file', help='URL of parameters file.', required=False, type=click.Path(exists=True, dir_okay=False))
@click.option('--timeout-mins', help='Minutes to timeout.', type=int, default=60)
@click.option('--disable-rollback', help='Disable rollback if failed.', required=False, is_flag=True, default=False)
@click.pass_context
def create_stack_command(ctx: click.Context, stack_name: str, template_file: str, parameters_file: str, timeout_mins: int, disable_rollback: bool):
    """Create a new stack."""

    acs_client = ctx.obj['acs_client']

    template = YamlTemplate()
    template.load(template_file)

    if parameters_file is not None:
        parameters = YamlTemplate()
        parameters.load(parameters_file)
        template.content['Parameters'] = parameters.content

    request = CreateStackRequest()
    request.set_StackName(stack_name)
    request.set_TemplateBody(json.dumps(template.content))
    request.set_TimeoutInMinutes(timeout_mins)
    request.set_DisableRollback(disable_rollback)

    send_request(acs_client, request)
