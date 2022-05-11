import bpy

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