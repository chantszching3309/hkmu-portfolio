def isLuckySeven(pwd):
    
    #initialize
    digit_amount=0
    punct_amount=0

    # 1 between 8 and 32 characters
    if len(pwd) < 8 or len(pwd) > 32:
        return False
        
    # 2 invalid characters
    for char in pwd:
        
        if not (char.isalpha() or char.isdigit() or char in "+-*/"):
            return False
        
        #count digit   
        if char.isdigit() :
            digit_amount += 1
            
        #count punctuation
        if char in "+-*/":
           punct_amount += 1 
            
# 3 digit needs >=1
    if punct_amount < 1:
        return False


# one punctuation
    if punct_amount != 1:
        return False
            
#substring
    if "77" not in pwd:
        return False
        
    return True

if __name__=="__main__":
    test_pwd = input("请输入密码：")
    result = isLuckySeven(test_pwd)
    print(result)
