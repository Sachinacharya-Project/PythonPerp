# Encoded Message System

def ConvertEncoding (message="", increments=10):
    "This will convert the passed message into encoded format"
    return [bin(ord(x) + increments) for x in message]

print(ConverterEncoding(message="Hello  World"))