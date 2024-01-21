import json
from aliros.template import Template_YAML
from aliros.stack import send_request
from aliyunsdkros.request.v20150901.ValidateTemplateRequest import ValidateTemplateRequest

import click


@click.command('validate-template')
@click.option('--template-file', help='Path of template file.', required=True, type=click.Path(exists=True, dir_okay=False))
def validate_template_command(ctx: click.Context, template_file: str):
    """Validate the specified template."""

    asc_client = ctx.obj['asc_client']

    template = Template_YAML()
    template.load(template_file)

    body = {
        'Template': json.dumps(template.content),
    }

    request = ValidateTemplateRequest()
    request.set_content(json.dumps(body))
    request.set_content_type('application/json')

    send_request(asc_client, request)
