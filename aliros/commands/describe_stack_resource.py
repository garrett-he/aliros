import json
from aliyunsdkros.request.v20150901.DescribeResourceDetailRequest import DescribeResourceDetailRequest
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest

import click


@click.command('describe-stack-resource')
@click.option('--stack-name', help='Name of stack.', required=True)
@click.option('--resource-name', help='Name of resource.', required=True)
def describe_stack_resource_command(ctx: click.Context, stack_name: str, resource_name: str):
    """Describe the specified resource in stack."""

    asc_client = ctx.obj['asc_client']

    request = DescribeStacksRequest()
    request.set_Name(stack_name)
    status, headers, body = asc_client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] != 1:
        raise Exception('Stacks with name "%s" not unique.' % stack_name)

    stack_id = response['Stacks'][0]['Id']

    request = DescribeResourceDetailRequest()

    request.set_StackName(stack_name)
    request.set_StackId(stack_id)
    request.set_ResourceName(resource_name)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
