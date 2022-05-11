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
        row.operator('shader.galaxy_ops')

        row = layout.row()
        row.operator('shader.foil_ops')

### GALAXY SHADER
class SHADER_OT_GALAXY(bpy.types.Operator):
    bl_label = "Galaxy"
    bl_idname = 'shader.galaxy_ops'
    
    def execute(self, context):
        shaders.CREATE_galaxy_shader(self, context)
        self.report({'INFO'}, 'Shader added.')
        
        return{'FINISHED'}

### FOIL SHADER
class SHADER_OT_FOIL(bpy.types.Operator):
    bl_label = "Foil"
    bl_idname = "shader.foil_ops"

    def execute(self, context):
        shaders.CREATE_foil_shader(self, context)
        self.report({'INFO'}, 'Shader added.')
        
        return{'FINISHED'}