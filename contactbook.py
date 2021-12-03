names = []
phone_numbers=[]
num=3
for i in range(num):
   name = input("Name: ")
   phone_number = input("phone number:")
   names.append(name)
   phone_numbers.append(phone_number)
print("\n Name\t\t phone Number \n")


for i in range(num):
    print("{}\t\t\t{}" .format(names[i],phone_numbers[i]))
search_term = input("\n Enter search name :")
print("search result")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name {},phone number :{}".format(search_term,phone_number))
else:
    print("Name not found")
