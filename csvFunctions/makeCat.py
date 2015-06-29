catList = {
    'Milk 1l': 'shortLife',
    'Imasi': 'shortLife',
    'Bread': 'shortLife',
    'Chakalaka Can': 'cannedGoods',
    'Gold Dish Vegetable Curry Can': 'cannedGoods',
    'Fanta 500ml': 'cooldrinks',
    'Coke 500ml': 'cooldrinks',
    'Cream Soda 500ml': 'cooldrinks',
    'Iwisa Pap 5kg': 'longLife',
    'Top Class Soy Mince': 'longLife',
    'Shampoo 1 litre': 'toiletries',
    'Soap Bar': 'toiletries',
    'Bananas - loose': 'fruit',
    'Apples - loose': 'fruit',
    'Mixed Sweets 5s': 'sweets',
    'Heart Chocolates': 'sweets',
    'Rose (plastic)': 'gifts',
    'Valentine Cards': 'gifts'
}

def makeCat(itemMap):

    catMap = {};

    for itemName in itemMap:
        if not catMap[catList[itemName]]:
            catMap[catList[itemName]] = []
        
        catMap[catList[itemName]].update({"product": itemName, "qty": itemMap[itemName]})    
    return catMap;
