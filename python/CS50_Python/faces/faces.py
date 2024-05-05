text = input("Give Your Text Here:")
if (text.find(" :)") != -1):
    text = text.replace(" :)", " 🙂")
if (text.find(" :(") != -1):
    text = text.replace(" :(", " 🙁")
print(text)