while True:
    number = input("Enter number: ")

    try:
        if len(number) != 10:
            print ("Enter 10 digits\n")
        break

    except ValueError:
        print ("Enter only numbers\n")
        exit()

    else: 
        break


    # -----------------------------------------------