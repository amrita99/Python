menu=("1 for tea\n" "2 for coffee\n" "3 for milk\n")
print(menu)
choice =int(input("enter your choice"))
print(choice)
if choice>4:
    print("enter a valid number")
elif choice==1:
    print("you have selected tea")
elif choice==2:
    print("you have selected coffee")
elif choice==3:
    print("you have selected milk")
else:
    print("please select you choice")
