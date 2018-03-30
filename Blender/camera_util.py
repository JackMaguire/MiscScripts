import bpy
import math

def get_active_camera():
    return bpy.context.scene.camera


#Inclusive:
def rotate_camera_around_point_XY( x, y, z, r, first_frame, last_frame, pos_offset ):
    camera = get_active_camera()
    num_frames = last_frame - first_frame + 1
    for i in range( first_frame, last_frame + 1 ):
        if( i == last_frame + 1 ):
            break#I always forget if range is inclusive

        pos = i + pos_offset
        if( pos > last_frame ):
            pos -= num_frames
        pos -= first_frame

        percent = float( pos ) / num_frames
        radians = 2 * math.pi * percent
        sin = math.sin( radians )
        cos = math.cos( radians )

        pos_x = x + ( r * cos )
        pos_y = y + ( r * sin )

        camera.location[ 0 ] = pos_x
        camera.location[ 1 ] = pos_y
        camera.location[ 2 ] = z
        camera.keyframe_insert( data_path="location", frame=i )

        #need to use radians here
        camera.rotation_euler[ 0 ] = math.pi / 2.0
        camera.rotation_euler[ 1 ] = 0.0
        camera.rotation_euler[ 2 ] = 2.0 * math.pi * percent
        camera.keyframe_insert( data_path="rotation_euler", frame=i )
