def temp_convert(var): 
    try: 
            return int(var) 
    except Exception as e:
            print("The argument does not contain numbers\n", e.args) #print message
            print(type(e)) #print type of exception
          
            
print(temp_convert("10"));

print(temp_convert("abc")); #throws exception
