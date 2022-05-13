import bpy

### DROPDOWN
def get_objects():
    return bpy.context.scene.objects

comp_types = [
    'MESH'
]

def get_named_obj(obj_name=None):
    if not obj_name:
        obj_name = bpy.context.scene.geoclip_list

    for obj in get_objects():
        if obj.type in comp_types:
            if (obj_name and obj.name == obj_name) or not obj_name:
                return obj
    return None

def get_comp_objects():
    objects = []
    for obj in get_objects():
        if obj.type in comp_types:
            objects.append(obj)
    return objects

def get_comp_list(self, context):
    choices = []
    
    for item in get_comp_objects():
        name = item.data.name
        choices.append((item.name, name, item.name))
        
    if len(choices) == 0:
        choices.append(('None', 'None', 'None'))

    bpy.types.Object.Enum = sorted(choices, key=lambda x: tuple(x[0].lower()))
    return bpy.types.Object.Enum

def update_shredded_list(self=None, context=None):
    print("UPDATING LIST")