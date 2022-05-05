bl_info = {
    "name": "Shredded Blender Plugin",
    "author": "SlickFromMars",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View 3D > Sidebar > Shredded",
    "description": "A powerful plugin with many functions.",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

if "bpy" in locals():
    import importlib
    importlib.reload(add_mesh_sus)
else:
    from . import add_mesh_sus

import bpy


def register():
    add_mesh_sus.register()

def unregister():
    add_mesh_sus.unregister()
    