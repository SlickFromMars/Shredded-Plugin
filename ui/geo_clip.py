if "bpy" in locals():
    import importlib
    importlib.reload(geometry)
    importlib.reload(common)
else:
    from ..tools import geometry
    from ..tools import common
import bpy

###THE PANEL
class SHREDDED_geo_clip(bpy.types.Panel):
    bl_label = "Geometry Clipboard"
    bl_idname = "SHREDDED.geoclip"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shredded"
    # bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        col = box.column(align=True)

        obj_count = len(common.get_comp_objects())
        if obj_count == 0:
            row = col.row(align=True)
            row.label(text="No objects in scene.")
        else:
            col.label(text="Copy Mesh Data")
            row = col.row(align=True)
            row.scale_y = 1.2
            row.operator(GEO_CLIP_verts.bl_idname, icon= 'VERTEXSEL')
            row.operator(GEO_CLIP_edges.bl_idname, icon= 'EDGESEL')
            row = col.row(align=True)
            row.operator(GEO_CLIP_faces.bl_idname, icon= 'FACESEL')

        if obj_count > 1:
            col.separator()
            row = col.row(align=True)
            row.scale_y = 1.1
            row.prop(context.scene, 'geoclip_list', icon='ARMATURE_DATA')  
        
        
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