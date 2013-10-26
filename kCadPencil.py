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
    "category": "Add Mesh"}


import bpy

index=0
def draw_callback_px(self, context):
    global index
    ob = context.object
    print('WOW COOL:',index)
    index+=1


class kCadPencilOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "Add CAD object"

    x = bpy.props.IntProperty()
    y = bpy.props.IntProperty()    

    def modal(self, context, event):
        context.area.tag_redraw()
        if event.type in {'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def execute(self, context):
        print("Hello World")
        self.report({'INFO'}, "Mouse coords are %d %d" % (self.x, self.y))
        return {'FINISHED'}

    def invoke(self, context, event):
#        self.x = event.mouse_x
#        self.y = event.mouse_y
#        return self.execute(context)
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_VIEW')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}
def register():
    bpy.utils.register_class(kCadPencilOperator) 
    #bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_class(kCadPencilOperator) 
    #bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
