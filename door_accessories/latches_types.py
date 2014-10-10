# Prefabricated Latches
# Date created: Jun 11, 2012
# Author: Kolozsi Róbert

class Latch_Type1():
    def __init__(self, leaf):
        self.name = "Type1 Latch"
        self.offset_origin = leaf.my_leaf.leaf_depth / 2

        self.vertices = [
            (-0.014999999664723873, -0.004999999888241291 - self.offset_origin, -0.11499998718500137),
            (-0.014999999664723873, 0.0 - self.offset_origin, -0.11499998718500137),
            (0.014999999664723873, 0.0 - self.offset_origin, -0.11499998718500137),
            (0.014999999664723873, -0.004999999888241291 - self.offset_origin, -0.11499998718500137),
            (-0.014999999664723873, -0.004999999888241291 - self.offset_origin, 0.11499998718500137),
            (-0.014999999664723873, 0.0 - self.offset_origin, 0.11499998718500137),
            (0.014999999664723873, 0.0 - self.offset_origin, 0.11499998718500137),
            (0.014999999664723873, -0.004999999888241291 - self.offset_origin, 0.11499998718500137),
            (-0.008113863877952099, -0.04773304611444473 - self.offset_origin, 0.030987177044153214),
            (-0.008113863877952099, -0.004999999888241291 - self.offset_origin, 0.030987177044153214),
            (0.008113863877952099, -0.004999999888241291 - self.offset_origin, 0.030987177044153214),
            (0.008113863877952099, -0.04773304611444473 - self.offset_origin, 0.030987177044153214),
            (-0.008113863877952099, -0.04773304611444473 - self.offset_origin, 0.04721488803625107),
            (-0.008113863877952099, -0.004999999888241291 - self.offset_origin, 0.04721488803625107),
            (0.008113863877952099, -0.004999999888241291 - self.offset_origin, 0.04721488803625107),
            (0.008113863877952099, -0.04773304611444473 - self.offset_origin, 0.04721488803625107),
            (-0.008113863877952099, -0.032231368124485016 - self.offset_origin, 0.04721488803625107),
            (-0.008113863877952099, -0.032231368124485016 - self.offset_origin, 0.030987177044153214),
            (0.008113863877952099, -0.032231368124485016 - self.offset_origin, 0.04721488803625107),
            (0.008113863877952099, -0.032231368124485016 - self.offset_origin, 0.030987177044153214),
            (0.07762917876243591, -0.032231368124485016 - self.offset_origin, 0.030987177044153214),
            (0.07762917876243591, -0.032231368124485016 - self.offset_origin, 0.04721488803625107),
            (0.07762917876243591, -0.04773304611444473 - self.offset_origin, 0.04721488803625107),
            (0.07762917876243591, -0.04773304611444473 - self.offset_origin, 0.030987177044153214)]

        self.polygons = [
            (4, 5, 1, 0), (5, 6, 2, 1), (6, 7, 3, 2), (7, 4, 0, 3),
            (0, 1, 2, 3), (7, 6, 5, 4), (16, 13, 9, 17), (13, 14, 10, 9),
            (18, 15, 22, 21), (15, 12, 8, 11), (17, 9, 10, 19), (18, 14, 13, 16),
            (12, 16, 17, 8), (14, 18, 19, 10), (8, 17, 19, 11), (15, 18, 16, 12),
            (20, 23, 11, 19), (21, 20, 19, 18), (15, 11, 23, 22), (21, 22, 23, 20) ]

    def __del__(self):
        del self.name
        del self.offset_origin
        del self.vertices
        del self.polygons

        return "deleted latch"

    def __str__(self):
        return self.name


class Latch_Type2():
    def __init__(self):
        self.name = 'Type2 Latch'

        self.vertices = [
            ###
        ]

        self.polygons = [
            ###
        ]

    def __del__(self):
        del self.name
        del self.offset_origin
        del self.vertices
        del self.polygons

        return "deleted latch"

    def __str__(self):
        return self.name


class Latch_Type3():
    def __init__(self):
        self.name = 'Type3 Latch'

        self.vertices = [
            ###
        ]

        self.polygons = [
            ###
        ]

    def __del__(self):
        del self.name
        del self.offset_origin
        del self.vertices
        del self.polygons

        return "deleted latch"

    def __str__(self):
        return self.name

class Latch_Type4():
    def __init__(self):
        self.name = 'Type4 Latch'

        self.vertices = [
            ###
        ]

        self.polygons = [
            ###
        ]

    def __del__(self):
        del self.name
        del self.offset_origin
        del self.vertices
        del self.polygons

        return "deleted latch"

    def __str__(self):
        return self.name

class Latch_Type5():
    def __init__(self):
        self.name = 'Type5 Latch'

        self.vertices = [
            ###
        ]

        self.polygons = [
            ###
        ]

    def __del__(self):
        del self.name
        del self.offset_origin
        del self.vertices
        del self.polygons

        return "deleted latch"

    def __str__(self):
        return self.name

