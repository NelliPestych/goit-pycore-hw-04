from pathlib import Path


cats_file_path = Path("../files/cats_file.txt")
def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print("Помилка, файл не знайдено!")
        return None
    except Exception as e:
        print("Сталася помилка:", e)
        return None


# Виклик функції:
cats_info = get_cats_info(cats_file_path)
if cats_info is not None:
    print(cats_info)
