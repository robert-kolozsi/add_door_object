# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

# Date created: Apr 23, 2012
# Last edited: Jun 21, 2012
# Version: 0.1
# file: __init__.py


# TODO: If in edit mode this should not work! But still works.
 #      date: Apr 24, 2012.

bl_info = {
    'name': 'Architectural Door System',
    'author': 'Kolozsi Róbert (krobi)',
    'version': (0, 1),
    'blender': (2, 6, 6),
    'location': 'View3D > Add > Mesh',
    'description': 'Create architectural parametric door objects in the scene.',
    'warning': 'Under heavy development!',
    'category': 'Add Mesh'
}

# To support modules reload with KEYF8 (DEBUGING)
# Currently not working. Blender crashes. Apr 18, 2013
if "bpy" in locals():
    import imp
    imp.reload(add_door)
    print("Module for door reloaded!")
else:
    import bpy
    from add_door_object import add_door
    print("Module for door imported!")


# Define the 'Add Door' menu
class INFO_MT_mesh_door_add(bpy.types.Menu):
    bl_idname = 'INFO_MT_mesh_door_add'
    bl_label = "Add Doors"

    #@classmethod
    #def poll(cls, context):
    #    return (context.object is not None)

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator('mesh.primitive_door_add', text='Doors')


# Define the 'Door & Window System' panel on tools shelf.
class VIEW3D_PT_AddDoorButton_objectmode(bpy.types.Panel):
    """Class for adding button on Tools shelf for door frame.
    """
    bl_idname = 'OBJECT_PT_door_add'
    bl_label = "Doors"
    bl_space_type = 'VIEW_3D'  # 'PROPERTIES' # 'VIEW_3D'
    bl_region_type = 'TOOLS'  # 'WINDOW' # 'TOOLS'
    bl_context = 'objectmode'  # 'object' # 'scene'
    #bl_options = { 'DEFAULT_CLOSED' }
    bl_default_closed = False

    #@classmethod
    #def poll(cls, context):
    #    return context.active_object is not None

    #def draw_header(self, context):
    #   pass

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        row = col.row()
        row.operator('mesh.primitive_door_add', text='Add Door')


def menu_function(self, context):
    # This will be interested when I build the door stuff too..
    #self.layout.menu("INFO_MT_mesh_window_add", icon="PLUGIN")

    # Is fine as well, this will just create a single entry
    self.layout.menu('INFO_MT_mesh_door_window_add',
                     text="Doors & Windows",
                     icon='PLUGIN')
    #self.layout.operator("mesh.primitive_window_frame_add", icon="PLUGIN")
    #self.layout.operator("mesh.primitive_door_frame_add", icon="PLUGIN")

#def panel_function(self, context):
    #self.layout.panel('OBJECT_PT_door_window_add', text="Doors & Windows")


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(menu_function)
    #bpy.types.OBJECT_PT_door_window_add.append(panel_function)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_mesh_add.remove(menu_function)


def main():
    register()


if __name__ == '__main__':
    main()
