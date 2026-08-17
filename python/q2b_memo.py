#start from [1] , create 1001 arrays , 1<=N<=1000
store = [0] * 1001
#Fib(1)=1,Fib(2)=1
store[1] = 1
store[2] = 1

def Fib(N):
    #N >= 1
    if N < 0:
        return 0
        
    if store[N] != 0:
        return store[N]
        
    if N < 0 or N > 1001:
        print("error")
    #store = calculated
    store[N] = Fib(N - 1) + Fib(N - 2)
    return store[N]

#main 
def main():
    
    #input start and end
    A = int(input("Enter the start of the series (A): "))
    B = int(input("Enter the end of the series (B): "))

    #loop range
    for n in range(A,B+1):
        print(f"{n}   {Fib(n)}")

    
if __name__ == "__main__":
    main()
