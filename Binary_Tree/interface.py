import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from Trees.functions import build_tree_from_file, search_word_in_file


def search_word():
    word = word_entry.get()

    start_time = time.time()
    found_in_tree = tree.find(word) is not None
    end_time = time.time()
    tree_search_time = end_time - start_time

    start_time = time.time()
    found_in_file = search_word_in_file(filename, word)
    end_time = time.time()
    file_search_time = end_time - start_time

    result_text = f'Слово знайдено в дереві: {found_in_tree}\nСлово знайдено в файлі: {found_in_file}'
    time_text = f'Час пошуку в дереві: {tree_search_time} секунд\nЧас пошуку в файлі: {file_search_time} секунд'

    messagebox.showinfo("Результат пошуку", result_text)
    time_label.config(text=time_text)


filename = 'functions.py'
word_to_search = 'your_word'

tree = build_tree_from_file(filename)
found_in_tree = tree.find(word_to_search) is not None
found_in_file = search_word_in_file(filename, word_to_search)

print(f'Word found in tree: {found_in_tree}')
print(f'Word found in file: {found_in_file}')


# Ваш код для класів Node, BinaryTree та функцій build_tree_from_file, search_word_in_file тут

def search_word():
    word = word_entry.get()

    start_time = time.time()
    found_in_tree = tree.find(word) is not None
    end_time = time.time()
    tree_search_time = end_time - start_time

    start_time = time.time()
    found_in_file = search_word_in_file(filename, word)
    end_time = time.time()
    file_search_time = end_time - start_time

    result_text = f'Слово знайдено в дереві: {found_in_tree}\nСлово знайдено в файлі: {found_in_file}'
    time_text = f'Час пошуку в дереві: {tree_search_time} секунд\nЧас пошуку в файлі: {file_search_time} секунд'

    messagebox.showinfo("Результат пошуку", result_text)
    time_label.config(text=time_text)
    root.update()


def delete_word():
    word = word_entry.get()
    # Ваш код для видалення слова з дерева та файлу тут
    messagebox.showinfo("Результат видалення", "Слово було видалено")


filename = 'functions.py'
tree = build_tree_from_file(filename)

root = tk.Tk()
root.title("Пошук та видалення слів")

word_label = tk.Label(root, text="Введіть слово:")
word_label.pack(pady=5)

word_entry = tk.Entry(root)
word_entry.pack(pady=5)

search_button = tk.Button(root, text="Шукати слово", command=search_word)
search_button.pack(pady=5)

delete_button = tk.Button(root, text="Видалити слово", command=delete_word)
delete_button.pack(pady=5)

output = Text(root, height=20, width=100, state=DISABLED)
output.pack(pady=10)

time_label = Label(root, text="")
time_label.pack()

root.mainloop()
