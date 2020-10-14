from tkinter import *
from tkinter import ttk
import random
from visualizeSort.bubbleSort import bubbleSort

root = Tk()
root.title("Sorting Visualisation")
root.maxsize(900, 600)
root.config(bg="grey")

# vars
selAlg = StringVar()
data = []

# functions
def drawData(data, colorArray):
    canvas.delete("all")
    canvasHeight = 380
    canvasWidth = 600
    xWidth = canvasWidth / (len(data) + 1)
    offset = 5
    spacing = 5

    # normalize data
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * xWidth + offset + spacing
        y0 = canvasHeight - height * 340
        # bottom right
        x1 = (i + 1) * xWidth + offset
        y1 = canvasHeight
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    root.update()

def generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ["red" for x in range(len(data))])


def startAlgorithm():
    global data
    bubbleSort(data, drawData, speedScale.get())


# frame
UI_frame = Frame(root, width=600, height=200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selAlg, values=["Bubble-Sort", "Merge-Sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                   label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=startAlgorithm, bg="red").grid(row=0, column=3, padx=5, pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=30, resolution=1, orient=HORIZONTAL, label="Data size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min. value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max. value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=generate, bg="white").grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
