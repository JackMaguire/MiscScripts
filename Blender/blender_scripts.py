import bpy, bmesh

def square_box (x, y, z, d):
    r = d/2
    return bpy.ops.mesh.primitive_cube_add( location=(x+r,y+r,z+r), radius=r)

