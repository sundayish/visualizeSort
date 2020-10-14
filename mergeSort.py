import time

def mergeSort(data, drawData, timeTick):
    mergeSortAlgo(data, 0, len(data)-1, drawData, timeTick)

def mergeSortAlgo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left+right) // 2

        #recursion
        #left
        mergeSortAlgo(data, left, middle, drawData, timeTick)
        #right
        mergeSortAlgo(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    #visualize
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle +1 ]
    rightPart = data[middle + 1: right + 1]

    leftIndex = rightIndex = 0

    for dataIndex in range(left, right + 1):
        if leftIndex < len(leftPart) and rightIndex < len(rightPart):
            if leftPart[leftIndex] <= rightPart[rightIndex]:
                data[dataIndex] = leftPart[leftIndex]
                leftIndex += 1
            else:
                data[dataIndex] = rightPart[rightIndex]
                rightIndex += 1
        elif leftIndex < len(leftPart):
            data[dataIndex] = leftPart[leftIndex]
            leftIndex += 1
        else:
            data[dataIndex] = rightPart[rightIndex]
            rightIndex += 1
    #visualize
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray
