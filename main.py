class StudentsInMLOps:
    def __init__(self, name, roll_no):
        self.strength = 0
        self.name = name
        self.roll_no = roll_no
        
    def enrollStudents(self, count):
        self.strength += count
        return self.strength
       
    def dropStudents(self, count):
        self.strength -= count
        return self.strength

    def getTotalStrength(self):
        return self.strength 
                
    def getClassName(self):
        return "MLOps N"            