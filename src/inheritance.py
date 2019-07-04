class Person:
    def __init__(self, p_firstName, p_lastName, idNumber):
        self.firstName = p_firstName
        self.lastName = p_lastName
        self.idNum = idNumber

    def printPerson(self):
        if len(self.firstName) >= 1 and len(self.lastName) <= 10:
            print("Name:", self.firstName + ',', self.lastName)
        if len(self.idNum) == 7:
            print("ID: ", self.idNum)


class Student(Person):
    def __init__(self, s_firstName, s_lastName, s_idNumber, s_scores):
        super().__init__(s_firstName, s_lastName, s_idNumber)
        self.scores = s_scores


    def calculate(self):
        if self.scores is None:
            return None
        for val in self.scores:
            if 0 <= val <= 100:
                avg = int(sum(self.scores)/len(self.scores))
                grade = self.get_grade(avg)
                return grade

    def get_grade(self, s_avg):
        if 90 <= s_avg <= 100:
            return 'O'
        elif 80 <= s_avg <= 90:
            return 'E'
        elif 70 <= s_avg <= 80:
            return 'A'
        elif 55 <= s_avg <= 70:
            return 'P'
        elif 40 <= s_avg <= 55:
            return 'D'
        elif s_avg < 40:
            return 'T'


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    # numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
