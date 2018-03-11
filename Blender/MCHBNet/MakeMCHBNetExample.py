import bpy
import math
import re
#To run: exec( compile( open( "/home/jack/Desktop/blender_workdir/MCHBNetExample/make_graph.py" ).read(), "/home/jack/Desktop/blender_workdir/MCHBNetExample/make_graph.py", 'exec'))

R=0.1
D=0.1
scale=2*R

z_offset = D/2
z_gap = 2*D

green_nodes = []
blue_nodes = []
hbond_edges = []
clash_edges = []

green_coords = [ #11
    [ -1.17, -0.18 , 13 ],
    [ -1.8, -0.28 , 11 ],
    [ -2.5, -0.08 , 10 ],
    [ -3.1, -0.4 , 10 ],
    [ -2.9, 0.2 , 11 ],
    [ -2.5, 0.5 , 7 ],
    [ -1.7, 0.4 , 12 ],
    [ -1.17, 0.75 , 10 ],
    [ -0.6, 1.17 , 11 ],
    [ -0.07, 1.6 , 11 ],
    [ 0.5, 1.98, 10 ]
]

blue_coords = [ #8
    [ -2.4, -0.9 , 8 ],
    [ -1.5, -0.8 , 10 ],
    [ -0.8, -0.7 , 11 ],
    [ -1.8, 0.9 , 9 ],
    [ -1.5, 1.7 , 10 ],
    [ -1.0, 2.3 , 10 ],
    [ -0.4, 2.7 , 9 ],    
    [ 0.05, 3.2 , 10 ],    
]

g2b_hbond_edge_coords = [
    [ 0, 3, 1, 6 ],
    [ 0, 3, 1, 5 ],
    [ 0, 3, 1, 6 ],
    [ 0, 3, 1, 7 ],
    [ 1, 8, 1, 7 ],
    [ 1, 8, 0, 5 ],
    [ 1, 9, 1, 7 ],
    [ 1, 9, 0, 5 ],
    [ 2, 8, 0, 3 ],
    [ 2, 8, 0, 5 ],
    [ 3, 9, 0, 3 ],
    [ 3, 9, 0, 4 ],

    [ 5, 2, 3, 7 ],
    [ 5, 5, 3, 2 ],
    [ 6, 5, 3, 7 ],
    [ 7, 1, 3, 2 ],

    [ 8, 5, 4, 9 ],
    [ 8, 5, 4, 8 ],
    [ 8, 5, 4, 7 ],
    [ 8, 1, 5, 2 ],
    [ 8, 1, 6, 2 ],
    [ 8, 3, 6, 3 ],
    [ 8, 4, 6, 3 ],

    [ 10, 1, 7, 0 ],
    [ 10, 1, 7, 2 ],
    [ 10, 4, 6, 6 ],
    [ 10, 4, 6, 5 ],
    [ 10, 4, 6, 4 ],

#starting state
    [ 8, 5, 5, 3 ], 
    [ 8, 5, 5, 7 ],
    [ 8, 2, 5, 3 ], 
]

g2g_hbond_edge_coords = [
    [ 0, 2, 6, 2 ],
    [ 1, 9, 6, 5 ],
    [ 2, 8, 5, 5 ],

    [ 3, 2, 4, 4 ],
    [ 4, 0, 5, 1 ],
    [ 3, 2, 4, 4 ],

    [ 10, 5, 9, 6 ],
    [ 10, 3, 9, 7 ],
    [ 9, 2, 8, 4 ],

    [ 8, 7, 7, 9 ],
    [ 8, 2, 7, 2 ],
    [ 8, 1, 7, 2 ],

    [ 7, 2, 6, 2 ],
    [ 7, 3, 6, 5 ],
    [ 7, 7, 6, 7 ],
]

b2b_hbond_edge_coords = [
    [ 0, 3, 1, 5 ],
    [ 0, 2, 1, 0 ],
    [ 2, 8, 1, 7 ],
    [ 2, 1, 1, 1 ],

    [ 4, 1, 5, 2 ],
    [ 4, 6, 5, 6 ],
    [ 5, 3, 6, 4 ],
    [ 5, 4, 6, 4 ],
    [ 5, 5, 6, 4 ],

    [ 6, 4, 7, 4 ],
    [ 6, 1, 7, 1 ],
    [ 6, 5, 7, 5 ],
]

g2b_clash_edge_coords = [
    [ 0, 0, 1, 1 ],
    [ 0, 1, 1, 1 ],
    [ 0, 2, 1, 1 ],
    [ 0, 2, 1, 2 ],
    [ 0, 5, 2, 3 ],
    [ 0, 6, 2, 3 ],
    [ 0, 7, 2, 3 ],
    [ 0, 7, 0, 7 ],
    [ 1, 6, 0, 3 ],
    [ 1, 6, 0, 4 ],
    [ 2, 1, 0, 3 ],

    [ 10, 1, 7, 0 ],
    [ 10, 4, 7, 6 ],
    [ 10, 4, 6, 5 ],
    [ 10, 4, 6, 4 ],
]



def create_node(x,y,z,listr):
    bpy.ops.mesh.primitive_cylinder_add(
        radius = R, 
        depth = D,
        location = (x, y, z_offset)   
    )
    node = bpy.context.object
    node.keyframe_insert( data_path="location", frame=1 )

    start_frame = 130.0 - ( z - z_offset ) * 80.0 / 1.8
    node.keyframe_insert( data_path="location", frame=start_frame )

    node.location[2] = z
    node.keyframe_insert( data_path="location", frame=130 )

    listr.append( node )
    return node

def cylinder_between(x1, y1, z1, x2, y2, z2, r, listr):

  dx = x2 - x1
  dy = y2 - y1
  dz = z2 - z1    
  dist = math.sqrt(dx**2 + dy**2 + dz**2)

  bpy.ops.mesh.primitive_cylinder_add(
      radius = r, 
      depth = dist,
      location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)   
  ) 

  phi = math.atan2(dy, dx) 
  theta = math.acos(dz/dist) 

  bpy.context.object.rotation_euler[1] = theta 
  bpy.context.object.rotation_euler[2] = phi 
  listr.append( bpy.context.object )
  return bpy.context.object

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


def set_materials():
    node_mat = bpy.data.materials.get("GreenNode")
    if node_mat is None:
        node_mat = bpy.data.materials.new(name="GreenNode")

    for node in green_nodes:
        if node.data.materials:
            node.data.materials[0] = node_mat
        else:
            node.data.materials.append( node_mat )

    node_mat = bpy.data.materials.get("BlueNode")
    if node_mat is None:
        node_mat = bpy.data.materials.new(name="BlueNode")

    for node in blue_nodes:
        if node.data.materials:
            node.data.materials[0] = node_mat
        else:
            node.data.materials.append( node_mat )

    edge_mat = bpy.data.materials.get("HBondEdge")
    if edge_mat is None:
        edge_mat = bpy.data.materials.new(name="HBondEdge")

    for edge in hbond_edges:
        if edge.data.materials:
            edge.data.materials[0] = edge_mat
        else:
            edge.data.materials.append( edge_mat )

    edge_mat = bpy.data.materials.get("ClashEdge")
    if edge_mat is None:
        edge_mat = bpy.data.materials.new(name="ClashEdge")

    for edge in clash_edges:
        if edge.data.materials:
            edge.data.materials[0] = edge_mat
        else:
            edge.data.materials.append( edge_mat )



bpy.ops.group.create( name="first_nodes" )
bpy.ops.group.create( name="extra_nodes" )
bpy.ops.group.create( name="hbond_edges" )
bpy.ops.group.create( name="clash_edges" )


for xy in green_coords:
    for z in range( 0, xy[2] ):
        n = create_node( xy[0], xy[1], z_offset + ( z_gap * z ), green_nodes )
        if ( z == 0 ) :
            to_group("first_nodes", n)
        else :
            to_group("extra_nodes", n)
            


for xy in blue_coords:
    for z in range( 0, xy[2] ):
        n = create_node( xy[0], xy[1], z_offset + ( z_gap * z ), blue_nodes )
        if ( z == 0 ) :
            to_group("first_nodes", n)
        else :
            to_group("extra_nodes", n)


for edge in g2b_hbond_edge_coords:
    xy1 = green_coords[ edge[0] ]
    xy2 = blue_coords[ edge[2] ]
    x1 = xy1[0]
    y1 = xy1[1]
    z1 = z_offset + ( z_gap * edge[1] )
    x2 = xy2[0]
    y2 = xy2[1]
    z2 = z_offset + ( z_gap * edge[3] )
    e = cylinder_between( x1, y1, z1, x2, y2, z2, R/10, hbond_edges )
    to_group("hbond_edges", e)
    #e.group_link( "hbond_edges" )

for edge in g2g_hbond_edge_coords:
    xy1 = green_coords[ edge[0] ]
    xy2 = green_coords[ edge[2] ]
    x1 = xy1[0]
    y1 = xy1[1]
    z1 = z_offset + ( z_gap * edge[1] )
    x2 = xy2[0]
    y2 = xy2[1]
    z2 = z_offset + ( z_gap * edge[3] )
    e = cylinder_between( x1, y1, z1, x2, y2, z2, R/10, hbond_edges )
    to_group("hbond_edges", e)

for edge in b2b_hbond_edge_coords:
    xy1 = blue_coords[ edge[0] ]
    xy2 = blue_coords[ edge[2] ]
    x1 = xy1[0]
    y1 = xy1[1]
    z1 = z_offset + ( z_gap * edge[1] )
    x2 = xy2[0]
    y2 = xy2[1]
    z2 = z_offset + ( z_gap * edge[3] )
    e = cylinder_between( x1, y1, z1, x2, y2, z2, R/10, hbond_edges )
    to_group("hbond_edges", e)


'''
for edge in g2b_clash_edge_coords:
    xy1 = green_coords[ edge[0] ]
    xy2 = blue_coords[ edge[2] ]
    x1 = xy1[0]
    y1 = xy1[1]
    z1 = z_offset + ( z_gap * edge[1] )
    x2 = xy2[0]
    y2 = xy2[1]
    z2 = z_offset + ( z_gap * edge[3] )
    e = cylinder_between( x1, y1, z1, x2, y2, z2, R/10, clash_edges )
    to_group("clash_edges", e)
'''
set_materials()
