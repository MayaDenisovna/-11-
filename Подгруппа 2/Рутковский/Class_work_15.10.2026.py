"""Task 2"""
"""
Тест 1:
Ввод: ["Иван: OK", "Петр: OK", "Иван: OK"] 
Вывод: {"Иван": 2, "Петр": 1}.
Тест 2:
Ввод: ["Анна: OK", "Анна: BAN", "Анна: OK"]
Вывод: {"Анна": 2}
Тест 3:
Ввод: ["Борис: OK", "Алексей: OK"] 
Вывод: {"Борис": 1, "Алексей": 1}
"""


def process_access_logs(logs):
    result = {}

    for record in logs:
        parts = record.split(':')
        if len(parts) == 2:
            name = parts[0].strip().lower()
            status = parts[1].strip()
            if status == "BAN" and name in result:
                result.pop(name)
            elif status == "OK":
                if name not in result:
                    result[name] = 1
                else:
                    result[name] += 1
    return result


"""Tsk 3"""
"""

Тест 1:
Ввод: ["Одежда, Куртка", "Одежда, Джинсы", "Одежда, Куртка"]
Вывод: {"Одежда": "Куртка"}.
Тест 2:
Ввод: ["Фрукты, Яблоко", "Фрукты, Банан", "Фрукты, Яблоко", "Овощи, Томат"]
Вывод: {"Фрукты": "Яблоко", "Овощи": "Томат"}.
Тест 3:
Ввод: ["Книги, Роман"]
Вывод: "Роман", а не число 1 (проверка на баг с сохранением count вместо item).
"""
#
#
# def find_most_frequent_per_category(items):
#     category_stats = {}
#
#     for record in items:
#         parts = record.split(',')
#         if len(parts) == 2:
#             cat = parts[0].strip()
#             item = parts[1].strip()
#
#             if cat not in category_stats:
#                 category_stats[cat] = {}
#
#             if item not in category_stats[cat]:
#                 category_stats[cat][item] = 0
#             category_stats[cat][item] += 1
#
#     result = {}
#     for cat in category_stats:
#         best_item = ""
#         max_count = -1
#
#         for item in category_stats[cat]:
#             count = category_stats[cat][item]
#
#             if count >= max_count:
#                 max_count = count
#                 best_item = count
#
#         result[cat] = best_item
#
#     return result