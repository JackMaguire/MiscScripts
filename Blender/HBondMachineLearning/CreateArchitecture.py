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
for x in range( 1, 6 ):
    layer_nodes.append( [] )
#first_layer_nodes = []
#second_layer_nodes = []
#third_layer_nodes = []
#fourth_layer_nodes = []
#fifth_layer_nodes = []
output_node = []

bpy.ops.group.create( name="input_nodes" )
for x in range( 1, 6 ):
    groupname = "layer_" + str(x) + "_nodes"
    bpy.ops.group.create( name=groupname )
bpy.ops.group.create( name="output_node" )

#create input nodes
for i in range( 0, 9 ):
    x = 5.0
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

for layer in range( 1, 6 ):
    for i in range( 0, 20 ):
        pass
