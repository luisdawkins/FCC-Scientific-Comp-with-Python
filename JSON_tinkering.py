#Input
#The JSON data is stored in a string and will be processed using dictionary commands.
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''

#Processing and Output

#The line below changes the format of the data from a string to a dictionary. This allows for easier data manipulation and more access to python tools.
info = json.loads(data)

#This block of code represents the output of data. The number of users is printed, then each users data is printed.
print('User count:', len(info))
print()

#This for loop is designed to print every value in the dictionary. Keys store the value in the value pair.
for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attribute', item['x'])
    print()

#print(info[1]['name']) 
