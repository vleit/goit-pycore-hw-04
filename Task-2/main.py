
def get_cats_info(path):
    cats = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3: 
                print("Формат рядку неправильна")
                continue
            try:
                cat_id = parts[0]
                _name = parts[1]
                _age = parts[2]

                cat = {"id": cat_id, "name": _name, "age": _age}
                cats.append(cat)
            except ValueError:
                continue 
    return cats

print(get_cats_info("Task-2\cats_list.txt"))