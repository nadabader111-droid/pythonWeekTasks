class Student:

    def  __init__(self,name,mark,fullMark):
        self.name =name
        self.mark =mark
        self.fullmark =fullMark

    def   get_PCT(self):
        pct = self.mark /self.fullmark *100
        return pct

    def getGrade(self):
        pct =self.get_PCT()
        if pct >= 84:
            return ('Excellent')
        elif pct > 74:
            return('v.good')
        elif pct > 64:
            return('Good')
        elif pct >= 50:
            return('pass')
        else:
            return('Failed')



#patient test_paintient
    #name weight height
    #getBMI(),getStatus()
