class Employee(object):
    def showEmployeeData(self,name,email):
        print("name: "+name)
        print("email: "+email)
class Manager(Employee):
        def showEmployeeData(self,department,saraly):
           print("department: "+department)
           print("saraly: "+saraly)


class Accaountant(Employee):
     def showAccaountant(self,jobTitle,saraly):
         print("jobTitle: "+jobTitle)
         print("saraly: "+saraly)

Manager=Manager()
print("Employee data\n.............\n")
Manager.showEmployeeData("patrick","birori@gmail.com")
print("\nManager data\n.......")
Manager.showEmployeeData("software engineer","20020") 

acc=Accaountant() 
print("\n\nAccount data\data\n........")
acc.showEmployeeData("innocent","in@gmail.com")       
