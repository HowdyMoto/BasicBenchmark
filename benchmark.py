import random
import datetime

loops =0

startTime = datetime.datetime.now()

while True:
    result = random.random() * random.random()
    # print(result)
    loops += 1
    if loops == 100000000:
        print(f"{loops:,d}" + " LOOPS DONE")
        endTime = datetime.datetime.now()
        elapsedTime = endTime - startTime
        print("Seconds to complete: " + str(elapsedTime.total_seconds() ) )
        break