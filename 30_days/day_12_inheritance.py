class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        mean_score = sum(self.scores) / len(self.scores)
        grades = 'TDPAEO'
        conditions = [40, 55, 70, 80, 90]

        idx = sum(mean_score >= c for c in conditions)

        return grades[idx]


x = Student('foo', 'bar', 10, [100, 100, 100, 100, 100, 100, 100, 100])

x.calculate()
