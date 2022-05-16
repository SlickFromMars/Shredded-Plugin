import bpy

from bpy.types import Scene
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty, CollectionProperty

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
            ("FOIL", 'Shiny Foil', '')
        ]
    )
