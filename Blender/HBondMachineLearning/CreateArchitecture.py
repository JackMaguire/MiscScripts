import bpy
import math
import re

#methods
def to_group(named, obj):
    '''
    named:   (string) name of group to use, or to create if not present 
    objs:    a collection of object references
    '''
    groups = bpy.data.groups

    # alias existing group, or generate new group and alias that
    group = groups.get(named, groups.new(named))

    if obj.name not in group.objects:
        group.objects.link(obj)


#data
input_nodes = []
layer_nodes = []
for x in range( 0, 5 ):
    layer_nodes.append( [] )
output_node = []

bpy.ops.group.create( name="input_nodes" )
for x in range( 0, 5 ):
    groupname = "layer_" + str(x) + "_nodes"
    bpy.ops.group.create( name=groupname )
bpy.ops.group.create( name="output_node" )

#create input nodes
for i in range( 0, 9 ):
    x = 8.0
    y = 8 - i * 2
    z = 0
    bpy.ops.mesh.primitive_cylinder_add(
        vertices = 128,
        radius = 0.5, 
        depth = 0.2,
        location = (x, y, z)   
    )
    node = bpy.context.object
    input_nodes.append( node )
    to_group( "input_nodes", node )

    #Location keyframes
    node.keyframe_insert( data_path="location", frame=1 )

    #start_frame = 130.0 - ( z - z_offset ) * 80.0 / 1.8
    #node.keyframe_insert( data_path="location", frame=start_frame )

    #node.location[2] = z
    #node.keyframe_insert( data_path="location", frame=130 )

for layer in range( 0, 5 ):
    groupname = "layer_" + str(layer) + "_nodes"
    for i in range( 0, 100 ):
        x = 15.0 + 7 * layer
        y = 50.0 - i
        z = 0
        bpy.ops.mesh.primitive_cylinder_add(
            vertices = 32,
            radius = 0.3, 
            depth = 0.1,
            location = (x, y, z)   
        )
        node = bpy.context.object
        layer_nodes[ layer ].append( node )
        to_group( groupname, node )

        #Location keyframes
        node.keyframe_insert( data_path="location", frame=1 )

        #start_frame = 130.0 - ( z - z_offset ) * 80.0 / 1.8
        #node.keyframe_insert( data_path="location", frame=start_frame )

        #node.location[2] = z
        #node.keyframe_insert( data_path="location", frame=130 )

for i in range( 0, 1 ):
    #dummy for-loop to create scope. Though not sure how useful this is in python
    x = 50
    y = 1
    z = 0
    bpy.ops.mesh.primitive_cylinder_add(
        vertices = 128,
        radius = 1, 
        depth = 0.1,
        location = (x, y, z)   
    )
    node = bpy.context.object
    output_node.append( node )
    to_group( "output_node", node )

    #Location keyframes
    node.keyframe_insert( data_path="location", frame=1 )

    #start_frame = 130.0 - ( z - z_offset ) * 80.0 / 1.8
    #node.keyframe_insert( data_path="location", frame=start_frame )

    #node.location[2] = z
    #node.keyframe_insert( data_path="location", frame=130 )



#Set Materials!
input_node_mat = bpy.data.materials.get("input_node")
if node_mat is None:
    node_mat = bpy.data.materials.new(name="input_node")
for node in input_nodes:
    if node.data.materials:
        node.data.materials[0] = node_mat
    else:
        node.data.materials.append( node_mat )

for layer in range( 0, 5 ):
    matname = "layer_" + str(layer) + "_material"
    node_mat = bpy.data.materials.get( matname )
    if node_mat is None:
        node_mat = bpy.data.materials.new(name=matname)
    for node in layer_nodes[ layer ]:
        if node.data.materials:
            node.data.materials[0] = node_mat
        else:
            node.data.materials.append( node_mat )

output_node_mat = bpy.data.materials.get("output_node")
if node_mat is None:
    node_mat = bpy.data.materials.new(name="output_node")
for node in output_node:
    if node.data.materials:
        node.data.materials[0] = node_mat
    else:
        node.data.materials.append( node_mat )

