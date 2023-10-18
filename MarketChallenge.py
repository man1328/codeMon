import random


def MarketChallange(total, options):
    sum = int(total)
    lst = []
    while sum > 0:
        affordable_items = [item for item, price in options.items() if price <= sum]
        if not affordable_items:
            break

        item = random.choice(affordable_items)
        price = options[item]
        sum -= price
        lst.append(item)

    if not lst:  
        print("No items can be purchased with the given total.")
    else:
        formatted = ", ".join(lst)
        if sum > 0:
            print(f'{formatted}, {sum} Solocoins')
        else:
            print(formatted)


options = {"Vegetable": 5, "Fruit": 10, "Bread": 15, "Candy": 20, "Meat": 25, "Toy": 30, "Blanket": 30}

MarketChallange(int(input("Enter #: ")), options)
