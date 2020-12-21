class points:
    def __init__(self):
        self.points = list()

    def add_point(self, point):
        self.points.append(point)

    def get_range(self, yards):
        for point in self.points:
            if point.get_yards() == yards:
                return point
