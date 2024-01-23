import json
from aliyunsdkcore.client import AcsClient, AcsRequest
from aliyunsdkros.request.v20150901.DescribeStacksRequest import DescribeStacksRequest


def find_stack_id(acs_client: AcsClient, stack_name: str) -> str:
    request = DescribeStacksRequest()
    request.set_Name(stack_name)

    _, _, body = acs_client.get_response(request)
    response = json.loads(body)

    if response['TotalCount'] > 1:
        raise ValueError(f'Stack not unique with name: {stack_name}')

    if response['TotalCount'] == 0:
        raise ValueError(f'Stack not found with name: {stack_name}')

    return response['Stacks'][0]['Id']


def send_request(acs_client: AcsClient, request: AcsRequest):
    status, _, body = acs_client.get_response(request)

    if 200 <= status < 300:
        print(json.loads(body))
        return

    raise RuntimeError(f'Unexpected errors: status={status}, error={body}')
