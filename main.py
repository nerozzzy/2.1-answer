import json
import os


def load_books():
    if os.path.exists("library.json"):
        with open("library.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_books(books):
    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def add_book(books):
    print("\nДобавление книги")
    book = {
        "title": input("Название: "),
        "author": input("Автор: "),
        "genre": input("Жанр: "),
        "year": int(input("Год: ")),
        "description": input("Описание: "),
        "is_read": False,
        "is_favorite": False
    }
    books.append(book)
    print("Книга добавлена!")


def show_books(books):
    if not books:
        print("Библиотека пуста.")
        return
    for i, book in enumerate(books):
        if book["is_read"]:
            status = "Книга прочитана"
        else:
            status = "Книга не прочитана"
        if book["is_favorite"]:
            fav = "В избранном"
        else:
            fav = ""
        print(f"{i}. {book['title']} — {book['author']} ({book['year']}) {status} , {fav}")


def delete_book(books):
    show_books(books)
    index = int(input("Введите номер книги для удаления: "))
    if 0 <= index < len(books):
        books.pop(index)
        print("Книга удалена!")
    else:
        print("Неверный номер.")


def mark_read(books):
    show_books(books)
    index = int(input("Введите номер книги: "))
    if 0 <= index < len(books):
        books[index]["is_read"] = not books[index]["is_read"]
        print("Статус обновлен!")
    else:
        print("Ошибка.")


def toggle_favorite(books):
    show_books(books)
    index = int(input("Введите номер книги: "))
    if 0 <= index < len(books):
        books[index]["is_favorite"] = not books[index]["is_favorite"]
        print("Избранное обновлено!")
    else:
        print("Ошибка.")


def search_books(books):
    keyword = input("Введите ключевое слово: ").lower()
    results = [
        b for b in books
        if keyword in b["title"].lower()
        or keyword in b["author"].lower()
        or keyword in b["description"].lower()
    ]

    print("\nРезультаты поиска:")
    show_books(results)


def filter_books(books):
    genre = input("Жанр (оставьте пустым если не важен): ").lower()
    read = input("Прочитана? (да/нет: ").lower()

    result = books

    if genre:
        result = [b for b in result if genre in b["genre"].lower()]
    if read == "да":
        result = [b for b in result if b["is_read"]]
    elif read == "нет":
        result = [b for b in result if not b["is_read"]]
    show_books(result)


def sort_books(books):
    print("Сортировка по: 1 - названию, 2 - автору, 3 - году")
    choice = input("Ваш выбор: ")
    if choice == "1":
        books.sort(key=lambda x: x["title"])
    elif choice == "2":
        books.sort(key=lambda x: x["author"])
    elif choice == "3":
        books.sort(key=lambda x: x["year"])
    print("Отсортировано!")


def show_favorites(books):
    favs = [b for b in books if b["is_favorite"]]
    print("\nИзбранные книги:")
    show_books(favs)

def main():
    books = load_books()

    while True:
        print("\nБиблиотека")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Удалить книгу")
        print("4. Отметить как прочитанную")
        print("5. Добавить/убрать из избранного")
        print("6. Поиск")
        print("7. Фильтр")
        print("8. Сортировка")
        print("9. Избранные книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            delete_book(books)
        elif choice == "4":
            mark_read(books)
        elif choice == "5":
            toggle_favorite(books)
        elif choice == "6":
            search_books(books)
        elif choice == "7":
            filter_books(books)
        elif choice == "8":
            sort_books(books)
        elif choice == "9":
            show_favorites(books)
        elif choice == "0":
            save_books(books)
            print("Данные сохранены. Выход...")
            break
        else:
            print("Неверный ввод!")


if __name__ == "__main__":
    main()