from tkinter import *
from tkinter import messagebox
import time
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def __str__(self):
       result = "Doubly Linked List: "
       current = self.head
       while current:
          result += str(current.data) + " "
          current = current.next
       return result

    def remove_chars(self, word):
        return word.replace('a', '').replace('b', '')

    def process_words(self, words):
        first_letter = words[0][0]
        current = self.head

        result = ""
        found_first_word = False
        while current:
            if not found_first_word:
                if current.data[0] != first_letter:
                    found_first_word = True
            if found_first_word and current.data[0] != first_letter:
                result += current.data + " "
            current = current.next
        return result


def process_text():
    # Блокування невірного формату даних
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Error", "Please enter some text.")
        return
    # Перевірка на обмеження в 1000 символів
    if len(text) > 1000:
        messagebox.showerror("Error", "Text should not exceed 1000 characters.")
        return
    if not all(word.islower() for word in text.split()):
        messagebox.showerror("ERROR", "All characters must be in  lowercase.")
        return

    allowed_chars = set("abcdefghijklmnopqrstuvwxyz ")
   # Якщо всі символи тексту є в дозволеному наборі, все в порядку
    if not all(char in allowed_chars for char in text):
        messagebox.showerror("Error", "Text contains invalid characters")
        return

    words = text.split()

    if len(words) < 2:
        messagebox.showerror("Error", "Text should contain at least two words.")
        return

    if text.strip()[-1] != '.':
        text += '.'
     # Змінюємо текст у полі введення
    entry.delete(0, END)  # Видаляємо поточний текст
    entry.insert(0, text)  # Вставляємо змінений текст

    start_time = time.time()

    text = entry.get()
    words = text.split()

    linked_list = DoublyLinkedList()

    for word in words[1:]:
        new_node_data = linked_list.remove_chars(word)
        linked_list.append(new_node_data)

    result = linked_list.process_words(words)
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, result)
    output.config(state=DISABLED)

    end_time = time.time()

    # Виведення часу виконання
    execution_time = end_time - start_time
    time_label.config(text="Execution Time: {:.6f} seconds".format(execution_time))

    memory_usage = sys.getsizeof(linked_list)
    current_node = linked_list.head
    while current_node:
        memory_usage += sys.getsizeof(current_node.data)
        memory_usage += sys.getsizeof(current_node.prev)
        memory_usage += sys.getsizeof(current_node.next)
        current_node = current_node.next

    # Виведення об'єму пам'яті
    memory_label.config(text="Memory Usage: {:.2f} bytes".format(memory_usage))

linked_list = DoublyLinkedList()
linked_list.add_element('I')
print(linked_list)
linked_list.add_element('am')
print(linked_list)
linked_list.add_element('King')
print(linked_list)
# Створюємо вікно
window = Tk()
window.title("Words Processor")

# Пояснення користувачу


# Задання операції
instruction_label = Label(window, text="This program removes words starting with the same letter as the first word,"
                                       "and also the letters 'a' and 'b' ")
instruction_label.pack(pady=5)
instruction_label = Label(window, text="Enter a text. Use only small Latin letters.")
instruction_label.pack(pady=5)
instruction_label = Label(window, text="Example: the lazy dog")
instruction_label.pack(pady=5)
instruction_label = Label(window, text="Result: lzy dog")
instruction_label.pack(pady=5)
# Поле для введення тексту
entry = Entry(window, width=70)
entry.pack(pady=10)

# Кнопка для обробки тексту
process_button = Button(window, text="Process Text", command=process_text)
process_button.pack(pady=5)

# Текстове поле для виведення результатів
output = Text(window, height=20, width=100, state=DISABLED)
output.pack(pady=10)

# Інформація про час виконання
time_label = Label(window, text="")
time_label.pack()

# Інформація про об'єм пам'яті
memory_label = Label(window, text="")
memory_label.pack()

# Пояснення при виведенні результату
result_label = Label(window, text="Words starting with a different letter from the first word:")
result_label.pack(pady=5)

# Запускаємо цикл обробки подій
window.mainloop()
