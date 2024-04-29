from pathlib import Path


file_path = Path("../files/salary_file.txt")
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0  # Якщо у файлі 0 рядків

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Помилка, файл не знайдено!")
        return None
    except Exception as e:
        print("Сталася помилка:", e)
        return None


# Виклик функції:
total, average = total_salary(file_path)
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
