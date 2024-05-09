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

def main():
    file_name = 'C:\Users\Huawei\OneDrive\Рабочий стол\cook.txt'
    cook_book = read_recipes(file_name)
    print(cook_book)

if __name__ == '__main__':
    main()