if "bpy" in locals():
    import importlib
    importlib.reload(globs)
else:
    from .. import globs

import bpy
import webbrowser

### PANEL
class ShreddedCreditsPanel(bpy.types.Panel):
    bl_label = "Credits & Support"
    bl_idname = "SHREDDED.credits"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shredded"
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.label(text="Contributors")

        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator(YoutubeButton.bl_idname)

        col.separator()
        col.separator()

        row = col.row(align=True)
        row.label(text="Found a bug? Suggestion?")
        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator(IssueButton.bl_idname)
        col.separator()
        
        row = col.row(align=True)
        row.operator(LatestPatchButton.bl_idname, icon= "WORDWRAP_ON")

### BUTTONS

class YoutubeButton(bpy.types.Operator):
    bl_idname = 'shredded.youtube'
    bl_label = 'SlickFromMars'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open(globs.youtube_link)

        return {'FINISHED'}

class LatestPatchButton(bpy.types.Operator):
    bl_idname = 'shredded.latest'
    bl_label = 'Latest Patch Notes'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open(globs.repo_link + "/releases")

        self.report({'INFO'}, 'Opened GitHub!')
        return {'FINISHED'}

class IssueButton(bpy.types.Operator):
    bl_idname = 'shredded.issues'
    bl_label = 'Let Us Know!'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open(globs.issue_link)

        self.report({'INFO'}, 'Opened Issue Reports!')
        return {'FINISHED'}