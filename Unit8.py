from pprint import pprint

cook_book = {}
print("Кулинарная книга\n")
with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        name_dish = line.strip()
        quantity = int(f.readline().strip())
        pure_data = []
        for number in range(int(quantity)):
            ingredient = f.readline().strip().split(' | ')
            pure_data.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            cook_book[name_dish] = pure_data

        if not name_dish:
            continue

        f.readline()
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    void_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_list = ingridient
            new_key = new_list["ingredient_name"]
            inside = {}
            key = void_list.get(new_key)
            if key == None:
                inside["measure"] = new_list["measure"]
                inside["quantity"] = int(new_list["quantity"]) * person_count
                void_list[new_key] = inside
            else:
                void_list[new_key]["quantity"] += int(new_list["quantity"]) * person_count

    pprint(void_list)



get_shop_list_by_dishes(['Омлет','Фахитос'], 5)
print("колличество ингридиентов")