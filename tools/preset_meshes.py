if "bpy" in locals():
    import importlib
    importlib.reload(low_poly_amogus_data)
    importlib.reload(cubee_data)
else:
    from ..resources.preset_data import low_poly_amogus_data
    from ..resources.preset_data import cubee_data

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


### AMOGUS

def add_sus_object(self, context):
    mesh = bpy.data.meshes.new(name="Amogus")
    mesh.from_pydata(low_poly_amogus_data.sussy_verts, low_poly_amogus_data.sussy_edges, low_poly_amogus_data.sussy_faces)
    # useful for development when the mesh may be invalid.
    object_data_add(context, mesh, operator=self)
    location = self.location


### CUBEE!!!

def add_cubee_object(self, context):
    mesh = bpy.data.meshes.new(name="Cubee")
    mesh.from_pydata(cubee_data.cubee_verts, cubee_data.cubee_edges, cubee_data.cubee_faces)
    # useful for development when the mesh may be invalid.
    object_data_add(context, mesh, operator=self)
    location = self.location