from marshmallow import Schema, fields, post_load

from floyd.constants import DEFAULT_DOCKER_IMAGE, DEFAULT_ENV, DEFAULT_ARCH
from floyd.model.base import BaseModel


class ModuleSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    command = fields.Str()
    mode = fields.Str(allow_none=True)
    enable_tensorboard = fields.Boolean()
    module_type = fields.Str()
    # TODO: remove default_container once we fully migrated to env mapping
    default_container = fields.Str(allow_none=True)
    family_id = fields.Str(allow_none=True)
    outputs = fields.List(fields.Dict)
    inputs = fields.List(fields.Dict)
    env = fields.Str()
    arch = fields.Str()
    resource_id = fields.Str()

    @post_load
    def make_module(self, data):
        return Module(**data)


class Module(BaseModel):
    schema = ModuleSchema(strict=True)
    default_outputs = [{'name': 'output', 'type': 'dir'}]
    default_inputs = [{'name': 'input', 'type': 'dir'}]

    def __init__(self,
                 name,
                 description,
                 command,
                 mode="cli",
                 enable_tensorboard=False,
                 module_type="code",
                 default_container=DEFAULT_DOCKER_IMAGE,
                 family_id=None,
                 outputs=default_outputs,
                 inputs=default_inputs,
                 env=DEFAULT_ENV,
                 arch=DEFAULT_ARCH,
                 resource_id=None,):
        self.name = name
        self.description = description
        self.command = command
        self.mode = mode
        self.enable_tensorboard = enable_tensorboard
        self.module_type = module_type
        self.default_container = default_container
        self.family_id = family_id
        self.outputs = outputs
        self.inputs = inputs
        self.env = env
        self.arch = arch
        self.resource_id = resource_id
