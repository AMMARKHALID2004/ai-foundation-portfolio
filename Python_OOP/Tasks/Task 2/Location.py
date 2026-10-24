from Point import Point
class Location:
    def __init__(self,loc_x,loc_y,dest_x,dest_y):
        self.start_point=Point(loc_x,loc_y)
        self.dest_point=Point(dest_x,dest_y)
    def reflected_axis(self):
        reflected_x=self.dest_point.x
        reflected_y=(-1)*self.dest_point.y
        return f"The reflected axis is ({reflected_x},{reflected_y})"
