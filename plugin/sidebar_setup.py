import bpy

### PANEL OPS
class ShreddedCreatePanel(bpy.types.Panel):
    bl_category = "Create"
    bl_label = "Shredded"
    bl_idname = "SHREDDED_ADD"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = self.layout.column(align=True)
        row = col.row(align=True)

        row.label(text="Preset Meshes:")


### REGISTER

def register():
    bpy.utils.register_class(ShreddedCreatePanel)

def unregister():
    bpy.utils.unregister_class(ShreddedCreatePanel)