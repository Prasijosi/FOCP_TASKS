#Values already defined inside the function mentioning here for viewers
pizza_price = 12
delivery_cost_threshold = 5
delivery_cost = 2.5
tuesday_discount = 0.5
app_discount = 0.75

def BPP_Pizza_Calc():
    
    print("******************************")
    print("******************************")
    print("WELCOME TO BECKETT PLAZE PIZZA")
    print("******************************")
    print("******************************")

# Loop until valid input
    while True:  
        try:
            num_of_pizzas = int(input("How many pizzas ordered? "))
            if num_of_pizzas > 0:
                # Exits after valid input
                break 
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Invalid input. Please enter a number!")
            
    while True: 
        wants_delivery = input("Is delivery required? ").lower()
        if wants_delivery in ("y", "n"):
            break 
        else:
            print("Invalid input.Please answer 'y' or 'n'.")

    while True:
        happy_tuesday = input("Is it Tuesday? ").lower() 
        if happy_tuesday in ("y","n"):
            break
        else:
            print("Invalid input.Please answer 'y' or 'n'.")

    while True: 
        used_app = input("Did the customer use the app? ").lower()
        if used_app in ("y","n"):
            break 
        else:
            print("Invalid input.Please answer 'y' or 'n'.")

#calculating the total price of pizza
    pizza_price = num_of_pizzas * 12
    
#in cases where one orders more than 5 pizza they get free delivery
    delivery_cost = 2.5 if wants_delivery and num_of_pizzas < 5 else 0
    total_price = pizza_price + delivery_cost

#For Tuesday Discount
    if happy_tuesday:
        total_price *=tuesday_discount
    
#Discount for using BPP app
    if used_app:
        total_price *= app_discount

    total_price = round(total_price, 2)
    print(f"Total Price: £{total_price}.")

BPP_Pizza_Calc()