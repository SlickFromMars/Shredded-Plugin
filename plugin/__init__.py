bl_info = {
    "name": "Shredded Blender Plugin",
    "author": "SlickFromMars",
    "version": (0, 2, 5),
    "blender": (2, 80, 0),
    "location": "View 3D > Sidebar > Create Tab",
    "description": "A powerful plugin with many functions.",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

if "bpy" in locals():
    import importlib
    importlib.reload(shaders)
    importlib.reload(meshes)
else:
    from . import shaders
    from . import meshes


import bpy

### REGISTER

classes = [
    
]

def register():
    print("Loading SHREDDED...")

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    shaders.register()
    meshes.register()

    print("\nLoaded successfully.")
    
def unregister():
    print("Unloading SHREDDED...")

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    shaders.unregister()
    meshes.unregister()

    print("\nUnloaded successfully. Sorry to see you go.")
    
    
if __name__ == "__main__":
    register()