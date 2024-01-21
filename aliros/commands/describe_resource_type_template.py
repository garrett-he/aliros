import json
from aliyunsdkros.request.v20150901.DescribeResourceTypeTemplateRequest import DescribeResourceTypeTemplateRequest

import click


@click.command('describe-resource-type-template')
@click.option('--type-name', help='Name of resource type.', required=True)
def describe_resource_type_template_command(ctx: click.Context, type_name: str):
    """Describe resource type template."""

    asc_client = ctx.obj['asc_client']
    request = DescribeResourceTypeTemplateRequest()

    request.set_TypeName(type_name)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
