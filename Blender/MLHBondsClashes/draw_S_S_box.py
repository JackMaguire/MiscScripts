import bpy
import math
import numpy
import re
import platform

# Global data #
all_boxes = []

box_hist = []
for x in range( 0, 10 ):
    box_hist.append( [] )



def my_assert_equals( name, actual, theoretical ):
    if actual != theoretical:
        print( str( name ) + " is equal to " + str( actual ) + " instead of " + str( theoretical ) )
        exit( 1 )


# 2*pi 
#N_SLOTS_X = 71
#SLOT_WIDTH_X = 0.1 #angle1
#SLOT_WIDTH_Y = 0.1 #angle2
#SLOT_WIDTH_Z = 0.5 #dist

BOX_X = 0.1
BOX_Y = 0.1
BOX_Z = 0.1

def angle1_to_x( angle1 ):
    return math.floor( angle1 * 10 ) / 10

def angle2_to_y( angle2 ):
    return angle1_to_x( angle2 )
    #return math.floor( angle2 * 10 ) / 10

def dist_to_z( dist ):
    return math.floor( dist * 5 ) / 10

my_assert_equals( "angle1_to_x( 0 )",     angle1_to_x( 0 ),      0   )
my_assert_equals( "angle1_to_x( -0.11 )", angle1_to_x( -0.11 ), -0.2 )
my_assert_equals( "angle1_to_x( -0.1 )",  angle1_to_x( -0.1 ),  -0.1 )
my_assert_equals( "angle1_to_x( -0.09 )", angle1_to_x( -0.09 ), -0.1 )
my_assert_equals( "angle1_to_x( 0.1 )",   angle1_to_x( 0.1 ),    0.1 )
my_assert_equals( "angle1_to_x( 0.099 )", angle1_to_x( 0.099 ),  0   )
my_assert_equals( "angle1_to_x( 0.99 )",  angle1_to_x( 0.99 ),   0.9 )
my_assert_equals( "angle1_to_x( 1.00 )",  angle1_to_x( 1.00 ),   1.0 )

#####################
# BLENDER FUNCTIONS #
#####################

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


def create_cube( angle1, angle2, dist, box_list ):
    bpy.ops.mesh.primitive_cube_add(
        radius = 0.03,
        location = ( angle1_to_x( angle1 ), angle2_to_y( angle2 ), dist_to_z( dist ) )   
    )
    node = bpy.context.object
    #node.keyframe_insert( data_path="location", frame=1 )

    #start_frame = 130.0 - ( z - z_offset ) * 80.0 / 1.8
    #node.keyframe_insert( data_path="location", frame=start_frame )

    #node.location[2] = z
    #node.keyframe_insert( data_path="location", frame=130 )

    all_boxes.append( node )
    box_list.append( node )
    return node

def color_material( material, scale_from_0_to_1 ):
    b = 0
    if scale_from_0_to_1 < 0.5:        #first, green stays at 100%, red raises to 100%
        g = 1.0
        r = 2 * scale_from_0_to_1
    else:
        r = 1.0
        g = 1.0 - 2 * (scale_from_0_to_1-0.5)
    #r = 1.0 - scale_from_0_to_1
    #g = r
    #b = r
    material.diffuse_color = ( r, g, b )

#######################
# Customization Funcs #
#######################

def clash_skip( score, angle1, angle2, dist ):
    #TODO make this more complicated
    return score == 0

#13 columns
#best_possible_hbond_score,worst_possible_clash_score,tx,ty,tz,rz,ry,rz,pair,cenpack,angle1,angle2,dist

BEST_POSSIBLE_HBOND_SCORE  = int( 0 )
WORST_POSSIBLE_CLASH_SCORE = int( 1 )

TX = int( 2 )
TY = int( 3 )
TZ = int( 4 )

RX = int( 5 )
RY = int( 6 )
RZ = int( 7 )

PAIR    = int( 8 )
CENPACK = int( 9 )

ANGLE1 = int( 10 )
ANGLE2 = int( 11 )
DIST   = int( 12 )

custom_input_file=""
#custom_input_file="/Volumes/My Book/tensorflow_hbonds_and_clashes/E_W/first_2000.txt"
if( len(custom_input_file) > 0 ):
    dataset = numpy.genfromtxt( custom_input_file, delimiter=",", skip_header=1 )
elif( platform.platform().startswith( "Linux" ) ):
    dataset = numpy.genfromtxt( "/home/jack/HBondMachineLearning/sample_data.csv", delimiter=",", skip_header=1 )
else:
    dataset = numpy.genfromtxt( "/Users/jack/HBondMachineLearning/sample_data.csv", delimiter=",", skip_header=1 )

input = dataset[:,[ TX, TY, TZ, RX, RY, RZ, ANGLE1, ANGLE2, DIST ] ]
input_3D = dataset[:, [ ANGLE1, ANGLE2, DIST ] ]

both_output = dataset[:,0:2]
output_hbond = dataset[:,[ BEST_POSSIBLE_HBOND_SCORE  ] ]
output_clash = dataset[:,[ WORST_POSSIBLE_CLASH_SCORE ] ]

num_elements = len( dataset )

# Create Clash Boxes
for i in range( 0, num_elements ):
    score = output_clash[ i ]
    angle1 = input_3D[ i ][ 0 ]
    angle2 = input_3D[ i ][ 1 ]
    dist   = input_3D[ i ][ 2 ]

    if( clash_skip( score, angle1, angle2, dist ) ):
        continue

    box_hist_val = math.floor( score * 10 )
    if box_hist_val > 9 :
        box_hist_val = 9
    print( "box_hist_val: " + str( box_hist_val ) + " score: " + str( score ) )

    new_mesh = create_cube( angle1, angle2, dist, box_hist[ box_hist_val ] )


for i in range( 0, len( box_hist ) ):
    if( len( box_hist[i] ) == 0 ):
        continue

    material_name = str( i )
    group_name = "group_" + str( i )

    group = bpy.ops.group.create( name=group_name )

    node_mat = bpy.data.materials.get( material_name )
    if node_mat is None:
        node_mat = bpy.data.materials.new( name=material_name )
        frac = float( i ) / ( len( box_hist ) - 1 )
        color_material( node_mat, frac )

    for node in box_hist[ i ]:
        if node.data.materials:
            node.data.materials[ 0 ] = node_mat
        else:
            node.data.materials.append( node_mat )

        to_group( group_name, node )
