def euclide(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 
a = 120
b= 38 
print ("The gcd of 120 and 38 is") 
print (euclide(120,38))
