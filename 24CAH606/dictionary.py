d = {}
while True:
    try:
        c = int(input("Press 1 to continue and 2 to exit: "))
        
        if c == 1:
            i = input("Enter the user ID: ")
            if i in d:
                print("ID already exists.")
            else:
                name = input("Enter the name: ")
                age = int(input("Enter the age: "))
                d[i] = {"name": name, "age": age}
        
        elif c == 2:
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

uid = input("Enter the user ID to print details: ")
if uid in d:
    print(f"User details for ID {uid}:")
    print(f"Name: {d[uid]['name']}")
    print(f"Age: {d[uid]['age']}")
else:
    print("User ID not found.")