menu={
    "espresso":{
    "ingredients:":{
        "water":200,
        "mik":50,
        "coffee":24
    },
        "cost":1.5,

    },
"latte":{
    "ingredients:":{
        "water":50,
        "coffee":18,
    },
        "cost":2.5,
    },
"caapuccino":{
    "ingredients:":{
        "water":50,
        "milk":150,
        "coffee":24,
    },
        "cost":3.0,
    },
}
resources={
    "water":300,
    "milk":200,
    "coffee":100,
}
def is_suff(order_ingredients):
    """If resources are sufficient or not"""
    for key in order_ingredients:
        if(order_ingredients[key]>=resources[key]):
            print(f"Sorry there is not enough {key} ")
            return False
    return True

def is_transaction_successful(money_received,drink_cost):
    if(money_received>=drink_cost):
        return True
    else:
        return False








def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    total=int(input("how many quarters?:"))*0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total




is_on=True
money=0
while is_on:
    choice=input("What would you like?(espresso/latte/caapuccino")
    if choice=="off":
        is_on=False

    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:Rs{money}")
    else:
        drink=menu[choice]
        if is_suff(drink["ingredients:"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                money+=drink["cost"]
                balance=round(payment-drink["cost"],2)
                print(f"Here is your {choice}\n Change={balance}")

            else:
                print("You do not have sufficient money. Money is refunded")












