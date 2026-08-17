def find_e(N):
    
    #(summation series)N is positive and >=1
    if N == 1:
       return 1
    
    def factorial(n):
        #1! = 1
        if N == 1:
            return 1
        #n! = n(n-1)
        return n* factorial(n-1)
        
    #N-1 +N , N = 1/N
    return find_e(N-1) + 1/factorial(N)
