if "bpy" in locals():
    import importlib
    importlib.reload(globs)
else:
    from .. import globs

import bpy
import webbrowser

class ShreddedSupportPanel(bpy.types.Panel):
    bl_label = "Support"
    bl_idname = "SHREDDED.support"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shredded"
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)

        row = col.row(align=True)
        row.operator(IssueButton.bl_idname)

class IssueButton(bpy.types.Operator):
    bl_idname = 'shredded.issues'
    bl_label = 'Report An Issue'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open(globs.issue_link)

        self.report({'INFO'}, 'Opened Issue Reports!')
        return {'FINISHED'}