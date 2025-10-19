
def total_salary(path):
    try:
        with open(path, "r") as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, salary_str = line.split(",")
                    salary = float(salary_str)
                    total += salary
                    count += 1
                except ValueError:
                    print("Помилка в рядку")
                    return 0
            if count == 0:
                print("В файлі немає жодної зарплати")
                return 0
            average = total/count
            return total,average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0


print(total_salary('Task-1\salary_list.txt'))
