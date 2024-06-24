from random import choice
import time

choices = ["zevel","airon","jed","shams","ace","aldrain","jhoren","alvin"]

for i in range(1,3):
    print(i)
    time.sleep(i)
print(choice(choices))