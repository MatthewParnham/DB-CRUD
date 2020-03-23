

class Student:

    def __init__(self,studentId,firstName,lastName,GPA,major,facultyAdvisor):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.GPA = GPA
        self.major = major
        self.facultyAdvisor = facultyAdvisor

    def getStudentId(self):
        return self.studentId

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getGPA(self):
        return self.GPA

    def getMajor(self):
        return self.major

    def getFacultyAdvisor(self):
        return self.facultyAdvisor

    def getStudent(self):
        return "ID: " + str(self.studentId) + " Name: " + str(self.lastName) + ", " + str(self.firstName) + " GPA: " + str(self.GPA) + " Major: " + str(self.major) + " Faculty Advisor: " + str(self.facultyAdvisor)