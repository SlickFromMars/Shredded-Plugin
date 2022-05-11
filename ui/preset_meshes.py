if "bpy" in locals():
    import importlib
    importlib.reload(preset_meshes)
else:
    from ..tools import preset_meshes

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

### DEFINE EXTRAS

class VIEW3D_MT_mesh_presets(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_mesh_presets"
    bl_label = "Shredded Presets"
    
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator('mesh.add_sus', text="LowPoly Amogus", icon='MEMORY')
        layout.operator('mesh.add_cubee', text="Cubee", icon='MOD_WIREFRAME')


###AMOGUS
class AddSus(Operator, AddObjectHelper):
    """Create a Low Polygon Amogus"""
    bl_idname = "mesh.add_sus"
    bl_label = "Add Amogus Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        preset_meshes.add_sus_object(self, context)

        return {'FINISHED'}


###CUBEE
class AddCubee(Operator, AddObjectHelper):
    """Create Cubee From Project Expansion"""
    bl_idname = "mesh.add_cubee"
    bl_label = "Add Cubee Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        preset_meshes.add_cubee_object(self, context)

        return {'FINISHED'}