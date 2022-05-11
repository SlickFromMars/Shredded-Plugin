if "bpy" in locals():
    import importlib
    importlib.reload(globs)
else:
    from .. import globs

import bpy
import webbrowser

class ShreddedCreditsPanel(bpy.types.Panel):
    bl_label = "Credits"
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
        row.label(text="Created by SlickFromMars")

        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator(GithubButton.bl_idname)
        
        row = col.row(align=True)
        row.operator(YoutubeButton.bl_idname)
        
class GithubButton(bpy.types.Operator):
    bl_idname = 'shredded.github'
    bl_label = 'Github'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open(globs.github_link)

        self.report({'INFO'}, 'Opened GitHub!')
        return {'FINISHED'}
    
class YoutubeButton(bpy.types.Operator):
    bl_idname = 'shredded.youtube'
    bl_label = 'Youtube'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open(globs.youtube_link)

        self.report({'INFO'}, 'Opened Youtube!')
        return {'FINISHED'}