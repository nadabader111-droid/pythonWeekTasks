class Room:

    #ctor
    def __init__(self,w,l):
        self.width=w
        self.length=l

    def get_Area(self):
        area = self.width * self.length
        return  area

