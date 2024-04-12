import bpy
import math

R = 0.1
D = 0.1
scale = 2 * R

z_offset = D / 2
z_gap = 2 * D

green_nodes = []
blue_nodes = []
hbond_edges = []
clash_edges = []

green_coords = [  # 11
    [-1.17, -0.18, 13],
    [-1.8, -0.28, 11],
    [-2.5, -0.08, 10],
    [-3.1, -0.4, 10],
    [-2.9, 0.2, 11],
    [-2.5, 0.5, 7],
    [-1.7, 0.4, 12],
    [-1.17, 0.75, 10],
    [-0.6, 1.17, 11],
    [-0.07, 1.6, 11],
    [0.5, 1.98, 10]
]

blue_coords = [  # 8
    [-2.4, -0.9, 8],
    [-1.5, -0.8, 10],
    [-0.8, -0.7, 11],
    [-1.8, 0.9, 9],
    [-1.5, 1.7, 10],
    [-1.0, 2.3, 10],
    [-0.4, 2.7, 9],
    [0.05, 3.2, 10],
]

def create_node(x, y, z, listr, use_spheres=False):
    if use_spheres:
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=R,
            location=(x, y, z_offset)
        )
    else:
        bpy.ops.mesh.primitive_cylinder_add(
            radius=R,
            depth=D,
            location=(x, y, z_offset),
            scale=(1, 1, 1)
        )
    node = bpy.context.object
    bpy.context.collection.objects.unlink(bpy.context.object)  # Unlink from current collection

    node.keyframe_insert(data_path="location", frame=1)

    start_frame = 130.0 - (z - z_offset) * 80.0 / 1.8
    node.keyframe_insert(data_path="location", frame=start_frame)

    node.location.z = z
    node.keyframe_insert(data_path="location", frame=130)

    listr.append(node)
    return node

def cylinder_between(x1, y1, z1, x2, y2, z2, r, listr):
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

    listr.append(obj)
    return obj

def to_collection(named, obj):
    coll = bpy.data.collections.get(named)
    if not coll:
        coll = bpy.data.collections.new(name=named)
        bpy.context.scene.collection.children.link(coll)
    coll.objects.link(obj)

def set_materials():
    gmat = bpy.data.materials.get("GreenNodeMaterial")
    if gmat is None:
        gmat = bpy.data.materials.new(name="GreenNodeMaterial")

    bmat = bpy.data.materials.get("BlueNodeMaterial")
    if bmat is None:
        bmat = bpy.data.materials.new(name="BlueNodeMaterial")

    emat = bpy.data.materials.get("EdgeMaterial")
    if emat is None:
        emat = bpy.data.materials.new(name="EdgeMaterial")

    #for obj_list in [green_nodes, blue_nodes, hbond_edges, clash_edges]:
    def setter( obj_list, mat ):
       for obj in obj_list:
            if obj.data.materials:
                obj.data.materials[0] = mat
            else:
                obj.data.materials.append(mat)
    setter( green_nodes, gmat )
    setter(  blue_nodes, bmat )
    setter( hbond_edges, emat )

for xy in green_coords:
    for z in range(xy[2]):
        n = create_node(xy[0], xy[1], z_offset + (z_gap * z), green_nodes)
        collection_name = "first_nodes" if z == 0 else "extra_nodes"
        to_collection(collection_name, n)

for xy in blue_coords:
    for z in range(xy[2]):
        n = create_node(xy[0], xy[1], z_offset + (z_gap * z), blue_nodes)
        collection_name = "first_nodes" if z == 0 else "extra_nodes"
        to_collection(collection_name, n)
  
#This is just and example edge between dummy points:
n = cylinder_between( -1.17, -0.18, 0.1, -1.5, -0.8, 0.2, 0.005, hbond_edges )
to_collection("edges", n)

set_materials()
