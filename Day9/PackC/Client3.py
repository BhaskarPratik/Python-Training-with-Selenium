# Approach 1:
import sys

sys.path.append("E:/PythonTraining/Day9/PackA")
sys.path.append("E:/PythonTraining/Day9/PackB")
#
# import Emp
#
# empobj = Emp.Employee(101, "Merry", 185000)
# empobj.displayemp()
#
# import Stu
#
# objstu = Stu.Student(102, "John", 125000)
# objstu.displaystu()

# Approach 2:

from Emp import Employee
objEmp = Employee(102,"Kash",158000)
objEmp.displayemp()

from Stu import Student
objStu = Student(103,"Rani",152500)
objStu.displaystu()
