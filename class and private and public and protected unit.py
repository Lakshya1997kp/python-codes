class student:
    def __init__(self,name, age):
        self.name = name
        self.age=age
    def setDetails(self,group,report):
        self.__group = group
        self.__report = report
    def getdetails(self):
        print(self.name,self.age,self.__group,self.___report)

print("student Report Card")
s1= student("Sri Ram","19")
s1.setDetails("CSC" , "pass")
s1.getdetails()
