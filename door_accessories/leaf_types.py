# Prefabricated Leafs
# Date created: Jun 13, 2012
# Date last edited: (Jun 20, 2012), Oct 11, 2012
# Author: Kolozsi Róbert


class Leaf_Simple1(object):
    """Most simple, full-box like leaf.
    """
    ROTATION_DEVIATION = 0.015
    TOOTH_DEPTH = 0.00 # Needed for other leaf types positioning in correct place, against frame.


    def __init__(self, leaf_depth, my_frame, leaf_position):

        self.name = 'Simple Leaf 1'

        self.leaf_depth = leaf_depth
        self.frame_light_width = my_frame.my_frame.frame_width - 2 * my_frame.my_frame.sect_width
        self.leaf_width = self.frame_light_width + 2 * Leaf_Simple1.TOOTH_DEPTH
        self.frame_light_height = my_frame.my_frame.frame_height - my_frame.my_frame.sect_width
        self.leaf_height = self.frame_light_height + Leaf_Simple1.TOOTH_DEPTH

        y0 = -self.leaf_depth + Leaf_Simple1.ROTATION_DEVIATION # Plane toward me.
        y1 = y0 + self.leaf_depth

        z0 = 0.00
        z1 = self.leaf_height

        if leaf_position == 'LEFT':
            x0 = Leaf_Simple1.ROTATION_DEVIATION
            x1 = self.leaf_width + Leaf_Simple1.ROTATION_DEVIATION

        elif leaf_position == 'RIGHT':
            x0 = -self.leaf_width - Leaf_Simple1.ROTATION_DEVIATION
            x1 = -Leaf_Simple1.ROTATION_DEVIATION

        self.vertices = [
           (x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
           (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1),
        ]

        self.polygons = [
           (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
           (0, 3, 2, 1), (4, 5, 6, 7),
        ]

    def __del__(self):
        del self.name
        del self.leaf_depth
        del self.frame_light_width
        del self.leaf_width
        del self.frame_light_height
        del self.leaf_height

        return "deleted leaf"

    def __str__(self):
        return self.name


class Leaf_Simple2(object):
    """Simple full leaf with tooth.
    """
    ROTATION_DEVIATION = 0.015
    TOOTH_DEPTH = 0.015

    def __init__(self, leaf_depth, my_frame, leaf_position):
        self.name = 'Simple Leaf 2'

        self.leaf_depth = leaf_depth

        self.frame_light_width = (my_frame.my_frame.frame_width - \
                                 2 * my_frame.my_frame.sect_width)

        self.leaf_width = self.frame_light_width + \
                          3 * Leaf_Simple2.TOOTH_DEPTH + \
                          Leaf_Simple2.ROTATION_DEVIATION

        self.frame_light_height = my_frame.my_frame.frame_height - \
                                  my_frame.my_frame.sect_width

        self.leaf_height = self.frame_light_height + \
                           2 * Leaf_Simple2.TOOTH_DEPTH

        # Y axis
        self.origin_offset = self.leaf_depth - Leaf_Simple2.TOOTH_DEPTH
        #print("origin_offset:", self.origin_offset, end='\n')

        # Face pointig off me (outer face). Plane has to be fixfixed.
        y1 = Leaf_Simple2.TOOTH_DEPTH + Leaf_Simple2.ROTATION_DEVIATION

        # Face between two above faces. Plane has to be fixed.
        self.y_tooth = y1 - Leaf_Simple2.ROTATION_DEVIATION

        # Face pointing toward me (inner face). Plane has to be movable.
        y0 = -self.leaf_depth + self.y_tooth + Leaf_Simple2.TOOTH_DEPTH

        # The length of reminder door leaf - tooth
        self.reminder = self.leaf_depth - Leaf_Simple2.TOOTH_DEPTH

        # Z axis
        z0 = 0.00
        z1 = self.leaf_height
        z_tooth = z1 - Leaf_Simple2.TOOTH_DEPTH

        # For x direction purposes (half of rotating deviation)
        half_dev = Leaf_Simple2.ROTATION_DEVIATION

        if leaf_position == 'LEFT': # The origin of the leaf is on the left.
            # X axis (Leaf_half_dev is needed to offset)
            x0 = 0.00 + Leaf_Simple2.ROTATION_DEVIATION #half_dev
            x0_tooth = x0 + Leaf_Simple2.TOOTH_DEPTH 
            x1 = self.leaf_width + Leaf_Simple2.ROTATION_DEVIATION #half_dev
            x1_tooth = x1 - Leaf_Simple2.TOOTH_DEPTH


        elif leaf_position == 'RIGHT':
            # X axis (half_dev is needed to offset)
            x0 = -self.leaf_width - Leaf_Simple2.ROTATION_DEVIATION #half_dev
            x0_tooth = x0 + Leaf_Simple2.TOOTH_DEPTH
            x1 = 0.00 - Leaf_Simple2.ROTATION_DEVIATION #half_dev
            x1_tooth = x1 - Leaf_Simple2.TOOTH_DEPTH

        self.vertices = [
            (x0, y0, z0),
            (x0, self.y_tooth, z0),
            (x1, self.y_tooth, z0),
            (x1, y0, z0),
            (x0, y0, z1),
            (x0, self.y_tooth, z1),
            (x1, self.y_tooth, z1),
            (x1, y0, z1),
            (x1_tooth, self.y_tooth, z1),
            (x1_tooth, self.y_tooth, z0),
            (x1_tooth, y0, z1),
            (x1_tooth, y0, z0),
            (x1, y0, z_tooth),
            (x1, self.y_tooth, z_tooth),
            (x0, y0, z_tooth),
            (x0, self.y_tooth, z_tooth),
            (x0_tooth, y1, z0),
            (x1_tooth, y1, z0),
            (x0_tooth, self.y_tooth, z1),
            (x0_tooth, y0, z0),
            (x0_tooth, self.y_tooth, z0),
            (x0_tooth, y0, z1),
            (x1_tooth, y0, z_tooth),
            (x1_tooth, self.y_tooth, z_tooth),
            (x1_tooth, y1, z_tooth),
            (x0_tooth, y1, z_tooth),
            (x0_tooth, self.y_tooth, z_tooth),
            (x0_tooth, y0, z_tooth)
        ]

        self.polygons = [(14, 15, 1, 0), (23, 13, 2, 9), (13, 12, 3, 2), (27, 14, 0, 19),
                         (11, 9, 2, 3), (21, 18, 5, 4), (25, 16, 20, 26), (12, 22, 11, 3),
                         (19, 20, 9, 11), (7, 6, 8, 10), (4, 5, 15, 14), (18, 8, 23, 26),
                         (6, 7, 12, 13), (10, 21, 27, 22), (21, 4, 14, 27), (8, 6, 13, 23),
                         (22, 27, 19, 11), (7, 10, 22, 12), (15, 26, 20, 1), (23, 9, 17, 24),
                         (26, 23, 24, 25), (25, 24, 17, 16), (10, 8, 18, 21), (5, 18, 26, 15),
                         (0, 1, 20, 19), (16, 17, 9, 20)]

    @staticmethod
    def get_deviation():
        return Leaf_Simple2.ROTATION_DEVIATION

    def __del__(self):
        del self.name
        del self.leaf_depth
        del self.frame_light_width
        del self.leaf_width
        del self.frame_light_height
        del self.leaf_height
        del self.origin_offset

        return "deleted leaf"

    def __str__(self):
        return self.name

