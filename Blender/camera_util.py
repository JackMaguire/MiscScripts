import bpy
import math

def get_active_camera():
    return bpy.context.scene.camera


#Inclusive:
def rotate_camera_around_point_XY( x, y, z, r, first_frame, last_frame, pos_offset ):
    camera = get_active_camera()
    num_frames = last_frame - first_frame + 1
    for x in range( first_frame, last_frame + 1 ):
        if( x == last_frame + 1 ):
            break#I always forget if range is inclusive

        pos = x + pos_offset
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
        camera.keyframe_insert( data_path="location", frame=x )

        camera.rotation_euler[ 0 ] = 90
        camera.rotation_euler[ 1 ] = 0
        camera.rotation_euler[ 2 ] = 360.0 * percent
        camera.keyframe_insert( data_path="rotation_euler", frame=x )
