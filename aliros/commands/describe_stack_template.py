import json
from aliyunsdkros.request.v20150901.DescribeTemplateRequest import DescribeTemplateRequest
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest

import click


@click.command('describe-stack-template')
@click.option('--stack-name', help='Name of stack.', required=True)
def describe_stack_template_command(ctx: click.Context, stack_name: str):
    """Describe template of the specified stack."""

    asc_client = ctx.obj['asc_client']

    request = DescribeStacksRequest()

    request.set_Name(stack_name)
    status, headers, body = asc_client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] != 1:
        raise Exception('Stacks with name "%s" not unique.' % stack_name)

    stack_id = response['Stacks'][0]['Id']

    request = DescribeTemplateRequest()

    request.set_StackName(stack_name)
    request.set_StackId(stack_id)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
