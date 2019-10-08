class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        total = 0
        for score in scores:
            total += score
        
        avg = total/len(scores)
        
        if 90 <= avg and avg <= 100:
            return 'O'
        elif 80 <= avg and avg < 90:
            return 'E'
        elif 70 <= avg and avg < 80:
            return 'A'
        elif 55 <= avg and avg < 70:
            return 'P'
        elif 40 <= avg and avg < 55:
            return 'D'
        else:
            return 'T'
   
