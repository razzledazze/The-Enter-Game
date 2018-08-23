import time
import csv

def playGame():
    input()
    startTime = time.time()
    input()
    finishTime = time.time()
    timeElapsed = finishTime - startTime
    return timeElapsed

print(playGame())