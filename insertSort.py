import time

def insertSort(data, drawData, timeTick):
    for i in range(1, len(data)):
        currentValue = data[i]
        currentPosition = i

        while currentPosition > 0 and data[currentPosition - 1] > currentValue:
            data[currentPosition] = data[currentPosition - 1]  
            currentPosition = currentPosition - 1
            drawData(data, ["green" if x == i else "red" for x in range(len(data))])
            time.sleep(timeTick)
        
        data[currentPosition] = currentValue
