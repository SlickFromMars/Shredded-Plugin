if "bpy" in locals():
    import importlib
    importlib.reload(geometry)
    importlib.reload(preset_meshes)
    importlib.reload(shaders)
else:
    import bpy
    from . import geometry
    from . import preset_meshes
    from . import shaders