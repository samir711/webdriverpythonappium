a=10
b=0
try:
    print(a/b)
except:
    print("error")
else:
    print("no error")
finally:
    print("will always execute")