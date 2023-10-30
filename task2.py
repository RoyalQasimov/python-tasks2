my_dict = {}

while True:
    print("1 - Enter Key")
    print("2 - Enter Value")
    print("e - Exit")

    a = input("Enter your choice: ")

    if a == "1":
        key = input("Enter key: ")
       
        my_dict[key] = None
    elif a == "2":
        key = input("Enter the key for which you want to set a value: ")
        if key in my_dict:
            value = input("Enter the value: ")
    
            my_dict[key] = value
        else:
            print("Key not found in the dictionary. Please enter a key first.")
    elif a.lower() == "e":
        break
    else:
        print("Invalid choice. Please select 1, 2, or e.")


print("Final Dictionary:")
print(my_dict)
