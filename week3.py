def calculate_discount(price, discount_percentage):


    
    price = int(input(f"Enter the price:"))
    discount_percentage = float(input(f"Enter the discount:"))

    if discount_percentage >= 20:
        results = price * discount_percentage
        print(f"The final price is {results}")
    elif discount_percentage >= 60:
        results = print(f"Invalid discount!")

    else:
        print(f"The discount is too low. Pay: {price} ")


    



