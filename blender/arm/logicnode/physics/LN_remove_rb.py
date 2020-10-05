import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class RemovePhysicsNode (ArmLogicTreeNode):
    """Removes the rigid body from the given object."""
    bl_idname = 'LNRemovePhysicsNode'
    bl_label = 'Remove RB'
    arm_version = 1

    def init(self, context):
        super(RemovePhysicsNode, self).init(context)
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'RB')
        self.outputs.new('ArmNodeSocketAction', 'Out')

add_node(RemovePhysicsNode, category=PKG_AS_CATEGORY)
