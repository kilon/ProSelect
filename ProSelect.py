import bpy, bgl, blf, os, importlib, time

bl_info={
"name": "ProSelect",
"description": "Select vertices that are connected through a specific number of edges",
"author": "Kilon ",
"version": (1, 0, 0, 0),
"blender": (2, 77, 0),
"location": "View3D",
"wiki_url": "http://www.kilon-alios.com",
"category": "Object"}

class ProSelectPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "ProSelect"
    bl_idname = "ProSelect_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "ProSelect"
    #bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout

        scene = context.scene


        col = layout.column(align=True)

        row = col.row(align=True)
        row.operator("view3d.pro_select")
        row = col.row(align=True)

        row.prop(scene,"number_of_verts")
  


class ProSelectOperator(bpy.types.Operator):
    bl_idname = "view3d.pro_select"
    bl_label = "ProSelect"


    def execute(self, context):
        svert_index = 0
        ob = bpy.context.active_object
        oldmode = ob.mode
        if oldmode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT') 
        num_of_edges= context.scene.number_of_verts
        trvert = []
        for vert in ob.data.vertices:
            count_edges=0
            for x in range(0,len(ob.data.edges)):
                for verte in ob.data.edges[x].vertices:
                    if verte == vert.index:
                        count_edges = count_edges +1
            if count_edges == num_of_edges:
                trvert.append(vert)
                vert.select = True
        if oldmode != 'OBJECT':
            bpy.ops.object.mode_set(mode=oldmode) 
        return {'FINISHED'}



def register():
    bpy.utils.register_class(ProSelectOperator)
    bpy.utils.register_class(ProSelectPanel)
    

    bpy.types.Scene.number_of_verts = bpy.props.IntProperty(default=3,soft_min=0,soft_max=100,name="Number of Vertices",description="Number of Vertices connected with edges")

def unregister():

    bpy.utils.unregister_class(ProSelectOperator)
    bpy.utils.unregister_class(ProSelectPanel)
    del bpy.types.Scene.number_of_verts





                
    
