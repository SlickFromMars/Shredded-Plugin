if "bpy" in locals():
    import importlib
    importlib.reload(shaders)
else:
    from ..tools import shaders

import bpy

### PANEL FOR STUFF
class ShaderPanel(bpy.types.Panel):
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
        row.scale_y = 1.2
        row.prop(context.scene, 'shader_presets', icon='MATSHADERBALL')
        
        row = layout.row()
        row.operator(SHADER_OT_ADD.bl_idname)

### BUTTON
class SHADER_OT_ADD(bpy.types.Operator):
    bl_label = "Add Shader"
    bl_idname = 'shader.galaxy_ops'
    
    def execute(self, context):
        shaders.CREATE_shader_main(self, context)
        self.report({'INFO'}, 'Shader added.')
        
        return{'FINISHED'}