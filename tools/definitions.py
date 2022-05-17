import bpy

from bpy.types import Scene
from bpy.props import EnumProperty, BoolProperty

from . import common as Common

def register_enums():
    Scene.geoclip_list = EnumProperty(
        name= "Target",
        description= "Target to Copy",
        items= Common.get_comp_list,
        update= Common.update_shredded_list
    )

    Scene.shader_presets = EnumProperty(
        name= "Preset",
        description= "List of shaders.",
        items= [
            ("GALAXY", 'Galaxy', ''),
            ("FOIL", 'Shiny Foil', ''),
            ("MIRROR", 'Perfect Mirror', '')
        ]
    )

    Scene.expand_clip = BoolProperty(
        name= 'Expand Clipboard',
        default= True
    )
