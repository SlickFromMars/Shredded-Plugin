import bpy

### FOIL SHADER
class SHADER_OT_FOIL(bpy.types.Operator):
    bl_label = "Foil"
    bl_idname = "shader.foil_ops"

    def execute(self, context):
        material_foil = bpy.data.materials.new(name="Foil Shader")
        material_foil.use_nodes = True

        material_output = material_foil.node_tree.nodes.get('Material Output')
        material_output.location = [500, 0]

        material_main = material_foil.node_tree.nodes.get('Principled BSDF')
        material_main.location = [200, 0]
        material_main.inputs[6].default_value = 1
        material_main.inputs[9].default_value = 0

        material_bump = material_foil.node_tree.nodes.new('ShaderNodeBump')
        material_bump.location = [0, 0]
        material_bump.inputs[0].default_value = 0.1

        material_shape = material_foil.node_tree.nodes.new('ShaderNodeTexMusgrave')
        material_shape.location = [-200, 0]
        material_shape.inputs[2].default_value = 1
        material_shape.inputs[3].default_value = 16

        material_foil.node_tree.links.new(material_shape.outputs[0], material_bump.inputs[2])
        material_foil.node_tree.links.new(material_bump.outputs[0], material_main.inputs[22])

        bpy.context.object.active_material = material_foil
        
        return{'FINISHED'}  