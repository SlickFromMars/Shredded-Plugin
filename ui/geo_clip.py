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
        col = layout.column(align=True)
        row = col.row(align=True)
        row.label(text="Add PyData to clipboard.")

        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator(GEO_CLIP_verts.bl_idname, icon= 'VERTEXSEL')
        row = col.row(align=True)
        row.operator(GEO_CLIP_edges.bl_idname, icon= 'EDGESEL')
        row = col.row(align=True)
        row.operator(GEO_CLIP_faces.bl_idname, icon= 'FACESEL')
        
        
###THE BUTTONS
class GEO_CLIP_verts(bpy.types.Operator):
    bl_label = "Copy Vertices"
    bl_idname = 'geocopy.verts'
    
    def execute(self, context):
        try:
            get_geo("vert")
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
    
class GEO_CLIP_edges(bpy.types.Operator):
    bl_label = "Copy Edges"
    bl_idname = 'geocopy.edges'
    
    def execute(self, context):
        try:
            get_geo("edge")
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
    
class GEO_CLIP_faces(bpy.types.Operator):
    bl_label = "Copy Faces"
    bl_idname = 'geocopy.faces'
    
    def execute(self, context):
        try:
            get_geo("face")
        except:
            self.report({'ERROR'}, 'There was an error geting the data.')
        
        return{"FINISHED"}
        
        
###THE FUNCTION
def get_geo(string):
    object = bpy.context.object

    raw = []
    match(string):
        case "vert":
            raw = object.data.vertices
        case "edge":
            raw = object.data.edges
        case "face":
            raw = object.data.polygons
            
    data = []
    for i in raw:
        match(string):
            case "vert":
                data.append(i.co)
            case "edge":
                data2 = []
                for i2 in i.vertices:
                    data2.append(i2)
                data.append(data2)
            case "face":
                data2 = []
                for i2 in i.vertices:
                    data2.append(i2)
                data.append(data2)
    
    data_str = str(data)

    bpy.context.window_manager.clipboard = data_str
    return{"FINISHED"}