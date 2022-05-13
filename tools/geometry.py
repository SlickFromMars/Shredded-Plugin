import bpy
import json

from . import common

###THE FUNCTION
def get_geo(string):
    object = common.get_named_obj()

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

### JSON STUFF
json_dict = {}

def json_export():
    json_dict.clear()

    raw_verts = get_geo('vert')
    verts = []
    for i in raw_verts:
        data2 = []
        for i2 in i:
            data2.append(i2)
        verts.push(data2)

    json_dict['verts'] = verts
    json_dict['edges'] = get_geo('edge')
    json_dict['faces'] = get_geo('face')