import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data [tail]

    drawData(data, getColorArray(len(data), head, tail, border, border, False))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            #draw
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border +=1
        
        drawData(data, getColorArray(len(data), head, tail, border, j, False))
        time.sleep(timeTick)

    #Swap pivot with border
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)        
    data[border], data[tail] = data[tail], data[border]     
    return border       

def quickSort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIndex = partition(data, head, tail, drawData, timeTick)

        #left partition
        quickSort(data, head, partitionIndex - 1, drawData, timeTick)

        #right partition
        quickSort(data, partitionIndex + 1, tail, drawData, timeTick)

def getColorArray(dataLength, head, tail, border, currentIndex, isSwapping):
    colorArray = []
    for i in range(dataLength):
        if i >= head and i <= tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i == tail:
            colorArray[i] = "blue"
        elif i == tail:    
            colorArray[i] = "red"
        elif i == currentIndex:
            colorArray[i] = "yellow"
        
        if isSwapping:
            if i == border or i == currentIndex:
               colorArray[i] = "green"
    return colorArray