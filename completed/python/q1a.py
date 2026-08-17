import random

#function
def genUniqueRanList(M):
    #assert M is between 1 and 100
    assert 1 <= M <= 100
        
    #create empty set for store unique number
    uni_num = set()
        
    #generate random nuber 
    while len(uni_num) < M:
        num = random.randint(1,100)
        uni_num.add(num)
    
    #convert the set to list and return
    return list(uni_num)

if __name__ == '__main__':
    print(genUniqueRanList(8))
