# Prefabricated Thresholds
# Date created: Jun 13, 2012
# Date last edited: (Jun 20, 2012), Oct 11, 2012
# Author: Kolozsi Róbert


class Threshold_Simple():
    """
    """
    def __init__(self, door, sect_width, sect_height):
        self.name = "Threshold Simple"
        self.width = door.my_door.my_frame.frame_width
        self.sect_width = sect_width
        self.sect_height = sect_height

        y0 = -door.my_door.my_frame.sect_depth
        y1 = y0 + self.sect_width

        z0 = 0.00
        z1 = self.sect_height

        x0 = -(door.my_door.my_frame.frame_width / 2) + door.my_door.my_frame.sect_width
        x1 = (door.my_door.my_frame.frame_width / 2) - door.my_door.my_frame.sect_width

        self.vertices = [
            (x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
            (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)
        ]

        self.faces = [
            (0, 1, 5, 4), (4, 5, 6, 7), (2, 3, 7, 6), (1, 0, 3, 2),
            (1, 2, 6, 5), (3, 0, 4, 7),
        ]

    def __del__(self):
        del self.name
        del self.width
        del self.sect_width
        del self.sect_height

        return ""

    def __str__(self):
        return self.name
