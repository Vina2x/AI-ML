info= [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
# courses_set= set()
# for tup in info:
#     courses_set.add(tup[1])

# print(courses_set)

courses_set= set()
for name,courses in info:
    courses_set.add(courses)

print(courses_set)