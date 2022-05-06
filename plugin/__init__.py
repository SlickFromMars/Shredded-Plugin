bl_info = {
    "name": "Shredded Blender Plugin",
    "author": "SlickFromMars",
    "version": (0, 2),
    "blender": (2, 80, 0),
    "location": "View 3D > Sidebar > Create Tab",
    "description": "A powerful plugin with many functions.",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

if "bpy" in locals():
    import importlib
    importlib.reload(add_mesh_sus)
    importlib.reload(galaxy_node)
else:
    from . import add_mesh_sus
    from . import galaxy_node

import bpy


def register():
    add_mesh_sus.register()
    galaxy_node.register()
    

def unregister():
    add_mesh_sus.unregister()
    galaxy_node.unregister()
    