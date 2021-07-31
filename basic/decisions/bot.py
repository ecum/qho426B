#ask user for the direction
print("Wich direction should I paint(up,down,left or right)")
direction = input()

#Determine wich message to display 
if(direction == "up"):
  print("\nI am painting in upward direction!")
elif(direction == "down"):
  print("\nI am painting in the downward direction!")
elif(direction == "left"):
  print("\nI am painting in the leftward direction!")
elif(direction == "right"):
  print("\nI am painting in the rightward direction!")
else:
  print("\nNot sure wich direction in am painting in!") 