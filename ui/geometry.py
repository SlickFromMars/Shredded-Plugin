if "bpy" in locals():
    import importlib
    importlib.reload(geometry)
    importlib.reload(common)
    importlib.reload(globs)
else:
    from ..tools import geometry
    from ..tools import common
    from .. import globs
import bpy

from bpy_extras.io_utils import ExportHelper

###THE PANEL
class SHREDDED_geo_panel(bpy.types.Panel):
    bl_label = "Geometry Tools"
    bl_idname = "SHREDDED.geopanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shredded"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        col = box.column(align=True)

        scale_big = 1.8
        scale_small = 1.2

        obj_count = len(common.get_comp_objects())
        if obj_count == 0:
            row = col.row(align=True)
            row.label(text="No objects in scene.")
        else:
            col.separator()
            row = col.row(align=True)
            row.scale_y = scale_small
            row.prop(context.scene, 'geoclip_list', icon='OUTLINER_OB_MESH')

            col = layout.column(align=True)
            row = col.row(align=True)
            row.scale_y = scale_small
            if not context.scene.expand_clip:
                row.prop(context.scene, 'expand_clip', icon='ADD', emboss=True, expand=False, toggle=False, event=False)
            else:
                row.prop(context.scene, 'expand_clip', icon='REMOVE', emboss=True, expand=False, toggle=False, event=False)
                box = layout.box()
                col = box.column(align=True)

                col.label(text="Copy Mesh PyData")
                row = col.row(align=True)
                row.scale_y = scale_small
                row.operator(GEO_CLIP_verts.bl_idname, icon= 'VERTEXSEL')
                row.operator(GEO_CLIP_edges.bl_idname, icon= 'EDGESEL')
                row = col.row(align=True)
                row.scale_y = scale_small
                row.operator(GEO_CLIP_faces.bl_idname, icon= 'FACESEL')
        
        
###THE BUTTONS
class GEO_CLIP_verts(bpy.types.Operator):
    bl_label = "Vertices"
    bl_idname = 'geocopy.verts'
    
    def execute(self, context):
        try:
            geometry.get_geo("vert")
            self.report({'INFO'}, 'Added to clipboard!')
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
    
class GEO_CLIP_edges(bpy.types.Operator):
    bl_label = "Edges"
    bl_idname = 'geocopy.edges'
    
    def execute(self, context):
        try:
            geometry.get_geo("edge")
            self.report({'INFO'}, 'Added to clipboard!')
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
    
class GEO_CLIP_faces(bpy.types.Operator):
    bl_label = "Faces"
    bl_idname = 'geocopy.faces'
    
    def execute(self, context):
        try:
            geometry.get_geo("face")
            self.report({'INFO'}, 'Added to clipboard!')
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}