# Prefabricated Hinges
# Date created: Jun 20, 2012
# Author: Kolozsi Róbert

class Frame_Simple1():
    def __init__(self, width, height, sect_width, sect_depth):
        self.name = 'Simple Frame1'

        self.frame_width = width
        self.frame_height = height
        self.sect_width = sect_width
        self.sect_depth = sect_depth

        y0 = -self.sect_depth
        y1 = 0.00

        z0 = 0.00
        z1 = self.frame_height - self.sect_width
        z2 = self.frame_height


        x0 = -self.frame_width / 2
        x1 = x0 + self.sect_width
        x3 = self.frame_width / 2
        x2 = x3 - self.sect_width

        self.vertices = [
            (x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), # 0, 1, 2, 3
            (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1), # 4, 5, 6, 7
            (x0, y0, z2), (x1, y0, z2), (x1, y1, z2), (x0, y1, z2), # 8, 9, 10, 11
            (x2, y0, z2), (x3, y0, z2), (x3, y1, z2), (x2, y1, z2), # 12, 13, 14, 15
            (x2, y0, z1), (x3, y0, z1), (x3, y1, z1), (x2, y1, z1), # 16, 17, 18, 19
            (x2, y0, z0), (x3, y0, z0), (x3, y1, z0), (x2, y1, z0)  # 20, 21, 22, 23
        ]

        self.polygons = [
            (0, 3, 2, 1), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (0, 1, 5, 4),
            (4, 5, 9, 8), (7, 4, 8, 11), (6, 7, 11, 10), (8, 9, 10, 11),
            (5, 6, 19, 16), (9, 12, 15, 10), (5, 16, 12, 9), (19, 6, 10, 15),
            (12, 13, 14, 15), (18, 19, 15, 14), (17, 18, 14, 13), (16, 17, 13, 12),
            (20, 21, 17, 16), (21, 22, 18, 17), (22, 23, 19, 18), (23, 20, 16, 19), (20, 23, 22, 21) 
        ]

    def __del__(self):
        del self.name
        del self.frame_width
        del self.frame_height
        del self.sect_width
        del self.sect_depth

        return "frame deleted"

    def __str__(self):
        return self.name


class Frame_Simple2():
    def __init__(self, width, height, sect_width, sect_depth):
        self.name = 'Simple Frame2'

        self.frame_width = width
        self.frame_height = height
        self.sect_width = sect_width
        self.sect_depth = sect_depth

        y0 = -self.sect_depth
        y1 = 0.00

        z0 = 0.00
        z1 = self.frame_height - self.sect_width
        z2 = self.frame_height

        x0 = -self.frame_width / 2
        x1 = x0 + self.sect_width
        x3 = self.frame_width / 2
        x2 = x3 - self.sect_width

        self.vertices = [
            (x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), # 0, 1, 2, 3
            (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1), # 4, 5, 6, 7
            (x0, y0, z2), (x1, y0, z2), (x1, y1, z2), (x0, y1, z2), # 8, 9, 10, 11
            (x2, y0, z2), (x3, y0, z2), (x3, y1, z2), (x2, y1, z2), # 12, 13, 14, 15
            (x2, y0, z1), (x3, y0, z1), (x3, y1, z1), (x2, y1, z1), # 16, 17, 18, 19
            (x2, y0, z0), (x3, y0, z0), (x3, y1, z0), (x2, y1, z0)  # 20, 21, 22, 23
        ]

        self.polygons = [
            (0, 3, 2, 1), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (0, 1, 5, 4),
            (4, 5, 9, 8), (7, 4, 8, 11), (6, 7, 11, 10), (8, 9, 10, 11),
            (5, 6, 19, 16), (9, 12, 15, 10), (5, 16, 12, 9), (19, 6, 10, 15),
            (12, 13, 14, 15), (18, 19, 15, 14), (17, 18, 14, 13), (16, 17, 13, 12)
            (20, 21, 17, 16), (21, 22, 18, 17), (22, 23, 19, 18), (23, 20, 16, 19), (20, 23, 22, 21) 
        ]

    def __del__(self):
        del self.name
        del self.frame_width
        del self.frame_height
        del self.sect_width
        del self.sect_depth

        return "frame deleted"

    def __str__(self):
        return self.name

