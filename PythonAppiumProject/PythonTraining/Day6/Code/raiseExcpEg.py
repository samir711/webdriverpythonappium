def levelF( level ): 
    if level < 1: 
        # raise Exception("Invalid level!", level)
        raise Exception("Invalid level!", level)
    else:
        print(level)


try: 
    levelF(10)
except Exception as e: 
    print(e)
    print(type(e))
else: 
    print("no error") 
