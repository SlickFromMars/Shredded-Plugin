if "bpy" in locals():
    import importlib
    importlib.reload(geometry)
    importlib.reload(credits)
    importlib.reload(shaders)
    importlib.reload(preset_meshes)
else:
    import bpy
    from . import geometry
    from . import credits
    from . import shaders
    from . import preset_meshes