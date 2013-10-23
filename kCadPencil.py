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

class kCadPencilOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Tool Name"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "Add CAD object"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)
    #bpy.utils.register_class(kCadPencilOperator) 
    
def unregister():
    #bpy.utils.unregister_class(kCadPencilOperator) 
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
