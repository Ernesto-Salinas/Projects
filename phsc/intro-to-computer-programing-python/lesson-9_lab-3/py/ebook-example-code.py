class Error(Exception):
    def __init__(self):
        self.message = "An exception occurred"
try:
    raise Error()
except Error as e:
    print(e.message)