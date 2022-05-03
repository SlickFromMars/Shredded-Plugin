import bpy
from bpy.types import (
    Operator,
    Panel,
    PropertyGroup,
)

class Shredded_Panel(Panel):
    bl_label = "Ivy Generator"
    bl_idname = "CURVE_PT_IvyGenPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager
        col = layout.column(align=True)

def centerThing():
    bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)