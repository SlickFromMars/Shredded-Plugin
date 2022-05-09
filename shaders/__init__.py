if "bpy" in locals():
    import importlib
    importlib.reload(main)
    importlib.reload(galaxy)
    importlib.reload(foil)
else:
    from . import main
    from . import galaxy
    from . import foil

import bpy

### REGISTER
classes = [
    main.TestPanel,
    galaxy.SHADER_OT_GALAXY,
    foil.SHADER_OT_FOIL
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()