try:
    with open("sample.txt", 'r') as file_read:
        line_number = 1     #It's the number on which line we are.
        print("Reading file content:")      
        # We are supposing that /n means different/new line and not by fullstop(.)
        for i in file_read.readlines():     #runs a for loop in file_read where i is each elements of string
            print("Line{}: {}".format(line_number,i))       #Prints the requried set of info
            line_number += 1        #increased the number of line by 1
except Exception:
    print("The file 'sample.txt' was not found.")
