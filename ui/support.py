import bpy
import webbrowser

class ShreddedSupportPanel(bpy.types.Panel):
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
        row.scale_y = 1.4
        row.operator(GithubButton.bl_idname)
        
        row = col.row(align=True)
        row.operator(YoutubeButton.bl_idname)
        
class GithubButton(bpy.types.Operator):
    bl_idname = 'cats_credits.discord'
    bl_label = 'Github'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open('https://github.com/SlickFromMars/Shredded-Plugin')

        self.report({'INFO'}, 'Opened GitHub!')
        return {'FINISHED'}
    
class YoutubeButton(bpy.types.Operator):
    bl_idname = 'cats_credits.youtube'
    bl_label = 'Youtube'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        webbrowser.open('https://www.youtube.com/channel/UC7mKRZmigocWNRX63JV3Ttw')

        self.report({'INFO'}, 'Opened Youtube!')
        return {'FINISHED'}