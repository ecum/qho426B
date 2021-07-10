print("Program Started !")
a2 = abs(int(input (" Please enter an ASCII code:")))
if a2  in  range(32,127):
  print("The character represented by the ASCII code {} is {}".format(a2, chr(a2)))
else:
   print("This is an error!Invalid number code")
print("Program has ended!")

