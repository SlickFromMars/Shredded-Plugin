import bpy
         
### GALAXY SHADER
class SHADER_OT_GALAXY(bpy.types.Operator):
    bl_label = "Galaxy"
    bl_idname = 'shader.galaxy_ops'
    
    def execute(self, context):
        material_galaxy = bpy.data.materials.new(name="Galaxy Volume")
        material_galaxy.use_nodes = True
        
        material_galaxy.node_tree.nodes.remove(material_galaxy.node_tree.nodes.get('Principled BSDF'))
        
        material_output = material_galaxy.node_tree.nodes.get('Material Output')
        material_output.location = [400, 0]
        
        noise1_node = material_galaxy.node_tree.nodes.new('ShaderNodeTexNoise')
        noise1_node.location = [-800, 75]
        noise1_node.inputs[2].default_value = 3.5
        noise1_node.inputs[3].default_value = 50
        noise1_node.inputs[4].default_value = 0.6
        noise1_node.hide = True
        
        noise2_node = material_galaxy.node_tree.nodes.new('ShaderNodeTexNoise')
        noise2_node.location = [-800, -175]
        noise2_node.inputs[2].default_value = 3.6
        noise2_node.inputs[3].default_value = 50
        noise2_node.inputs[4].default_value = 0.5
        noise2_node.hide = True
        
        ramp1_node = material_galaxy.node_tree.nodes.new('ShaderNodeValToRGB')
        ramp1_node.location = [-600, 75]
        ramp1_node.color_ramp.elements[0].position = 0.52
        ramp1_node.color_ramp.elements[0].color = (0, 0, 0, 1)
        ramp1_node.color_ramp.elements[1].position = 1
        ramp1_node.color_ramp.elements[1].color = (1, 1, 1, 1)
        ramp1_node.hide = True
        
        ramp2_node = material_galaxy.node_tree.nodes.new('ShaderNodeValToRGB')
        ramp2_node.location = [-600, -175]
        ramp2_node.color_ramp.elements[0].position = 0.8
        ramp2_node.color_ramp.elements[0].color = (0, 0, 0, 1)
        ramp2_node.color_ramp.elements[1].position = 1
        ramp2_node.color_ramp.elements[1].color = (1, 1, 1, 1)
        ramp2_node.hide = True
        
        mix_node = material_galaxy.node_tree.nodes.new('ShaderNodeMixRGB')
        mix_node.location = [-250, 0]
        mix_node.blend_type = 'MIX'
        mix_node.inputs[0].default_value = 0.5
        mix_node.hide = True
        
        volume_node = material_galaxy.node_tree.nodes.new('ShaderNodeVolumePrincipled')
        volume_node.location = [0, 0]
        volume_node.inputs[0].default_value = (0.5, 0.5, 0.5, 1)
        volume_node.inputs[4].default_value = 0.5
        volume_node.hide = True
        
        material_galaxy.node_tree.links.new(noise1_node.outputs[1], ramp1_node.inputs[0])
        material_galaxy.node_tree.links.new(noise2_node.outputs[1], ramp2_node.inputs[0])
        material_galaxy.node_tree.links.new(ramp1_node.outputs[0], mix_node.inputs[0])
        material_galaxy.node_tree.links.new(ramp2_node.outputs[0], mix_node.inputs[1])
        material_galaxy.node_tree.links.new(mix_node.outputs[0], volume_node.inputs[2])
        material_galaxy.node_tree.links.new(volume_node.outputs[0], material_output.inputs[1])
        
        bpy.context.object.active_material = material_galaxy
        
        return{'FINISHED'}        