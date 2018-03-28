#import bpy
import math
import numpy
#import re

def my_assert_equals( name, actual, theoretical ):
    if actual != theoretical:
        print( name + " is equal to " + actual + " instead of " + theoretical )
        exit( 1 )


# 2*pi 
#N_SLOTS_X = 71
SLOT_WIDTH_X = 0.1 #angle1
SLOT_WIDTH_Y = 0.1 #angle2
SLOT_WIDTH_Z = 0.5 #dist

def angle1_to_x( angle1 ):
    return math.floor( angle*10 ) / 10;

my_assert_equals( "angle1_to_x( 0 )", angle1_to_x( 0 ), 0 )
my_assert_equals( "angle1_to_x( -0.1 )", angle1_to_x( -0.1 ), -1 )
my_assert_equals( "angle1_to_x( 0.1 )", angle1_to_x( 0.1 ), 0 )
my_assert_equals( "angle1_to_x( 0.99 )", angle1_to_x( 0.99 ), 0 )
my_assert_equals( "angle1_to_x( 1.00 )", angle1_to_x( 1.00 ), 1 )
exit( 0 )

def create_cube( x, y, z, listr ):
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

dataset = numpy.genfromtxt( "sample_data.csv", delimiter=",", skip_header=1 )
#print( len( dataset[ 0 ] ) )

input = dataset[:,[ TX, TY, TZ, RX, RY, RZ, ANGLE1, ANGLE2, DIST ] ]
input_3D = dataset[:, [ ANGLE1, ANGLE2, DIST ] ]

both_output = dataset[:,0:2]
output_hbond = dataset[:,[ BEST_POSSIBLE_HBOND_SCORE  ] ]
output_clash = dataset[:,[ WORST_POSSIBLE_CLASH_SCORE ] ]

