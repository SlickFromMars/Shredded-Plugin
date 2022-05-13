bl_info = {
    "name": "Shredded Blender Plugin",
    "author": "SlickFromMars",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View 3D > Sidebar > Shredded Tab",
    "description": "A powerful plugin with many functions.",
    "warning": "",
    "tracker_url": "https://github.com/SlickFromMars/Shredded-Plugin/issues/new/choose",
    "category": "3D View",
}

if "bpy" in locals():
    import importlib
    importlib.reload(registry)
    importlib.reload(tools)
    importlib.reload(ui)
else:
    from .tools import registry
    from . import tools
    from . import ui


import bpy

### REGISTER

def register():
    print("Loading SHREDDED...")

    registry.register_classes()
    tools.definitions.register_enums()

    print("\nLoaded successfully.")
    
def unregister():
    print("Unloading SHREDDED...")

    registry.unregister_classes()

    print("\nUnloaded successfully. Sorry to see you go.")
    
    
if __name__ == "__main__":
    register()