def expo(x, y, e) : 
    res = 1
    x = x % e  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % e
        y = y >> 1      
        x = (x * x) % e
    return res   
x = 3; y = 6; e = 14
print("Expo is ", expo(x, y, e))
