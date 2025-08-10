write_input = input("Enter text to write to the file: ")  #takes input of what to write
with open('output.txt','w') as output_file:  #opens the file in read mode
    output_file.write(write_input)  #writes the input in file
    print("Data successfully written to output.txt.\n")

append_input = input("Enter additional text to append: ")  #takes input of what to append
with open('output.txt','a') as appended_file:  #opens file in append mode
    appended_file.write('\n'+append_input)  #appends the input
    print("Data successfully appended.\n")

print("Final content of output.txt:")  
with open('output.txt','r') as read_file:  #opens the file in read mode
    print(read_file.read())  #reads file and print it
