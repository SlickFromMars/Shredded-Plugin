if "bpy" in locals():
    import importlib
    importlib.reload(geometry)
else:
    from ..tools import geometry
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

        if len(bpy.context.scene.objects) == 0:
            row = col.row(align=True)
            row.label(text="No objects in scene.")
            
        elif bpy.context.object.select_get() == False:
            row = col.row(align=True)
            row.label(text="No object selected.") 
            
        elif bpy.context.object.type == 'MESH':
            col.label(text="Mesh Data")
            row = col.row(align=True)
            row.operator(GEO_CLIP_verts.bl_idname, icon= 'VERTEXSEL')
            row = col.row(align=True)
            row.operator(GEO_CLIP_edges.bl_idname, icon= 'EDGESEL')
            row = col.row(align=True)
            row.operator(GEO_CLIP_faces.bl_idname, icon= 'FACESEL')
            
        else:
            row = col.row(align=True)
            row.label(text="Selection is not compatible.")
        
        
###THE BUTTONS
class GEO_CLIP_verts(bpy.types.Operator):
    bl_label = "Copy Vertices"
    bl_idname = 'geocopy.verts'
    
    def execute(self, context):
        try:
            geometry.get_geo("vert")
            self.report({'INFO'}, 'Added to clipboard!')
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
    
class GEO_CLIP_edges(bpy.types.Operator):
    bl_label = "Copy Edges"
    bl_idname = 'geocopy.edges'
    
    def execute(self, context):
        try:
            geometry.get_geo("edge")
            self.report({'INFO'}, 'Added to clipboard!')
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
    
class GEO_CLIP_faces(bpy.types.Operator):
    bl_label = "Copy Faces"
    bl_idname = 'geocopy.faces'
    
    def execute(self, context):
        try:
            geometry.get_geo("face")
            self.report({'INFO'}, 'Added to clipboard!')
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}