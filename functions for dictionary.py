emp={"Name":"Sudharshan","age":18,}
emp.clear()
print(len(emp))


fruts={"apple":"red","orange":"orange","mango":"yellow"}
dict2=fruits.copy()
print(dict2)

dict1={'cyan':1,'violet':2,'green':3}
dict1.setdefault('red',10)
print(dict1)
dict1.setdefautl('violet',10)
print(dict1)

dict1={'cyan':1,'violet':2,'green':3}
dict2={'red':4,'white':5}
dict1.update(dict2)
print(dict1)


            #***LIST COMPREHENSION***
l=[i for i in range(1,11)]
print(l)

print([i for i in range (1,11) if (not i % 2==0)]#list comprehension to print only odd

print ([a*b for a in [1,2,3] for b in [10,20,30]])

l=[a for a in [10,8,5,4] for b in [4,5,7,10] if a==b]
      print(l)


          #***DICTIONARY COMPREHENSION***
LIST1=[10,20,30]
dict1={key:vaue for key,value in enumerate(LIST1)}
print(dict1)

dict2={i:i**2 for i in range(1,11)}
print(dict1)

dict2={i.lower():i for i  in "PYTHON"}
print(dict2)
