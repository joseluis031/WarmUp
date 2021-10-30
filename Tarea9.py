f = open ("flag.txt" , "w") # creating and writing to a new file
f.write ("flag file created, with this content in!")
f.close ()
f = open ("flag.txt" , "r")
print (f.read())