#To open this file, we can use the open() function.

file1 = open("D:/Program Files/advanced python/file operations/data.txt")

#reading the contents of 'file1'
#read_data= file1.read()
#print(read_data)

file2=open("D:/Program Files/advanced python/file operations/data.txt","w")
file2.write("Kolhapur")
           

file1.close()
print("File closed")




