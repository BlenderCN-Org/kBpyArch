# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Cad modeling pencil",
    "author": "Karakal_13",
    "version": (0,1,2),
    "blender": (2, 61, 0),
    "location": "View3D > Add > Mesh",
    "description": "add cad models",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php",
    "tracker_url": "https://projects.blender.org",
    "category": "Object"}


import bpy
import bgl 

def mouse2space(view, x, y):
  if view.type != 'VIEW_3D':
    print("Error: not 3d view")
    return None
  
  bgl.glGetFloat(GL_PROJECTION_MATRIX, projection);
  bgl.glGetFloat(GL_MODELVIEW_MATRIX, modelview);
  bgl.glGetInteger(GL_VIEWPORT, viewport);
  
  winX = x; 
  winY = viewport[3] - y; 
  print ('VP x,y',winX,winY)
  

class kCadPencilOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "Add CAD object"

    def __init__(self):
      self.primitive = None
      self.x = bpy.props.IntProperty()
      self.y = bpy.props.IntProperty()


#    def modal(self, context, event):
#        context.area.tag_redraw()
#        if event.type in {'ESC'}:
#            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
#            return {'CANCELLED'}
#        return {'PASS_THROUGH'}
    def modal(self, context, event):
        #print('modal event:', str(event.type))
        if event.type == 'MOUSEMOVE':
            self.value = event.mouse_x
            self.execute(context)
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':  # Confirm
            self.x = event.mouse_x
            self.y = event.mouse_y
            if bpy.context.area.type == 'VIEW_3D':
              print("Mouse coords are %d %d %s" % (self.x, self.y,bpy.context.area.type))
              mouse2space(bpy.context.area, self.x, self.y)
            return {'RUNNING_MODAL'}
        elif event.type in ('RIGHTMOUSE', 'ESC'):  # Cancel
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def execute(self, context):
        pass

    def invoke(self, context, event):
        self.execute(context)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
      
class kCadPencilPolyline(kCadPencilOperator):
    bl_idname = "object.draw_polyline"
    bl_label = "kCad polyline"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "Add CAD polyline object"
    
    def __init__(self):
      self.primitive = 'line'
  
class kCadPanel(bpy.types.Panel):
    """A Custom Panel in the Viewport Toolbar"""
    bl_label = "kCad draw panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Add Objects:")

        split = layout.split()
        col = split.column(align=True)

        #col.operator("mesh.primitive_plane_add", text="PolyLine", icon='MESH_PLANE')
        col.operator("object.draw_polyline", text="PolyLine", icon='MESH_PLANE')

def register():
    bpy.utils.register_class(kCadPencilOperator) 
    bpy.utils.register_class(kCadPencilPolyline) 
    bpy.utils.register_class(kCadPanel)
    #bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_class(kCadPencilOperator) 
    bpy.utils.unregister_class(kCadPencilPolyline) 
    bpy.utils.unregister_class(kCadPanel)
    #bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
