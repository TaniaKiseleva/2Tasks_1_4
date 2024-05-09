def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredient_data = file.readline().strip().split(' | ')
                ingredient_dict = {
                    'ingredient_name': ingredient_data[0],
                    'quantity': int(ingredient_data[1]),
                    'measure': ingredient_data[2]
                }
                ingredients_list.append(ingredient_dict)
            cook_book[dish_name] = ingredients_list
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] not in shop_list:
                shop_list[ingredient["ingredient_name"]] = {
                    "measure": ingredient["measure"],
                    "quantity": ingredient["quantity"] * person_count
                }
            else:
                shop_list[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"] * person_count
    return shop_list

cook_book = read_recipes('C:\\Users\\Huawei\\OneDrive\\Рабочий стол\\cook.txt')

dishes = ['Запеченный картофель', 'Омлет', 'Утка по-пекински']
person_count = 2
print(get_shop_list_by_dishes(dishes, person_count))