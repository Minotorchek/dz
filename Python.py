import encodings


with open('data.txt', 'a+', encoding='utf-8') as f:
    f.seek(0)
    cook_book = {}

    for line in f:
        recipe = []
        dish = line.strip()
        quantity = int(f.readline().strip())
        for line in range(quantity):
            line_recipe = f.readline().split(' | ')
            recipe.append({'ingredient_name': line_recipe[0], 'quantity': int(line_recipe[1]), 'measure': line_recipe[2].strip()})
            cook_book[dish] = recipe
        f.readline()

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    for i in dishes:
        for a, b in cook_book.items():
            if i == a:
                for c in b:
                    recipe = {}
                    d = c['quantity']*person_count
                    recipe[c['ingredient_name']] = {'measure': c['measure'], 'quantity': d}
                    print(recipe)
            else:
                continue
    return
get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)



