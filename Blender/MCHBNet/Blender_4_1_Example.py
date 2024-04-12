import bpy
import math

class Settings:
    def __init__( self ):
        self.R = 0.1
        self.D = 0.1 #cylindar depth
        #self.scale = 2 * self.R

        self.z0 = self.D / 2
        self.z_gap = 2 * self.D

class Data:
    def __init__( self ):
        self.green_nodes = []
        self.blue_nodes = []
        self.hbond_edges = []
        self.clash_edges = []

        self.green_coords = [  # 11
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

        self.blue_coords = [  # 8
            [-2.4, -0.9, 8],
            [-1.5, -0.8, 10],
            [-0.8, -0.7, 11],
            [-1.8, 0.9, 9],
            [-1.5, 1.7, 10],
            [-1.0, 2.3, 10],
            [-0.4, 2.7, 9],
            [0.05, 3.2, 10],
        ]

def create_node(x, y, z, S, use_spheres=False):
    if use_spheres:
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=S.R,
            location=(x, y, S.z0)
        )
    else:
        bpy.ops.mesh.primitive_cylinder_add(
            radius=S.R,
            depth=S.D,
            location=(x, y, S.z0),
            scale=(1, 1, 1)
        )
    node = bpy.context.object
    bpy.context.collection.objects.unlink(bpy.context.object)  # Unlink from current collection

    node.keyframe_insert(data_path="location", frame=1)

    start_frame = 130.0 - (z - S.z0) * 80.0 / 1.8
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

def main():
    S = Settings()
    D = Data()

    for xy in D.green_coords:
        for z in range(xy[2]):
            n = create_node(xy[0], xy[1], S.z0 + (S.z_gap * z), S, use_spheres=False)
            collection_name = "first_nodes" if z == 0 else "extra_nodes"
            to_collection(collection_name, n)
            D.green_nodes.append( n )

    for xy in D.blue_coords:
        for z in range(xy[2]):
            n = create_node(xy[0], xy[1], S.z0 + (S.z_gap * z), S, use_spheres=False)
            collection_name = "first_nodes" if z == 0 else "extra_nodes"
            to_collection(collection_name, n)
            D.blue_nodes.append( n )

    #This is just and example edge between dummy points:
    n = cylinder_between( -1.17, -0.18, 0.1, -1.5, -0.8, 0.2, 0.005 )
    D.hbond_edges.append( n )
    to_collection("edges", n)

    set_materials(D)

if __name__ == '__main__':
    main()
