from colored import stylize
from colored import fg
import os
import time

#print(stylize("Hallo!", fg(256)))

i = 0
while i < 250000:
    os.system("clear")
    s = ""
    j = 0
    while j <= i:
        s += stylize("karbonaterol", fg(j % 256))
        j += 1
    print(s)
    time.sleep(®)