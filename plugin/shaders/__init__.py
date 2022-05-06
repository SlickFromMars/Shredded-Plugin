if "bpy" in locals():
    import importlib
    importlib.reload(galaxy)
else:
    from . import galaxy

import bpy

### PANEL FOR STUFF
class TestPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Shredded Presets"
    bl_idname = "OBJECT_PT_shader_presets"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Shredded"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        layout.label(text= "Select A Shader Preset To Be Added.")
        
        row = layout.row()
        row.operator('shader.galaxy_ops')

### REGISTER
classes = [
    TestPanel,
    galaxy.SHADER_OT_GALAXY
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()