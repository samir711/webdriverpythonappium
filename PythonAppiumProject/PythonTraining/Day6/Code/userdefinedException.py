class MyError(Exception):
    def __init__(self, data):
        self.value = data


try:
    raise MyError(2*3)
except MyError as e:
    print("My exception occurred, value : ", e)


class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.value = arg


try:
    raise NetworkError("Bad hostname")
except NetworkError as e:
    print(e)
