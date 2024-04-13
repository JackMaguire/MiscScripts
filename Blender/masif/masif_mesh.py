import bpy
import math
import bmesh
import numpy as np

class Settings:
    def __init__( self ):
        self.vertexR = 0.1
        self.edgeR = 0.001

def create_node(x, y, z, S):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=S.vertexR,
        location=(x, y, z)
    )

    node = bpy.context.object
    bpy.context.collection.objects.unlink(bpy.context.object)  # Unlink from current collection

    return node

    node.keyframe_insert(data_path="location", frame=1)

    start_frame = 130.0 - z * 80.0 / 1.8
    node.keyframe_insert(data_path="location", frame=start_frame)

    node.location.z = z
    node.keyframe_insert(data_path="location", frame=130)

    return node

def cylinder_between(x1, y1, z1, x2, y2, z2, r):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    dist = math.sqrt(dx**2 + dy**2 + dz**2)

    bpy.ops.mesh.primitive_cylinder_add(
        radius=r,
        depth=dist,
        location=(x1 + dx / 2, y1 + dy / 2, z1 + dz / 2),
        scale=(1, 1, 1)
    )

    phi = math.atan2(dy, dx)
    theta = math.acos(dz / dist) if dist != 0 else 0

    obj = bpy.context.object
    obj.rotation_euler[1] = theta
    obj.rotation_euler[2] = phi
    return obj

def to_collection(named, obj):
    coll = bpy.data.collections.get(named)
    if not coll:
        coll = bpy.data.collections.new(name=named)
        bpy.context.scene.collection.children.link(coll)
    coll.objects.link(obj)

def set_materials(D):
    gmat = bpy.data.materials.get("GreenNodeMaterial")
    if gmat is None:
        gmat = bpy.data.materials.new(name="GreenNodeMaterial")

    bmat = bpy.data.materials.get("BlueNodeMaterial")
    if bmat is None:
        bmat = bpy.data.materials.new(name="BlueNodeMaterial")

    emat = bpy.data.materials.get("EdgeMaterial")
    if emat is None:
        emat = bpy.data.materials.new(name="EdgeMaterial")

    def setter( obj_list, mat ):
       for obj in obj_list:
            if obj.data.materials:
                obj.data.materials[0] = mat
            else:
                obj.data.materials.append(mat)

    setter( D.green_nodes, gmat )
    setter(  D.blue_nodes, bmat )
    setter( D.hbond_edges, emat )

def get_active_camera():
    # Function to get the currently active camera in the scene
    return bpy.context.scene.camera

def rotate_camera_around_point_XY(x, y, z, r, first_frame, last_frame,
                                  pos_offset=0, x_tilt=0):
    camera = get_active_camera()
    num_frames = last_frame - first_frame + 1

    for i in range(first_frame, last_frame + 1):
        # Calculate the current position in the animation loop
        pos = (i + pos_offset) % num_frames

        # Calculate the percentage of the loop completed
        fraction = pos / num_frames
        radians = 2 * math.pi * fraction

        # Calculate new X and Y positions based on radius and angle
        pos_x = x + r * math.cos(radians)
        pos_y = y + r * math.sin(radians)

        # Update camera location
        camera.location = (pos_x, pos_y, z)
        camera.keyframe_insert(data_path="location", frame=i)

        # Update camera rotation
        # Assuming the rotation around z-axis to keep the camera oriented towards the center
        camera.rotation_euler = (
            math.pi/2 + x_tilt,
            0,
            math.pi * ( 0.5 + ( 2.0 * fraction ) )
        )
        camera.keyframe_insert(data_path="rotation_euler", frame=i)

def create_face_for_3_objects( objs ):
    assert len(objs) == 3, len(objs)

    # Step 1: Creating the Triangle Mesh

    # Create a new mesh and a new object
    mesh = bpy.data.meshes.new('TriangleMesh')
    obj = bpy.data.objects.new('Triangle', mesh)

    # Link the object to the scene
    scene = bpy.context.scene
    collection = bpy.context.collection
    collection.objects.link(obj)

    # Use bmesh to create the triangle geometry
    bm = bmesh.new()
    v1 = bm.verts.new(objs[0].location)
    v2 = bm.verts.new(objs[1].location)
    v3 = bm.verts.new(objs[2].location)
    bm.faces.new((v1, v2, v3))
    bm.to_mesh(mesh)
    bm.free()

    # Step 2: Attaching Vertices to Other Meshes
    def _hook_vertex_to_object(obj, vertex_index, target_object):
        # Ensure we're in object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Select the object and make it the active object
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        # Deselect all vertices
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')

        # Switch to vertex select mode
        bpy.ops.object.mode_set(mode='VERTEX_PAINT')

        # Select the specific vertex
        obj.data.vertices[vertex_index].select = True

        # Add a hook to the selected vertex
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.hook_add_newob()

        # Get the last hook modifier (which is the one we just added)
        hook_modifier = obj.modifiers[-1]

        # Set the hook object to the target object
        hook_modifier.object = target_object

        # Clear selection and return to object mode
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')

    for i,v in enumerate( objs ):
        _hook_vertex_to_object(obj, i, v)

    return obj

def build_static_mesh( vertices, F, S: Settings, name: str ):
    # Nodes
    nodes = []
    collection_name = name+"_nodes"
    for v in vertices:
        n = create_node(v[0], v[1], v[2], S)
        to_collection(collection_name, n)
        nodes.append( v )

    # Edges
    edges = []
    collection_name = name+"_edges"
    edge_indices = set(
        [(i[0],i[1]) for i in F] +
        [(i[0],i[2]) for i in F] +
        [(i[1],i[2]) for i in F] )
    for (i,j) in edge_indices:
        xyz_i = vertices[i]
        xyz_j = vertices[j]
        n = cylinder_between( xyz_i[0], xyz_i[1], xyz_i[2], xyz_j[0], xyz_j[1], xyz_j[2], S.edgeR )
        edges.append( n )
        to_collection(collection_name, n)

    # faces
    faces = []
    collection_name = name+"_faces"
    for f in F:
        objs = [nodes[i] for i in f]
        n = create_face_for_3_objects( objs )
        faces.append( n )
        to_collection(collection_name, n)
        

def main():
    S = Settings()

    data = np.load( "/Users/jbm13835/temps/24_04APR/dummy6/0.rawmesh.npz" )
    build_static_mesh(
        vertices = data["meshV"],
        F        = data["meshF"],
        S    = S,
        name = "0" )

    return

    set_materials(D)

    rotate_camera_around_point_XY(
        x=D.mean_x(),
        y=D.mean_y(),
        z=1,
        r=10,
        first_frame=50,
        last_frame=250,
        pos_offset=0 )


if __name__ == '__main__':
    main()
