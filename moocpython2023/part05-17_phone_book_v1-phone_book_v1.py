# Write your solution here

phone_book = {}
command = 0
while command != 3:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    # add phone number in phone book
    if command == 1:
        name = input("name: ")
        if name not in phone_book:
            print("no number")
        else:
            print(phone_book[name])
    elif command == 2:
        name = input("name: ")
        phone = input("number: ")
        phone_book[name] = phone
        print("ok!")
    elif command == 3:
        print("quitting...")