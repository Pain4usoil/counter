from openpyxl import Workbook

class CalorieTracker:
    def __init__(self):
        self.calories = 0
        self.meals = {}
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(["Продукт", "Калории"])

    def add_meal(self, name, calories):
        if name in self.meals:
            self.meals[name] += calories
        else:
            self.meals[name] = calories
        self.calories += calories
        self.sheet.append([name, calories])

    def display_calories(self):
        print(f"Общее количество потребленных калорий: {self.calories}")

    def display_meals(self):
        print("Список приемов пищи:")
        for meal, calories in self.meals.items():
            print(f"{meal}: {calories} калорий")

    def save_to_excel(self, filename):
        self.workbook.save(filename)


if __name__ == "__main__":
    tracker = CalorieTracker()

    while True:
        print("\nМеню:")
        print("1. Добавить продукт и калории")
        print("2. Показать общее количество калорий")
        print("3. Показать список приемов пищи")
        print("4. Сохранить данные в Excel")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите название продукта: ")
            calories = int(input("Введите количество калорий: "))
            tracker.add_meal(name, calories)
        elif choice == '2':
            tracker.display_calories()
        elif choice == '3':
            tracker.display_meals()
        elif choice == '4':
            filename = input("Введите имя файла для сохранения (с расширением .xlsx): ")
            tracker.save_to_excel(filename)
            print(f"Данные успешно сохранены в файл: {filename}")
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")
