from tkinter import *
import random
import time
win = Tk()

win.geometry('800x600')
win.title('Sorting Visualizer')

win.config(bg = 'silver')


data = []


    
        
def array_generated(array, colorarray):
    canva.delete('all')
    canva_width = 800
    canva_height = 550
    bar_width = canva_width/(len(array))
    normalizing = [i/max(array) for i in array]
    for i, height in enumerate(normalizing):
        x1 = i*bar_width+10
        y1 = canva_height - height*500
        x2 = (i+1)*bar_width+10
        y2 = canva_height
        canva.create_rectangle(x1,y1, x2, y2, fill = colorarray[i])
    win.update_idletasks()

def generate():
    global data
    data.clear()
    size = int(e.get())

    for i in range(size):
        data.append( random.randrange(10, 50+size))
    array_generated(data, ['blue' for x in range(len(data))])



def insertionsort(data, array_generated):
    for i in range(1, len(data)):
        k = data[i]
        j = i-1
        while j>=0 and k<data[j]:
            data[j+1] = data[j]
            j -=1
        data[j+1] = k
        array_generated(data, ['purple' if x == j+1 or x ==i-1 else 'blue' for x in range(len(data))])
        time.sleep(0.2)
    array_generated(data, ['yellow' for x in range(len(data))])
def bubblesort(data, array_generated):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] >data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                array_generated(data, ['purple' if x==j or x ==j+1 else 'blue' for x in range(len(data))])
                time.sleep(0.1)
    array_generated(data ,['yellow' for x in range(len(data))])

def mergesort(array, array_generated):
    mergesortalgo(array, 0, len(data)-1, array_generated)

def mergesortalgo(array, left, right, array_generated):
    if left<right:
        middle = (left+right)//2
        mergesortalgo(array, left, middle, array_generated)
        mergesortalgo(array, middle, right , array_generated)
        merge(array, left, middle, right, array_generated)
def merge(array, left, middle, right, array_generated):
    array_generated(array, getcolorarray(len(array), left, middle, right))
    time.sleep(0.2)
    l = array[left: middle]
    r = array[middle:right]
    i= j =0
    for k in range(left, right+1):
        if i<len(l) and j<len(r):
            if l[i]<= r[j]:
                array[k] = l[i]
                i+=1
            else:
                array[k] = r[j]
                j+=1
        elif i<len(l):
            array[k] = l[i]
            i+=1
        else:
            array[k] = r[j]
            j+=1
    array_generated(array, ['green' if x>=left and x<= right else 'white' for x in range(len(array))])
    time.sleep(0,2)

def getcolorarray(length, left, middle, right):
    color = []
    for i in range(length):
        if i>=left and i<= right:
            if i<=middle:
                color.append('orange')
            else:
                color.append('yellow')

        else:
            color.append('white')
        
        
    
            
def startalgorithm():
    global data
    global algorithm
    if algorithm.get() == 'BubbleSort':
        bubblesort(data, array_generated)
    if algorithm.get() == 'InsertionSort':
        insertionsort(data,array_generated)
    
    
        
    
    

frame = Frame(win, width = 800, height = 200, bg = 'silver')
frame.grid(row = 0, column = 0)
canva = Canvas(win, width = 800, height = 550, bg = 'light pink')
canva.grid(row = 1, column = 0)
algorithm = StringVar()
algorithm.set('BubbleSort')
Label(frame, text = 'Sorting Algorithm', bg= 'silver', borderwidth = 5).grid(row = 0, column = 0, padx = 5, pady =5, sticky = W)
OptionMenu(frame, algorithm,'InsertionSort', 'BubbleSort').grid(row =0 , column = 1)
Button(frame, text = 'Generate', bg = 'green', fg  = 'white', borderwidth = 5, command = generate).grid(row = 0, column = 5)
Label(frame, text = 'Size of array :', bg = 'silver', borderwidth = 10).grid(row = 0, column = 2)
e = Entry(frame, width = 30)
e.grid(row = 0, column = 4, sticky = W)
Button(frame, text = 'Start', bg = 'red', fg = 'white',width = 7, borderwidth = 5, command = startalgorithm).grid(row = 0, column = 6)
win.mainloop()
