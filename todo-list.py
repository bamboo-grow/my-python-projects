todos = []

def show_tasks():
    if len(todos) == 0:
        print("📭 У вас нет задач!")
    else:
        print("\n📋 ВАШИ ЗАДАЧИ:")
        for номер, задача in enumerate(todos, 1):
            print(f"  {номер}. {задача}")

def add_task():
    новая_задача = input("📝 Введите новую задачу: ")
    if новая_задача.strip():  # Проверка на пустой ввод
        todos.append(новая_задача)
        print(f"✅ Задача '{новая_задача}' добавлена!")
    else:
        print("❌ Вы ничего не ввели!")

def delete_task():
    if len(todos) == 0:
        print("❌ Нет задач для удаления!")
        return
    
    show_tasks()
    
    try:
        номер_удаления = int(input("🔢 Введите НОМЕР задачи для удаления: "))
        if 1 <= номер_удаления <= len(todos):
            удаленная_задача = todos.pop(номер_удаления - 1)
            print(f"🗑️ Задача '{удаленная_задача}' удалена!")
        else:
            print("❌ Такого номера нет!")
    except ValueError:
        print("❌ Нужно ввести ЧИСЛО!")

# Основной цикл
while True:
    print("\n" + "=" * 40)
    print("📌 МОЙ СПИСОК ДЕЛ")
    print("=" * 40)
    print("\nЧто хотите сделать?")
    print("[1] - Показать все задачи")
    print("[2] - Добавить задачу")
    print("[3] - Удалить задачу")
    print("[4] - Выйти")

    выбор = input("👉 Введите номер (1-4): ").strip()

    # Обратите внимание на кавычки!
    if выбор == "1":
        show_tasks()
    elif выбор == "2":
        add_task()
    elif выбор == "3":
        delete_task()
    elif выбор == "4":
        print("До свидания!")
        break
    else:
        print("❌ Неверный выбор! Попробуйте снова.")


    
    