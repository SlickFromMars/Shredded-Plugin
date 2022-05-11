if "bpy" in locals():
    import importlib
    importlib.reload(geo_clip)
    importlib.reload(credits)
    importlib.reload(shaders)
    importlib.reload(preset_meshes)
    importlib.reload(support)
else:
    import bpy
    from . import geo_clip
    from . import credits
    from . import shaders
    from . import preset_meshes
    from . import support