import random

#ascending = False , descender = True
#     small>large  ,  large>small
def quickSort(aList , reverse=False): #default ascending
    quickSortHelper(aList , 0 , len(aList)-1 , reverse)

def quickSortHelper(aList, first, last , reverse):#default ascending by quickSort
    #at lease 2 item to compare
    if first < last:
        #middle line
        split_point = partition(aList, first, last , reverse)
        quickSortHelper(aList, first, split_point-1 , reverse) #end before split_point
        quickSortHelper(aList, split_point+1, last , reverse) #start after split_point

def partition(aList, first, last , reverse):#default ascending by quickSort
    pivot_val = aList[first] #base value = first number of list
    #start
    left = first + 1
    right = last
    
    while True:
        if not reverse:
            #ascending order ,find left<pivot and right>pivot
            while left <= right and aList[left] <= pivot_val:
                left += 1 #move right and see next nuber when true
                
            while right >= left and aList[right] >= pivot_val:
                right -= 1 #move left and see next nuber when true
                
        else:
            #descender order, find left>pivot and right<pivot
            while left <= right and aList[left] >= pivot_val:
                left += 1
            while right >= left and aList[right] <= pivot_val:
                right -= 1
                
        #check
        if right < left:
            break
        else:
            aList[left], aList[right] = aList[right], aList[left]
            
    # pivot=right is in the correct position
    aList[first], aList[right] = aList[right], aList[first]
    return right
            
if __name__ == '__main__':
    aList = []
    for i in range(20):
        aList.append(random.randint(1,100))
    print(aList)
    quickSort(aList)
    print(aList)
