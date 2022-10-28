with open('filename', 'r') as f_one:
    with open('filename', 'r') as f_two:
        if f_one.read() == f_two.read():
            print(True)
        else: 
            print(False)

        

    

