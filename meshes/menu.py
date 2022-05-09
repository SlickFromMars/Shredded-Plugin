if "bpy" in locals():
    import importlib
    importlib.reload(low_poly_amogus)
else:
    from . import low_poly_amogus

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

###PRESET MESH MENU

class VIEW3D_MT_mesh_presets(Menu):
    bl_idname = "VIEW3D_MT_mesh_presets"
    bl_label = "Shredded Presets"
    
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator('mesh.add_sus', text="LowPoly Amogus", icon='MEMORY')