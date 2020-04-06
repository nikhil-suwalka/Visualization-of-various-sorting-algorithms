import tkinter as tk
from tkinter import font
from random import randrange
import time

import sys

sys.setrecursionlimit(20000)
number = []
for i in range(160):
    number.append(randrange(0, 100000))
temp = []
for i in range(6):
    temp.append(number.copy())
number = temp

total_bubble = 0


def bubble(arr):
    global total_bubble
    bubble_start_time = time.time()
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    total_bubble += time.time() - bubble_start_time

    return arr


def insertion(arr):
    i = 0
    while (arr[i] <= arr[i + 1]):
        i += 1
        if (i >= len(arr) - 1):
            return arr

    temp = arr[i + 1]
    j = i + 1
    while (temp < arr[j - 1] and j > 0):
        arr[j] = arr[j - 1]
        j -= 1
    arr[j] = temp
    return arr


sel_index = 0


def selection(arr):
    global sel_index
    if sel_index >= len(arr):
        return arr
    mini = arr.index(min(arr[sel_index:]), sel_index)
    arr[sel_index], arr[mini] = arr[mini], arr[sel_index]
    sel_index += 1
    return arr


radix_mod = 1


def radix(arr):
    global radix_mod
    arr2 = []

    if (len(str(radix_mod)) > len(str(max(arr)))):
        return arr

    radix_mod *= 10
    for i in range(10):
        for j in range(len(arr)):
            if (int(arr[j] % radix_mod / (radix_mod / 10)) == i):
                arr2.append(arr[j])
    # arr = arr2
    for i in range(len(arr2)):
        arr[i] = arr2[i]
    return arr


shell_incr = None


def shell(arr):
    global shell_incr
    if (shell_incr is None):
        shell_incr = len(arr) // 2
    for i in range(shell_incr):
        for j in range(i, len(arr) - shell_incr):
            for k in range(i, len(arr) - shell_incr):
                if (arr[k] > arr[k + shell_incr]):
                    arr[k], arr[k + shell_incr] = arr[k + shell_incr], arr[k]
    shell_incr //= 2
    return arr


quick_passes = []

arr = number[5].copy()


def quick(start, end):
    s = start
    n = end

    pivot = start
    start += 1
    while (start <= end):
        if (arr[pivot] >= arr[start]):
            start += 1
        elif (arr[pivot] < arr[end]):
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot] = arr[pivot], arr[end]
    quick_passes.append(arr.copy())
    if (end >= s + 2):
        quick(s, end - 1)
    if (end <= n - 2):
        quick(end + 1, n)


quick(0, len(arr) - 1)
quick_count = 0
len_passes = len(quick_passes)
print("Len: ", len(quick_passes))
print(quick_passes)


def get_quick():
    global quick_count
    if (quick_count < len_passes):
        number[5] = quick_passes[quick_count].copy()
        quick_count += 1


WIDTH = 1200
HEIGHT = 600
root = tk.Tk()
w = tk.Canvas(root, width=WIDTH, height=HEIGHT)

section = []
sortingNames = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Radix Sort', 'Shell Sort', 'Quick Sort']
# Create sections
count = 0
for i in range(400, 1201, 400):
    section.append(
        [[i - 360, HEIGHT / 2 - 40], w.create_rectangle(i - 400, 0, i, HEIGHT / 2, fill='white', outline='grey'),
         w.create_line(i - 360, 0, i - 360, HEIGHT / 2 - 40, fill='black'),
         w.create_line(i - 360, HEIGHT / 2 - 40, i - 40, HEIGHT / 2 - 40, fill='black'),
         w.create_text(i - 200, 20, text=sortingNames[count], font=font.Font(family='Consolas', size=20, weight='bold'),
                       fill='black'), []])
    count += 1
    section.append(
        [[i - 360, HEIGHT - 40], w.create_rectangle(i - 400, HEIGHT / 2, i, HEIGHT, fill='white', outline='grey'),
         w.create_line(i - 360, HEIGHT / 2, i - 360, HEIGHT - 40, fill='black'),
         w.create_line(i - 360, HEIGHT - 40, i - 40, HEIGHT - 40, fill='black'),
         w.create_text(i - 200, HEIGHT / 2 + 20, text=sortingNames[count],
                       font=font.Font(family='Consolas', size=20, weight='bold'), fill='black'), []])
    count += 1
    pass
w.create_line(0, HEIGHT / 2, 1200, HEIGHT / 2, fill='grey')
w.pack()

# Create sort names


# number = [int(i) for i in input().split()]

# number.append(randrange(0, 1000))
# number = [19, 79, 19, 63, 63, 95, 39, 59, 63, 72]
print(number)
rank_number = []


# number = [[1, 2, 3, 4, 5], [7, 2, 3, 4, 5], [1, 2, 99, 4, 5], [1, 2, 3, 40, 5], [100, 2, 3, 4, 5], [1, 200, 3, 4, 5]]
def findRank(n):
    rank = []
    for i in range(0, len(n)):
        rank.append([sorted(n).index(n[i]) + 1, n[i]])
    return rank


def printGraph(number):
    rank_number.clear()
    for num in number:
        rank_number.append(findRank(num))
        # print(findRank(num))

    # create bar rectangles
    for sec in range(len(section)):
        size = 2
        # wrong need to change instead of multiple loops num needs to change
        for num in rank_number[sec]:
            section[sec][5].append(
                w.create_rectangle(section[sec][0][0] + size, section[sec][0][1], section[sec][0][0] + size + 2,
                                   section[sec][0][1] - num[0] * 1, fill='black', outline='white'))
            size += 2
        # print(rank_number[sec])


sortedArray = sorted(number[0])
while True:
    w.after(100, printGraph(number))
    # print(number)
    root.update()

    if (number[0] != sortedArray):
        bubble(number[0])
    # print("Bubble: ", total_bubble)

    insertion(number[1])
    selection(number[2])
    radix(number[3])
    shell(number[4])
    get_quick()

    # print(section)
    for i in section:
        for j in i[5]:
            w.delete(j)
        i[5] = []
