if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    from .. import ui

import bpy

### OPEN THE MENU

def preset_func(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'

    layout.separator()
    layout.menu("VIEW3D_MT_mesh_presets",text="Shredded Presets", icon="OUTLINER_OB_GROUP_INSTANCE")
    
    layout.separator()

### REGISTRY

classes1 = [
    ui.preset_meshes.AddSus,
    ui.preset_meshes.AddCubee,
    ui.shaders.SHADER_OT_ADD,
    ui.geo_clip.GEO_CLIP_verts,
    ui.geo_clip.GEO_CLIP_edges,
    ui.geo_clip.GEO_CLIP_faces,
    ui.credits.YoutubeButton,
    ui.credits.IssueButton,
    ui.credits.LatestPatchButton
]
### For panels and stuff that would require prereqs
classes2 = [
    ui.preset_meshes.VIEW3D_MT_mesh_presets,
    ui.shaders.ShaderPanel,
    ui.geo_clip.SHREDDED_geo_clip,
    ui.credits.ShreddedCreditsPanel
]

def register_classes():
    classes = classes1 + classes2

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.append(preset_func)

def unregister_classes():
    classes = classes1 + classes2

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.remove(preset_func)