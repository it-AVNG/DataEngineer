num1=11
num2=num1

print(id(num1)==id(num2))

# if we update num2 = 22, the id will be different, 
# as it points to a different memory location

dict1 = {
    'value': 11
}

dict2 = {
    'value': 11
    }

dict2 =dict1

dict2['value'] =2

print(id(dict1))
print(id(dict2))

print(dict1['value'])
