if "bpy" in locals():
    import importlib
    importlib.reload(geo_clip)
    importlib.reload(support)
else:
    from . import geo_clip
    from . import support

import bpy

### REGISTER
classes = [
    geo_clip.SHREDDED_geo_clip,
    geo_clip.GEO_CLIP_verts,
    geo_clip.GEO_CLIP_edges,
    geo_clip.GEO_CLIP_faces,
    support.ShreddedSupportPanel,
    support.GithubButton,
    support.YoutubeButton
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