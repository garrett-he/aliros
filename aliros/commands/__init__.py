from .abandon_stack import abandon_stack_command
from .create_stack import create_stack_command
from .delete_stack import delete_stack_command
from .describe_resource_type import describe_resource_type_command
from .describe_resource_type_template import describe_resource_type_template_command
from .describe_stack import describe_stack_command
from .describe_stack_resource import describe_stack_resource_command
from .describe_stack_template import describe_stack_template_command
from .list_regions import list_regions_command

command_group = [
    abandon_stack_command,
    create_stack_command,
    delete_stack_command,
    describe_resource_type_command,
    describe_resource_type_template_command,
    describe_stack_command,
    describe_stack_resource_command,
    describe_stack_template_command,
    list_regions_command,
]
