
class Calculator:
      def add (self,num1,num2):
        return num1+num2
      def substract(self,num1,num2):
        return num1-num2
      def multiply (self,num1,num2):
        return num1*num2 
      def divided(self,num1,num2):
        return num1/num2

calc=Calculator()      
print("enter your choice\n")
print("1.  for add\n")
print("2.  for substract\n")
print("3.  for multiply\n")
print("4.  for divided\n")
choice=int(input(""))

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
if (choice==1): 
      sum=calc.add(int(num1),int(num2))
      print("sum is: "+str(sum)) 
elif(choice==2):
      print("diferent is: "+str(calc.substract(float(num1),float(num2))))      
elif(choice==3):
      print("product is: "+str(calc.multiply(float(num1),float(num2))))
elif(choice==4):
      print("ratio is: "+str(calc.divided(float(num1),float(num2))))
