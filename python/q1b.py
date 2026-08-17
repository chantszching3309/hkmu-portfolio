#topping list with price
topping_list = {
    "pepperoni" : 3,
    "mushrooms" : 2,
    "onions" : 1.5,
    "olives" : 1,
    "extra Cheese" : 2.5
    }

#while loop
while True:
    total_price = 0  # initialize

    try:
        # input amount of pizza
        pizza_num = int(input("Enter number of pizzas: "))
        
        # invalid input
        if pizza_num <= 0:
            print("Value should be >=1. Please re-enter!")
            continue  # ask again
        
        # for each pizza
        for x in range(1, pizza_num + 1):
            pizza_price = 0
            topping_input = input(f"Pizza {x} toppings (comma-separated or 'none'): ")
            
            # lower case and input "none" case
            if topping_input.lower() == "none":
                print(f"Pizza {x} cost: $0.00")
                total_price += 0
                continue 
            
            #split and strip
            topping=[]
            invalid_topping=[]
            for t in topping_input.split(","):
                char = t.strip()
                char = char.lower()
                topping.append(char)
                
            #check item
            for top in topping:
                if top in topping_list:
                    pizza_price += topping_list[top]
                    print()
                else:
                    invalid_topping.append(top)
                    
            #show invalid input
            if invalid_topping !=[]:
                invalid_str=",".join(invalid_topping)
                print(f"Invalid topping(s): ['{invalid_str}']. Valid: pepperoni, mushrooms, onions, olives, extra cheese")
                    
            #show each pizza price
            print(f"Pizza {x} cost : ${pizza_price:.2f}")
        #total price
        total_price += pizza_price
        print(f"Total order cost: ${total_price:.2f}")

        #ask for process next order         
        while True:
            y_or_n = input("Process another order (y/n): ").lower()
            if y_or_n in ['y', 'n']:
                break
            print("Invalid input. Please enter 'y' or 'n'.")
        
        if y_or_n == 'n':
            print("Thank you for using Pizza Cost Calculator!")
            break
        
    except ValueError:
        print("Invalid input. Please enter a valid number!")
        continue
