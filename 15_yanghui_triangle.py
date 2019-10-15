"""
    杨辉三角，也称作帕斯卡三角。是一个无限堆成的数字金字塔。
    塔侧边为1，每一行的数字都是其上方两个数字的和(左上和右上)
"""
print('Enter the number of lines to print: ', end='')
row = int(input())
yh_arr = [[1], [1, 1]]
if 1 <= row <3:
    yh_arr = yh_arr[: row]
else:
    # walkthrough line by line 
    for i in range(2, row):
        # get previous row list data
        swap = yh_arr[i - 1]
        # define a list with the first element being 1
        arr =[1]
        # add a value from the second element
        for j in range(i - 1):
            # top left ,top right
            arr.append(swap[j] + swap[j + 1])
        # add the last element 1
        arr.append(1)
        yh_arr.append(arr)
        
[print(i) for i in yh_arr]

# fill [0]
print('Enter the number of lines to print: ', end='')
row = int(input())
if row < 1:
    print('incorrect input,please re-enter')
# initialize yh_arr,only store the elements of the first row
yh_arr = [[1]]
for i in range(1, row):
    # fill [0] to the previous line list
    #print('i: ', i)
    #print('yh_arr: ',yh_arr)
    swap = yh_arr[-1] + [0]
    #print('yh_arr[-1]: ', yh_arr[-1])
    #print('swap: ', swap)
    arr = [1]
    for j in range(len(swap)-1):
        #print('j: ',j)
        #print('swap[j]: ',swap[j])
        #print('swap[j+1]: ',swap[j+1])
        arr.append(swap[j] + swap[j + 1])
        #print('arr: ', arr)
    yh_arr.append(arr)

[print(i) for i in yh_arr]
