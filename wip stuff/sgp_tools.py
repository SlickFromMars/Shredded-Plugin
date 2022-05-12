import bpy

### UI
class SHREDDED_sgp_tools(bpy.types.Panel):
    bl_label = "SGP Tools"
    bl_idname = "SHREDDED.sgp.panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shredded"
    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        col = box.column(align=True)
        
        row = col.row(align=True)
        row.scale_y = 2
            
        row.operator(SGP_import.bl_idname, icon= "IMPORT")
        
        if bpy.context.object.type == 'MESH' and bpy.context.object.select_get() == True and len(bpy.context.scene.objects) != 0:
            
            row.operator(SGP_export.bl_idname, icon= "EXPORT")
            
class SHREDDED_sgp_settings(bpy.types.Panel):
    bl_label = "Model Options"
    bl_idname = "SHREDDED.sgp.settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shredded"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        col = box.column(align=True)
        
        row = col.row(align=True)
        row.label(text="Settings", icon="SETTINGS")
        
            
###THE BUTTONS
class SGP_import(bpy.types.Operator):
    bl_label = "Import"
    bl_idname = 'sgp.import'
    
    def execute(self, context):
        import_sgp()
        
        return{"FINISHED"}

class SGP_export(bpy.types.Operator):
    bl_label = "Export"
    bl_idname = 'sgp.export'
    
    def execute(self, context):
        export_sgp()
        
        return{"FINISHED"}

### FUNCTIONS

def import_sgp():
    print("this too")
    
def export_sgp():
    print("make this at some point lol")
    
### REGISTRATION
classes = [
    SHREDDED_sgp_tools,
    SHREDDED_sgp_settings,
    SGP_import,
    SGP_export
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