'''num1=int(input("num1: "))
num2=int(input("num2: "))
try:
    num3=num1/num2
    print(num3)         #so exception  is required to print the sentece other then getting errors such as nameerror , syntax error etc 
except:
    print("exception occured")
    '''
#=============================================================================================================================================================
num1=int(input("num1: "))
num2=int(input("num2: "))
if num2== 0:
    print("exception occured")            #it can be used to define some errors such as zero divison , but errors such as syntax errors and name errors acn only be defined by "try" and "except"
elif num2!=0:
    num3=num1/num2
    print(num3)
