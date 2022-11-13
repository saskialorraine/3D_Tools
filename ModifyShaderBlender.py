import bpy 

#Iterate over all members of the material struct
for item in bpy.data.materials:
    #Enable "use_shadeless"
    item.node_tree.nodes["Principled BSDF"].inputs[4].default_value = 0
    item.blend_method = 'OPAQUE'
