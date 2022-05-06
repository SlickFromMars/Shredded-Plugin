if "bpy" in locals():
    import importlib
    importlib.reload(low_poly_amogus)
else:
    from . import low_poly_amogus

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy.props import FloatVectorProperty
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
        
        
### DEFINE EXTRAS

def menu_func(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'

    layout.separator()
    layout.menu("VIEW3D_MT_mesh_presets",text="Shredded Presets", icon="OUTLINER_OB_GROUP_INSTANCE")
    
    layout.separator()
    

### REGISTER
classes = [
    VIEW3D_MT_mesh_presets,
    low_poly_amogus.AddSus
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    

if __name__ == "__main__":
    register()