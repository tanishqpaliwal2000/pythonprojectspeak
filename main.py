import os
from gtts import gTTS

from win32com.client import Dispatch
if __name__ == '__main__':

    print("welcome to robo 3.0 created by tanishq")
    while True:
        x = input("enter what you want me to speak-->>")

        if x=="t":
            break
        else:
            tts=gTTS(text=x,lang='en')
            tts.save("file.mp3")
            os.system("start file.mp3")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
