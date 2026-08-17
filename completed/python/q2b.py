def Fib(N):
    
    #Fib(1)=1,Fib(2)=1
    if N == 1 or N==2:
        return 1
        
    else:
        return Fib(N - 1) + Fib(N - 2)

        
def main():
    
    #input start and end
    A = int(input("Enter the start of the series (A): "))
    B = int(input("Enter the end of the series (B): "))

    #loop range
    for n in range(A,B+1):
        print(f"{n}   {Fib(n)}")

    
if __name__ == "__main__":
    main()
