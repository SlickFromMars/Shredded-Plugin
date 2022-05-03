bl_info = {
    "name": "Shredded Blender Plugin",
    "author": "SlickFromMars",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > Shredded",
    "description": "A powerful plugin with many functions.",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy

import ui.panel

classes = (
    ui.panel.Shredded_Panel
)

def register():
    print("Loading Shredded...")

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    print("Removing Shredded")

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()