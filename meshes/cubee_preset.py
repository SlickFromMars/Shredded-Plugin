###SUS BUTTON

if "bpy" in locals():
    import importlib
    importlib.reload(cubee_data)
else:
    from . import cubee_data

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

class AddCubee(Operator, AddObjectHelper):
    """Create Cubee From Project Expansion"""
    bl_idname = "mesh.add_cubee"
    bl_label = "Add Cubee Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        add_sus_object(self, context)

        return {'FINISHED'}

def add_sus_object(self, context):
    mesh = bpy.data.meshes.new(name="Cubee")
    mesh.from_pydata(cubee_data.cubee_verts, cubee_data.cubee_edges, cubee_data.cubee_faces)
    # useful for development when the mesh may be invalid.
    object_data_add(context, mesh, operator=self)
    location = self.location