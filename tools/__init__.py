if "bpy" in locals():
    import importlib
    importlib.reload(common)
    importlib.reload(definitions)
    importlib.reload(geometry)
    importlib.reload(preset_meshes)
    importlib.reload(shaders)
else:
    import bpy
    from . import common
    from . import definitions
    from . import geometry
    from . import preset_meshes
    from . import shaders