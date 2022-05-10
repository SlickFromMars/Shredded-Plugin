bl_info = {
    "name": "Shredded Blender Plugin",
    "author": "SlickFromMars",
    "version": (0, 3, 0),
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

    shaders.register()
    meshes.register()

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    print("\nLoaded successfully.")
    
def unregister():
    print("Unloading SHREDDED...")

    shaders.unregister()
    meshes.unregister()

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    print("\nUnloaded successfully. Sorry to see you go.")
    
    
if __name__ == "__main__":
    register()