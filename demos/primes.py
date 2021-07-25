'''Create funtions that can find out if number is prime,can find a prime number with a rang of values and compute N,used in RSA encryption'''
def isPrime(number):
  for thing in range(2,number):
    if number % thing==0:
      return False
  return True 
      
print(isPrime(100))    

def findPrime(start,end):
  for stuff in range(start,end +1):
    if isPrime(stuff):
      return stuff
      
def encrypt(): 
  x= int (input("Provide an integer"))
  y=int (input("Provide an integer(larger)"))
  p1= findPrime (x,y)
  x= int (input("Provide an integer"))
  y=int (input("Provide an integer(larger)"))
  p2= findPrime(x,y)
  return p1*p2
  print(encrypt)
  

 
