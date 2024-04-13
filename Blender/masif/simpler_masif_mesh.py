import bpy
import math
import bmesh
import numpy as np

class Settings:
    def __init__(self):
        self.vertexR = 0.1  # Adjust as necessary for visual appeal

def create_material():
    # Create a single material with a shader that uses vertex attributes for coloring
    mat = bpy.data.materials.new(name="DynamicVertexColor")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    bsdf = nodes.get('Principled BSDF')
    attr = nodes.new('ShaderNodeAttribute')
    attr.attribute_name = 'charge'
    color_ramp = nodes.new('ShaderNodeValToRGB')
    color_ramp.color_ramp.elements.new(0.5)
    color_ramp.color_ramp.elements[0].position = 0.0
    color_ramp.color_ramp.elements[0].color = (1, 0, 0, 1)  # Red at 0
    color_ramp.color_ramp.elements[1].position = 0.5
    color_ramp.color_ramp.elements[1].color = (1, 1, 1, 1)  # White at 0.5
    color_ramp.color_ramp.elements[2].position = 1.0
    color_ramp.color_ramp.elements[2].color = (0, 0, 1, 1)  # Blue at 1

    links.new(attr.outputs['Fac'], color_ramp.inputs['Fac'])
    links.new(color_ramp.outputs['Color'], bsdf.inputs['Base Color'])
    
    return mat

def create_mesh_object(vertices, faces, vertex_charges, settings):
    # Create mesh and object
    mesh = bpy.data.meshes.new("DynamicMesh")
    obj = bpy.data.objects.new("DynamicObject", mesh)
    bpy.context.collection.objects.link(obj)
    
    # Create mesh from given vertices and faces
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    
    # Assign material
    mat = create_material()
    if not obj.data.materials:
        obj.data.materials.append(mat)
    
    # Add vertex charge as an attribute
    mesh.attributes.new(name='charge', type='FLOAT', domain='POINT')
    charge_data = mesh.attributes['charge'].data
    for i, charge in enumerate(vertex_charges):
        charge_data[i].value = 0.5 + charge/20.0

    return obj

def main():
    # Example data
    vertices = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (0, 0, -1.5)]  # Example vertices
    faces = [(0, 1, 2, 3), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)]  # Example faces
    vertex_charges = [0.0, 5.0, -3.0, 10.0, -7.0]  # Example charges

    settings = Settings()

    # Load actual data here
    data = np.load( "/tmp/24_04APR/dummy6/0.rawmesh.npz" )
    vertices = data["meshV"]
    faces = data["meshF"]
    vertex_charges = data["vertex_charges"]

    obj = create_mesh_object(vertices, faces, vertex_charges, settings)

if __name__ == '__main__':
    main()
