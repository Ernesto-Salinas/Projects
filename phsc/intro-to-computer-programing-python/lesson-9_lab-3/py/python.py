class Error(Exception):
    def __init__(self, message):
        self.message = message

Error1 = Error("An Exception has occurred")

print(Error1.message)