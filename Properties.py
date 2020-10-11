class Status:
    ipoints = 0

    @property
    def points(self):
        return int(self.ipoints or 0)

    @points.setter
    def points(self, new_points):
        self.ipoints = new_points


status = Status()
print(status.points)
status.points = 10
print(status.points)
