###SUS BUTTON

if "bpy" in locals():
    import importlib
    importlib.reload(low_poly_amogus_data)
else:
    from . import low_poly_amogus_data

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

class AddSus(Operator, AddObjectHelper):
    """Create a Low Polygon Amogus"""
    bl_idname = "mesh.add_sus"
    bl_label = "Add Amogus Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        add_sus_object(self, context)

        return {'FINISHED'}

def add_sus_object(self, context):
    mesh = bpy.data.meshes.new(name="Amogus")
    mesh.from_pydata(low_poly_amogus_data.sussy_verts, low_poly_amogus_data.sussy_edges, low_poly_amogus_data.sussy_faces)
    # useful for development when the mesh may be invalid.
    object_data_add(context, mesh, operator=self)
    location = self.location