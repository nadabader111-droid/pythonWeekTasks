class Patient:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height  = height

    def getBMI(self):
        bmi =  self.weight / (self.height / 100) ** 2
        return bmi

    def getstatus(self ):
        bmi =self.getBMI()
        if bmi > 30:
            return('Obese')
        elif bmi > 24:
            return('Over Weight')
        elif bmi > 18:
            return('Normal Weight')
        else:
            return('Under Weight')