import os
import bpy

icon_collections = {}

icons_read = {
    'slick.png': 'slick',
}

def register_icons():
    # Note that preview collections returned by bpy.utils.previews
    # are regular py objects - you can use them to store custom data.
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    icons_dir = os.path.join(os.path.dirname(__file__), "thumbnails")

    # load a preview thumbnail of a file and store in the previews collection
    for ir in icons_read.keys():
        pcoll.load(icons_read[ir], os.path.join(icons_dir, ir), 'IMAGE')

    icon_collections["main"] = pcoll


def unregister_icons():
    for pcoll in icon_collections.values():
        bpy.utils.previews.remove(pcoll)
    icon_collections.clear()