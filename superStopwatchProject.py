import time
import os
#! python 3
# stopwatch.py - a simple stopwatch program.

#Display the program's instructiosn.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

#start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum+=1
        lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
    #handle the ctrl-c exception to keep its error message from displaying.
    print('\nDone.')