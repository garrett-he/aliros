import json
from aliyunsdkros.request.v20150901.DescribeEventsRequest import DescribeEventsRequest
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest

import click


@click.command('list-stack-events')
@click.option('--stack-name', help='Name of stack', required=True)
@click.option('--resource-status', help='Status of resource', required=False)
@click.option('--resource-name', help='Name of resource', required=False)
@click.option('--resource-type', help='Type of resource', type=int, default=1, required=False)
@click.option('--page-number', help='Number of page', type=int, default=1, required=False)
@click.option('--page-size', help='Size of pages', type=int, default=10, required=False)
def list_stack_events_command(ctx: click.Context, stack_name: str, resource_status: str, resource_name: str, resource_type: int, page_number: int,
                              page_size: int):
    """List events of the specified stack."""

    asc_client = ctx.obj['asc_client']

    request = DescribeStacksRequest()
    request.set_Name(stack_name)
    status, headers, body = asc_client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] != 1:
        raise Exception('Stacks with name "%s" not unique.' % stack_name)

    stack_id = response['Stacks'][0]['Id']

    request = DescribeEventsRequest()

    request.set_StackName(stack_name)
    request.set_StackId(stack_id)

    resource_status and request.set_ResourceStatus(resource_status)
    resource_name and request.set_ResourceName(resource_status)
    resource_type and request.set_ResourceType(resource_status)
    request.set_PageNumber(page_number)
    request.set_PageSize(page_size)

    status, headers, body = asc_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return 0
    else:
        raise Exception('Unexpected errors: status=%d, error=%s' % (status, body))
