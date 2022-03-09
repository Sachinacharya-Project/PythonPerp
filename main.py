# Encoded Message System
import os


class MessageManager:
    def ConvertEncoding (self, message="", increments=10):
        """
        This will convert the passed message into encoded format
        required parameters:
            message(default):
                Messages that is to be encoded (string)
            increments(default: 10)
                Hash encoding for the message (int)
        """
        return [bin(ord(x) + increments) for x in message]
    def ConvertDecoding (self, messages="", increments = 10):
        """
        This will Decode your encoded message
        required parameters:
            message(default):
                Messages that is to be encoded (string)
            increments(default: 10)
                Hash encoding for the message (int)
        """
        msg = ''
        messages = messages.replace("['", '')
        messages = messages.replace("]", '')
        messages = messages.replace("'", '')
        messages = messages.split(',')
        for message in list(messages):
            msg += chr(int(message, 2) - increments)
        return msg
if __name__ == '__main__':
    messageCoder = MessageManager()
    while True:
        print("""Choose Operation
              1. Encode Message
              2. Decode Message
              3. Clear Screen
              4. Exit
              """)
        opt = input("option: ")
        if opt.isdigit():
            if int(opt) == 1:
                # Keeping Hash 10
                msg = messageCoder.ConvertEncoding(message=input("Messages: "))
                print("\n")
                print(msg)
                print("\n")
            elif int(opt) == 2:
                msg = messageCoder.ConvertDecoding(messages=input("Encoded Message: "))
                print("\n")
                print(msg)
                print("\n")
            elif int(opt) == 3:
                os.system('cls')
            elif int(opt) == 4:
                exit()
            else:
                print("Invalid Option choosen")
        else:
            print("Invalid Option choosen")