'''try:
    a=int(input("a: "))
    b=int(input("b: "))
    c=a+b
    e=a/b
    print("try successful")
except ArithmeticError:
    print("arithmetic error occurred")
except Exception:
    print("exception occurred")
else:
    print("hi")
finally:
    print("executed in any condition")
   '''
#================================================================================
'''def checkage(age):
    if age<0:
        raise ValueError("age should be grater than or equal to zero")
    print("age is valid")
  try:
    age = int(input("age: "))
    checkage(age)
except ValueError as err:
    print(err.args)
finally:
    print("executed in any condition")'''
#===============================================================================
'''try:
    number1,number2=eval(input("Enter two number by a comma "))
    result=number1/number2
    print("Result is" ,result)
except ZeroDivisionError:
    print("Division by zero")
except SyntaxError:
    print("A comma may be missing in the input")
except:
    print("Something wrong in the input")
else:
    print("No exception")
finally:
    print("The finally clause is executed")'''
#=================================================================================

