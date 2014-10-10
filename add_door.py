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

# Date created: Apr 24, 2012
# Last edited: Apr 17, 2013
# Version: 0.1
# file: dr_frames_01.py


import bpy
from bpy.props import FloatProperty, EnumProperty, BoolProperty, IntProperty

import math

# To support modules reload in blender with KEYF8 (DEBUGGING)
if "la" and "hi" and "le" and "fr" and "th" in locals():
    import imp
    imp.reload(la)
    imp.reload(hi)
    imp.reload(le)
    imp.reload(fr)
    imp.reload(th)
    print("All door sub-modules are reloaded!")
else:
    from add_door_object.door_accessories import latches_types as la
    from add_door_object.door_accessories import hinges_types as hi
    from add_door_object.door_accessories import leaf_types as le
    from add_door_object.door_accessories import frame_types as fr
    from add_door_object.door_accessories import threshold_types as th
    print("All door sub-modules are imported!")


class Door(object):
    """Abstaraction of a door.
    The container of all other accessories.
    """
    def __init__(self,
                 door_type, frame_type,
                 width, height,
                 sect_width, sect_depth,
                 door_rot_angle):
        """Door is just a dummy container object,
        it contains only a setup for 'my_frame' object, and 'frame_py', the python mesh/object object.
        door_type   -> DOUBLE, SINGLE, GARAGE, INDUSTRIAL, GATE. <- (for future)
        """
        if frame_type == 'SIMPLE1':
            # This is my abstract object, not a blender python API object.
            self.my_door = Door_Frame(frame_type, width, height, sect_width, sect_depth)

        # This is a blender python API object. Contains a frame mesh.
        self.door_py = self.create_door(door_rot_angle)

        ## Create single door ##
        #if door_type == 'SINGLE':
        #    pass
        ### Create double door ##
        #elif door_type == 'DOUBLE':
        #    pass
        ### Create garage door ##
        #elif door_type == 'GARAGE':
        #    pass
        ### Create industrial door ##
        #elif door_type == 'INDUSTRIAL':
        #    pass
        ### Create gate door ##
        #elif door_type == 'GATE':
        #    pass
        #object.rotation_mode = 'XYZ'
        #degree_door = radians_door * (math.pi / 180)

    def __str__(self):
        return "Door Type: " + door_type + "\nFrame Type: " + frame_type

    def __del__(self):
        del self.my_door
        del self.door_py

        print("Deleted Door Object", end="\n")


    def create_door(self, door_rot_angle):
        # Creating a python frame mesh and object.
        frame_mesh = bpy.data.meshes.new('Door.Frame.Mesh')
        frame_object = bpy.data.objects.new('Door.Frame', frame_mesh)
        frame_object.location = bpy.context.scene.cursor_location

        scene = bpy.context.scene
        scene.objects.link(frame_object)

        # Creates the actual base frame python mesh.
        frame_mesh.from_pydata(self.my_door.my_frame.vertices, [], self.my_door.my_frame.polygons)
        frame_mesh.update(calc_edges=True)

        frame_object.select = True

        # The rotation logic is here!
        degree_door = door_rot_angle * (math.pi / 180)

        bpy.ops.transform.rotate(value=degree_door, # in eartly versions tuple: (degree_door, ),
                                 axis=(degree_door, 0, 0),
                                 constraint_axis=(False, False, True),
                                 constraint_orientation='GLOBAL',
                                 mirror=False,
                                 proportional='DISABLED')

        frame_object.select = False
        scene.objects.active = None

        return frame_object


class Door_Frame(object):
    """IMPORTANT NOTE: the constraint is that when placing a door in the scene,
    always think of it if you are inside of the room.
    """
    def __init__(self, frame_type, width, height, sect_width, sect_depth):
        """Frames are 'special' types. There are the bases.
        Always have to be recalculated if width, height and cross section changes.
        Anything can be excluded but frames. No doors without at least a frame.
        """
        if frame_type == 'SIMPLE1':
            self.my_frame = fr.Frame_Simple1(width, height, sect_width, sect_depth)

        elif frame_type == 'SIMPLE2':
            self.my_frame = fr.Frame_Simple2(width, height, sect_width, sect_depth)

    def __del__(self):
        # Not sure what is __del__ doing (in/to memory).
        del self.my_frame

        print("Deleted Door_Frame Object", end="\n")

    def __str__(self):
        return "Door Frame Type: " + frame_type


class Door_Leaf(object):
    """Leaf Class.
    """
    def __init__(self, leaf_type, door, leaf_depth, leaf_position, leaf_rot_angle, my_latch):
        """Leaf object depends on the frame object.
        So calculations of its dimensions is in relation to the frame object.
        """
        #self.rotation_deviation = 0.015

        if leaf_type == 'SIMPLE1':
            self.my_leaf = le.Leaf_Simple1(leaf_depth, door.my_door, leaf_position)

        elif leaf_type == 'SIMPLE2':
            self.my_leaf = le.Leaf_Simple2(leaf_depth, door.my_door, leaf_position)

        # This is a python blender object
        # WOW! NEW GOOD THING! Last parameter passing a class, itt works!!!
        self.leaf_py = self.create_leaf(door, leaf_position, leaf_rot_angle, self.my_leaf.__class__)

    def __del__(self):
        del self.my_leaf
        del self.leaf_py

        print("Deleted Leaf Object", end="\n")

    def __str__(self):
        return "Leaf Type: " + leaf_type

    def create_leaf(self, door, leaf_position, leaf_rot, class_type):
        leaf_mesh = bpy.data.meshes.new('Door.Leaf.Mesh')
        leaf_object = bpy.data.objects.new('Door.Leaf', leaf_mesh)

        scene = bpy.context.scene

        leaf_object.show_wire = True
        leaf_object.lock_rotation = (True, True, False)

        scene.objects.link(leaf_object)

        leaf_mesh.from_pydata(self.my_leaf.vertices, [], self.my_leaf.polygons)
        leaf_mesh.update(calc_edges=True)

        # Parenting a leaf to a door frame object.
        leaf_object.parent = door.door_py
        leaf_object.select = True

        # Positioning the leaf to apropriate place against frame.
        frame_light_width = door.my_door.my_frame.frame_width - 2 * door.my_door.my_frame.sect_width

        if leaf_position == 'LEFT':
            x = -frame_light_width / 2 - class_type.ROTATION_DEVIATION - 2 * class_type.TOOTH_DEPTH
            degree_leaf = leaf_rot * (math.pi / 180)

        elif leaf_position == 'RIGHT':
            x = frame_light_width / 2 + class_type.ROTATION_DEVIATION + 2 * class_type.TOOTH_DEPTH
            degree_leaf = -leaf_rot * (math.pi / 180)

        leaf_object.location.x = x
        leaf_object.location.y = -door.my_door.my_frame.sect_depth - class_type.ROTATION_DEVIATION

        # The rotation logic is here!
        bpy.ops.transform.rotate(value=-degree_leaf, # (-degree_leaf, ), changed API Nov 2, 2012
                                 axis=(0, 0, -degree_leaf),
                                 constraint_axis=(False, False, True),
                                 constraint_orientation='GLOBAL',
                                 mirror=False,
                                 proportional='DISABLED')

        leaf_object.select = False

        return leaf_object


class Door_Threshold(object):
    """Threshold objects.
    """
    def __init__(self, door, sect_width, sect_height):
        self.my_threshold = th.Threshold_Simple(door, sect_width, sect_height)

        self.threshold_py = self.create_threshold(door, self.my_threshold)


    def __del__(self):
        del self.my_threshold
        del self.threshold_py

        print("Deleted Threshold Object", end="\n")

    def create_threshold(self, door, my_threshold):
        threshold_mesh = bpy.data.meshes.new('Door.Threshold.Mesh')
        threshold_object = bpy.data.objects.new('Door.Threshold', threshold_mesh)

        scene = bpy.context.scene
        scene.objects.link(threshold_object)

        threshold_object.location = bpy.context.scene.cursor_location

        threshold_mesh.from_pydata(my_threshold.vertices, [], my_threshold.faces)
        threshold_mesh.update(calc_edges=True)

        # Parenting a leaf to a door frame object.
        threshold_object.parent = door.door_py

        threshold_object.show_wire = True

        return threshold_object


class Door_Latch(object):
    """Latch objects depeneds on existence of the leaf object.
    """
    def __init__(self, latch_type, my_door, leaf, vert_pos, mirror_flag, leaf_position):
        ### NOTE: probably to add horizontal position later!!! Jun 23, 2012.

        if latch_type == 'TYPE1':
            self.my_latch = la.Latch_Type1(leaf)

        elif latch_type == 'TYPE2':
            self.my_latch = la.Latch_Type2(leaf)

        elif latch_type == 'TYPE3':
            self.my_latch = la.Latch_Type3(leaf)

        elif latch_type == 'TYPE4':
            self.my_latch = la.Latch_Type4(leaf)

        elif latch_type == 'TYPE5':
            self.my_latch = la.Latch_Type5(leaf)

        # Creating the python stuff!
        self.latch_py = self.create_latch(vert_pos, my_door, leaf, leaf_position, mirror_flag)

    def __del__(self):
        del self.my_latch
        del self.latch_py

        print("Deleted Latch Object", end="\n")

    def mirror_latch(self, latch_object):
        scene = bpy.context.scene
        scene.objects.active = latch_object

        bpy.ops.object.modifier_add(type='MIRROR')

        latch_object.modifiers['Mirror'].use_x=False
        latch_object.modifiers['Mirror'].use_y=True
        latch_object.modifiers['Mirror'].use_z=False

        bpy.ops.object.modifier_apply(apply_as='DATA', modifier='MIRROR')

        scene.objects.active = None


    def create_latch(self, vert_pos, my_door, leaf, leaf_position, mirror_flag):
        # IMPORTANT NOTE: If object has a parent object then the position is #
        # calculated relative to the parent origin and                       #
        # not to the global coordinate system!                               #

        scene = bpy.context.scene
        TOOTH_DEPTH = leaf.my_leaf.__class__.TOOTH_DEPTH

        print("leaf.my_leaf.leaf_width=", leaf.my_leaf.leaf_width)

        # Positioning latch constant in X axis.
        LATCH_OFFSET = leaf.my_leaf.leaf_width - 0.10 + TOOTH_DEPTH

        latch_mesh = bpy.data.meshes.new('Door.Latch.Mesh')
        latch_object = bpy.data.objects.new('Door.Latch', latch_mesh)

        scene = bpy.context.scene

        if leaf_position == 'LEFT':
            x = LATCH_OFFSET
#            print("X=", x)
#            print("leaf.leaf_py.location.x=", x)

        elif leaf_position == 'RIGHT':
            x = -LATCH_OFFSET
#            print("X =", x)
#            print("leaf.leaf_py.location.x=", x)

        FIX_PART = TOOTH_DEPTH + leaf.my_leaf.__class__.ROTATION_DEVIATION
        y = FIX_PART - leaf.my_leaf.leaf_depth / 2

        latch_object.location.x = x
        latch_object.location.y = y
        latch_object.location.z = vert_pos

        scene.objects.link(latch_object)
        latch_mesh.from_pydata(self.my_latch.vertices, [], self.my_latch.polygons)

        # Mirroring a latch on the other side of a door leaf.
        if mirror_flag:
            self.mirror_latch(latch_object)

        # Now recalculate mesh!
        latch_mesh.update(calc_edges=True)

        # Mirroring latche object if it has LEFT positioning.
        if leaf_position == 'LEFT':
            latch_object.select = True
            scene.objects.active = latch_object

            bpy.ops.transform.resize(value=(-1, 1, 1), constraint_axis=(True, False, False))

            latch_object.select = False
            scene.objects.active = None

        latch_object.show_wire = True

        # Parenting latche to leaf.
        latch_object.parent = leaf.leaf_py

        return latch_object


class Door_Hinges(object):
    def __init__(self, hinge_type, hinge_count, hinge_distance, door, leaf_position):
        if hinge_type == 'SIMPLE':
            self.my_hinge = hi.Hinge_Simple()

        elif hinge_type == 'TYPE2':
            self.my_hinge = hi.Hinge_Type2()

        elif hinge_type == 'TYPE3':
            self.my_hinge = hi.Hinge_Type3()

        # This is actualy four size tuple.
        self.hinge_py = self.create_hinges(hinge_count, hinge_distance, door, leaf_position)

    def __del__(self):
        del self.my_hinge
        del self.hinge_py

        print("Deleted Hinges Object", end="\n")

    # Join multiplied hinges object in to one.
    def join_hinges(self,
                    door,
                    hinge_count,
                    hinge_object_1,
                    hinge_object_2,
                    hinge_object_3,
                    hinge_object_4):
        """
        ### Joining multiplied hinges in to one object!
        """
        scene = bpy.context.scene

        scene.objects.active = None

        door.my_door.select = False # <<<<<????????
        hinge_object_2.select = True
        hinge_object_1.select = True
        scene.objects.active = hinge_object_1

        if hinge_count == 4:
            hinge_object_3.select = True
            hinge_object_4.select = True

            bpy.ops.object.join()

            hinge_object_3.select = False
            hinge_object_4.select = False

        elif hinge_count == 3:
            hinge_object_1.select = True
            hinge_object_2.select = True
            hinge_object_3.select = True

            bpy.ops.object.join()

            hinge_object_1.select = False
            hinge_object_2.select = False
            hinge_object_3.select = False

        else:
            bpy.ops.object.join()

        hinge_object_1.select = False
        hinge_object_2.select = False

        scene.objects.active = None

        return hinge_object_1

    def create_hinges(self, hinge_count, hinge_distance, door, leaf_position):

        scene = bpy.context.scene

        HINGE_OFFSET = 0.015

        frame_hole_width = (door.my_door.my_frame.frame_width - 2 * door.my_door.my_frame.sect_width)
        frame_hole_height = door.my_door.my_frame.frame_height - door.my_door.my_frame.sect_width

        # Calculating the hinge position in X and Y axis.
        if leaf_position == 'LEFT':
            x = -frame_hole_width / 2 - HINGE_OFFSET

        elif leaf_position == 'RIGHT':
            x = frame_hole_width / 2 + HINGE_OFFSET

        y = door.my_door.my_frame.sect_depth + HINGE_OFFSET

        if hinge_count == 2:
            hinge_mesh_1 = bpy.data.meshes.new('Door.Hinge.Mesh1')
            hinge_mesh_2 = bpy.data.meshes.new('Door.Hinge.Mesh2')

            hinge_object_1 = bpy.data.objects.new('Door.Hinge1', hinge_mesh_1)
            hinge_object_2 = bpy.data.objects.new('Door.Hinge2', hinge_mesh_2)
            hinge_object_3 = None
            hinge_object_4 = None

            # Calculating the hinge position in Z axis.
            # Just for clearity!
            hinge_bottom = hinge_distance
            hinge_top = frame_hole_height - hinge_distance

            hinge_object_1.location.x = x
            hinge_object_1.location.y = -y
            hinge_object_1.location.z = hinge_bottom
            hinge_object_2.location.x = x
            hinge_object_2.location.y = -y
            hinge_object_2.location.z = hinge_top

            scene.objects.link(hinge_object_1)
            scene.objects.link(hinge_object_2)
            hinge_mesh_1.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_1.update(calc_edges=True)
            hinge_mesh_2.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_2.update(calc_edges=True)

        elif hinge_count == 3:
            hinge_mesh_1 = bpy.data.meshes.new('Door.Hinge.Mesh1')
            hinge_mesh_2 = bpy.data.meshes.new('Door.Hinge.Mesh2')
            hinge_mesh_3 = bpy.data.meshes.new('Door.Hinge.Mesh3')

            hinge_object_1 = bpy.data.objects.new('Door.Hinge1', hinge_mesh_1)
            hinge_object_2 = bpy.data.objects.new('Door.Hinge2', hinge_mesh_2)
            hinge_object_3 = bpy.data.objects.new('Door.Hinge3', hinge_mesh_3)
            hinge_object_4 = None

            # Calculating the hinge position in Z axis.
            # Just for clearity!
            hinge_bottom = hinge_distance
            hinge_mid = frame_hole_height / 2
            hinge_top = frame_hole_height - hinge_distance

            hinge_object_1.location.x = x
            hinge_object_1.location.y = -y
            hinge_object_1.location.z = hinge_bottom
            hinge_object_2.location.x = x
            hinge_object_2.location.y = -y
            hinge_object_2.location.z = hinge_mid
            hinge_object_3.location.x = x
            hinge_object_3.location.y = -y
            hinge_object_3.location.z = hinge_top

            scene.objects.link(hinge_object_1)
            scene.objects.link(hinge_object_2)
            scene.objects.link(hinge_object_3)
            hinge_mesh_1.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_1.update(calc_edges=True)
            hinge_mesh_2.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_2.update(calc_edges=True)
            hinge_mesh_3.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_3.update(calc_edges=True)

        elif hinge_count == 4:
            hinge_mesh_1 = bpy.data.meshes.new('Door.Hinge.Mesh1')
            hinge_mesh_2 = bpy.data.meshes.new('Door.Hinge.Mesh2')
            hinge_mesh_3 = bpy.data.meshes.new('Door.Hinge.Mesh3')
            hinge_mesh_4 = bpy.data.meshes.new('Door.Hinge.Mesh4')

            hinge_object_1 = bpy.data.objects.new('Door.Hinge1', hinge_mesh_1)
            hinge_object_2 = bpy.data.objects.new('Door.Hinge2', hinge_mesh_2)
            hinge_object_3 = bpy.data.objects.new('Door.Hinge3', hinge_mesh_3)
            hinge_object_4 = bpy.data.objects.new('Door.Hinge4', hinge_mesh_4)

            # Calculating the hinge position in Z axis.
            # Just for clearity!
            hinge_bottom = hinge_distance
            div = (frame_hole_height - (2 * hinge_distance)) / 3 # Divisor for middle two hinges.
            hinge_mid_bottom = hinge_distance + div
            hinge_mid_top = frame_hole_height - hinge_distance - div
            hinge_top = frame_hole_height - hinge_distance

            hinge_object_1.location.x = x
            hinge_object_1.location.y = -y
            hinge_object_1.location.z = hinge_bottom
            hinge_object_2.location.x = x
            hinge_object_2.location.y = -y
            hinge_object_2.location.z = hinge_mid_bottom
            hinge_object_3.location.x = x
            hinge_object_3.location.y = -y
            hinge_object_3.location.z = hinge_mid_top
            hinge_object_4.location.x = x
            hinge_object_4.location.y = -y
            hinge_object_4.location.z = hinge_top

            scene.objects.link(hinge_object_1)
            scene.objects.link(hinge_object_2)
            scene.objects.link(hinge_object_3)
            scene.objects.link(hinge_object_4)
            hinge_mesh_1.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_1.update(calc_edges=True)
            hinge_mesh_2.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_2.update(calc_edges=True)
            hinge_mesh_3.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_3.update(calc_edges=True)
            hinge_mesh_4.from_pydata(self.my_hinge.vertices, [], self.my_hinge.polygons)
            hinge_mesh_4.update(calc_edges=True)

        # Joining hinge objects in to one.
        hinge_object = self.join_hinges(door,
                                        hinge_count,
                                        hinge_object_1,
                                        hinge_object_2,
                                        hinge_object_3,
                                        hinge_object_4)

        hinge_object.parent = door.door_py

        return hinge_object


class Add_Door(bpy.types.Operator):
    """Add a door object."""
    bl_idname = 'mesh.primitive_door_add'
    bl_label = "Door"
    bl_description = "Adding a door object to the scene."
    bl_options = { 'REGISTER', 'UNDO', 'PRESET' }

    # Property list
    door_type = EnumProperty(
        items=( ('SINGLE', 'Single', ''),
                ('DOUBLE', 'Double', ''),
                ('GARAGE', 'Garage', ''),
                ('INDUSTRIAL', 'Industrial', ''),
                ('GATE', 'Gate', '')),
        default='SINGLE',
        name='Type of door',
        description='These are possible door failies/categories'
    )

    frame_type = EnumProperty(
        items=( ('SIMPLE1', 'Simple Frame 1', ''),
                ('SIMPLE2', 'Simple Frame 2', ''),
                ('TYPE2', 'Type 2', ''),
                ('TYPE3', 'Type 3', '')),
        default='SIMPLE1',
        name='Frame Type',
        description='These are possible frame types'
    )

    accessories_leaf = BoolProperty(
        name='leaf',
        default=False,
        description="Include Leaf in Door object.",
        options={ 'ANIMATABLE'}
    )

    accessories_threshold = BoolProperty(
        name='threshold',
        default=False,
        description="Include Threshold in Door object.",
        options={'ANIMATABLE'}
    )

    accessories_latch = BoolProperty(
        name='latch',
        default=False,
        description="Include Latch in Door object.",
        options={'ANIMATABLE'}
    )

    accessories_hinges = BoolProperty(
        name='hinges',
        default=False,
        description="Include Hinges in Door object.",
        options={'ANIMATABLE'}
    )

    frame_width = FloatProperty(
        name="Door Width",
        default=1.00,
        min=0.061,
        max=15.00,
        description="Defines width of a door frame, the actual door width.",
        options={ 'ANIMATABLE' }
    )

    frame_height = FloatProperty(
        name="Door Height",
        default=2.10,
        min=0.031,
        max=15.00,
        description="Defines height of a door frame, the actual door height.",
        options={ 'ANIMATABLE' }
    )

    frame_sect_depth = FloatProperty( # door frame depth
        name="Frame Cross Section Depth",
        default=0.12,
        min=0.03,
        max=1.00,
        description="Defines depth of a door frame in cross section sense.",
        options={ 'ANIMATABLE' }
    )

    frame_sect_width = FloatProperty(
        name="Frame Cross Section Width",
        default=0.06,
        min=0.02,
        max=0.15,
        description="Defines width of a door frame in cross section sense.",
        options={ 'ANIMATABLE' }
    )

    rot_angle = FloatProperty(
        name='Rotate Door',
        default=0.00,
        min=0.00,
        max=180.00,
        description="Rotation of complete door",
        options={ 'ANIMATABLE' }
    )

    parapet = FloatProperty(
        name='Door Parapet',
        min=0.00,
        max=100.00,
        default=0.00,
        description="Door parapet",
        options={ 'ANIMATABLE' }
    )

    leaf_depth = FloatProperty(
        name='Leaf depth',
        min=0.025,
        max=0.20,
        default=0.045,
        description="Leaf depth",
        options={ 'ANIMATABLE' }
    )

    latch_type = EnumProperty(
        items=( ('TYPE1', 'Type 1', ''),
                ('TYPE2', 'Type 2', ''),
                ('TYPE3', 'Type 3', ''),
                ('TYPE4', 'Type 4', ''),
                ('TYPE5', 'Type 5', '')),
        default='TYPE1',
        name='Latch type',
        description='These are possible latch types'
    )

    latch_vertical_pos = FloatProperty(
        name='Leaf depth',
        min=0.20,
        max=frame_height[1]['max'],
        default=1.00,
        description="Leaf depth",
        options={ 'ANIMATABLE' }
    )

    mirror_latch = BoolProperty(
        name='mirror a latch',
        default=True,
        description="Mirroring a latch on the other side of the door leaf."
        #options={ 'ANIMATABLE' }
    )

    # NOTE: Not yet in use!!!! Jun 23, 2012.
    latch_horizontal_pos = FloatProperty(
        name='Leaf depth',
        min=0.05,
        max=frame_width[1]['max'],
        default=0.035,
        description="Horizontal latch position against door leaf.",
        options={ 'ANIMATABLE' }
    )

    leaf_types = EnumProperty(
        items=( ('SIMPLE1', 'Simple Leaf 1', ''),
                ('SIMPLE2', 'Simple Leaf 2', '') ),
        name="Leaf Types",
        default='SIMPLE1',
        description="There are infinite possibilities..."
    )

    leaf_position = EnumProperty(
        items=( ('LEFT', 'Left', 'Leaf left position'),
                ('RIGHT', 'Right', 'Leaf right position') ),
        default='LEFT',
        name="Leaf positioning. Left or Right orientation.",
        description="",
        options={ 'ANIMATABLE' }
    )

    door_rot_angle = FloatProperty(
        name='Rotate Door',
        default=0.00,
        min=-180.00,
        max=180.00,
        description="Rotaion of the door",
        options={ 'ANIMATABLE' }
    )

    leaf_rot_angle = FloatProperty(
        name='Rotate Leaf',
        default=0.00,
        min=0.00,
        max=180.00,
        description="Rotation of a door leaf",
        options={ 'ANIMATABLE' }
    )

    threshold_sect_width = FloatProperty(
        name='Thershold Width',
        default=0.12,
        min=0.03,
        max=1.00,
        description="Threshold section width",
        options={ 'ANIMATABLE' }
    )

    threshold_sect_height = FloatProperty(
        name='Threshold Height',
        default=0.02,
        min=0.02,
        max=0.05,
        description="Threshold section height",
        options={ 'ANIMATABLE' }
    )

    hinge_count = IntProperty(
        name='Number of hinges',
        default=2,
        min=2,
        max=4,
        description='How many hinges we need?'
    )

    hinge_type = EnumProperty(
        items=( ('SIMPLE', 'Simple', ''),
                ('TYPE2', 'Type 2', ''),
                ('TYPE3', 'Type 3', '')),
        default='SIMPLE',
        name='Hinge Type',
        description='These are three possible hinge types.'
    )

    hinge_distance = FloatProperty(
        name='Hinge distance',
        default=0.20,
        min=0.10,
        max=0.50,
        description='Distance from bottom hinge to floor, and top hinge to frame hole height.',
        options={ 'ANIMATABLE' }
    )

    #@classmethod
    #def poll(cls, context):
    #    return context.scene != None
    #    return context.active_object != None


    def draw(self, context):
        layout = self.layout

        # The box for Door & Frame
        box = layout.box()
        row = box.row()
        row.label(text="Door & Frame Type:")
        box.prop(self, 'door_type', text="Door Type")
        box.prop(self, 'frame_type', text="Frame Type")

        box.separator()

        col = box.column(align=True)
        row = col.row()
        row.label(text="Accessories:")
        row = col.row()
        leaf_split = row.split()
        leaf_split.prop(self, 'accessories_leaf', text="Leaf", toggle=True)
        row.prop(self, 'accessories_threshold', text="Threshold", toggle=True)
        if self.accessories_leaf:
            row.prop(self, 'accessories_latch', text="Latch", toggle=True)
            row.prop(self, 'accessories_hinges', text="Hinges", toggle=True)
            if self.accessories_latch or self.accessories_hinges:
                leaf_split.enabled = False
            else:
                leaf_split.enabled = True

        row.separator()

        col = box.column(align=True)
        row = col.row()
        row.label(text="Frame parameters:")
        row = col.row()
        row.prop(self, 'frame_width', text="Door Width")
        row.prop(self, 'frame_height', text="Frame Height")

        col = box.column(align=True)
        row = col.row()
        row.prop(self, 'frame_sect_depth', text="Frame cross-section depth")
        row.prop(self, 'frame_sect_width', text="Frame cross-section width")
        row = col.row()
        row.prop(self, 'door_rot_angle', text="Door Rotation")

        # The box for Threshold part
        if self.accessories_threshold:
            threshold_box = layout.box()
            col = threshold_box.column(align=True)
            row = col.row()
            row.label(text="Threshold Parameters:")
            row = col.row()
            row.prop(self, 'threshold_sect_width', text="Threshold Width")
            row.prop(self, 'threshold_sect_height', text="Threshold Height")

        # The box for Leaf part
        if self.accessories_leaf:
            leaf_box = layout.box()
            col = leaf_box.column(align=True)
            row = col.row()
            row.label(text="Leaf parameters:")
            row = col.row()
            row.prop(self, 'leaf_types', text="Leaf Types")
            col = leaf_box.column(align=True)
            row = col.row()
            row.prop(self, 'leaf_depth', text="Leaf Depth")
            row.prop(self, 'leaf_position', text="Position")

            col = leaf_box.column(align=True)
            row = col.row()
            row.prop(self, 'leaf_rot_angle', text="Rotate Leaf")

            # The box for Latch part
            if self.accessories_latch:
                row = leaf_box.row()
                row.prop(self, 'mirror_latch', text="Mirror")
                row.prop(self, 'latch_type', text="Latch Type")

            # The box for Hinge part
            if self.accessories_hinges:
                hinges_box = layout.box()
                col = hinges_box.column(align=True)
                row = col.row()
                row.label(text="Hinges Parameters:")
                row = col.row()
                row.prop(self, 'hinge_distance', text="Hinge Distance")
                row = col.row()
                row.prop(self, 'hinge_type', text="Hinge Types")
                row.prop(self, 'hinge_count', text="Hinge Number")


    def execute(self, context):
        """NOTE: The actual logic for complete application is here.
        Creates an instance of a Door object.
        """
        # NOTE: Maybe the whole logic should be placed in some global main function???
        door = Door(self.door_type,
                    self.frame_type,
                    self.frame_width,
                    self.frame_height,
                    self.frame_sect_width,
                    self.frame_sect_depth,
                    self.door_rot_angle)

        leaf = None
        threshold = None
        latch = None
        hinge = None

        if self.accessories_leaf:
            # My custom object, not a blender-python API object.
            leaf = Door_Leaf(self.leaf_types, door,
                             self.leaf_depth, self.leaf_position,
                             self.leaf_rot_angle, latch)

            # Nesting latch and hinge inside leaf condition.
            if self.accessories_latch:
                latch = Door_Latch(self.latch_type,
                                   door.my_door, # Because I need only frame depth.
                                   leaf,
                                   self.latch_vertical_pos,
                                   self.mirror_latch,
                                   self.leaf_position)

            if self.accessories_hinges:
                hinge = Door_Hinges(self.hinge_type,
                                    self.hinge_count,
                                    self.hinge_distance,
                                    door,
                                    self.leaf_position)

        if self.accessories_threshold:
            threshold = Door_Threshold(door,
                                       self.threshold_sect_width,
                                       self.threshold_sect_height)

        return { 'FINISHED'}


#if __name__ == '__main__':
#    main()
