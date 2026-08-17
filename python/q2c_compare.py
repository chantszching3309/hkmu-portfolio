import random
import timeit

#Regular sort
def quickSortRegular(aList):
    quickSortHelperRegular(aList , 0 , len(aList)-1)

def quickSortHelperRegular(aList, first, last):
    #at lease 2 item to compare
    if first < last:
        #middle line
        split_point = _partitionRegular(aList, first, last)
        quickSortHelperRegular(aList, first, split_point-1) #end before split_point
        quickSortHelperRegular(aList, split_point+1, last) #start after split_point

def _partitionRegular(aList, first, last):
    pivot_val = aList[first]
    
    #start
    left = first + 1
    right = last
    
    while True:
            #find left<pivot and right>pivot
            while left <= right and aList[left] <= pivot_val:
                left += 1 #move right and see next nuber when true
                
            while right >= left and aList[right] >= pivot_val:
                right -= 1 #move left and see next nuber when true
                
            #check
            if right < left:
                break
            
            else:
                aList[left], aList[right] = aList[right], aList[left]
            
    # pivot=right is in the correct position
    aList[first], aList[right] = aList[right], aList[first]
    return right
    

#random sort
def quickSortRandom(aList):
    quickSortHelperRandom(aList , 0 , len(aList)-1)

def quickSortHelperRandom(aList, first, last):
    #at lease 2 item to compare
    if first < last:
        #middle line
        split_point = _partitionRandom(aList, first, last)
        quickSortHelperRandom(aList, first, split_point-1) #end before split_point
        quickSortHelperRandom(aList, split_point+1, last) #start after split_point

def _partitionRandom(aList, first, last):
    random_index = random.randint(first,last) #random int in range
    aList[first], aList[random_index] = aList[random_index], aList[first]

    pivot_val = aList[first] #pivot replace first
    #start
    left = first + 1
    right = last
    
    while True:
            #find left<pivot and right>pivot
            while left <= right and aList[left] <= pivot_val:
                left += 1 #move right and see next nuber when true
                
            while right >= left and aList[right] >= pivot_val:
                right -= 1 #move left and see next nuber when true
                
            #check
            if right < left:
                break
            
            else:
                aList[left], aList[right] = aList[right], aList[left]
            
    # pivot=right is in the correct position
    aList[first], aList[right] = aList[right], aList[first]
    return right
    

#ascending = False , descender = True
#     small>large  ,  large>small
def quickSortreverse(aList , reverse=False): #default ascending
    quickSortHelperreverse(aList , 0 , len(aList)-1 , reverse)

def quickSortHelperreverse(aList, first, last , reverse):#default ascending by quickSort
    #at lease 2 item to compare
    if first < last:
        #middle line
        split_point = partitionreverse(aList, first, last , reverse)
        quickSortHelperreverse(aList, first, split_point-1 , reverse) #end before split_point
        quickSortHelperreverse(aList, split_point+1, last , reverse) #start after split_point

def partitionreverse(aList, first, last , reverse):#default ascending by quickSort
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
    
def compare():
    print(f"{'Size':<10} {'Regular (s)':<20} {'Randomized (s)':<20}")
    
    for size in (100,200,400,800):
        data = [random.uniform(1, 10000) for _ in range(size)]
        
        #test regular
        reg1 = timeit.timeit(
            lambda: quickSortRegular(data.copy()),
            number=1)
        
        #test random
        reg2 = timeit.timeit(
            lambda: quickSortRandom(data.copy()),
            number=1)
            
        print(f"{size:<10} {reg1:<20.6f} {reg2:<20.6f}")
    print()
    print("Reverse: ")
    print(f"{'Size':<10} {'Regular (s)':<20} {'Randomized (s)':<20}")
    for size in (100,200,400,800):
        data = [random.uniform(1, 10000) for _ in range(size)]
        #test reverse
        reg3 = timeit.timeit(
            lambda: quickSortRandom(data.copy()),
            number=1)
            
        print(f"{size:<10} {reg1:<20.6f} {reg3:<20.6f}")

if __name__ == "__main__":
    compare()
