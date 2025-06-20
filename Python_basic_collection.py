# -------------------------------
# 🌟 STRING AND VARIABLE BASICS
# -------------------------------

krishna = "hello"
print(krishna)

# -------------------------------
# 🔢 BASIC ARITHMETIC OPERATIONS
# -------------------------------

a = 88
b = 64
print(type(a))
print(type(b))
print("Sum (a+b):", a + b)
print("Subtraction (a-b):", a - b)
print("Multiplication (a*b):", a * b)
print("Division (a/b):", a / b)

# -------------------------------
# 📚 STRING METHODS PRACTICE
# -------------------------------

story = "a small shop, tucked away on a bustling street, sold dreams in vials. Each one, a unique experience, a whisper of a forgotten memory or a glimpse into a future yet to come"
print(type(story))
print("Length of story:", len(story))
print("Ends with 'e':", story.endswith("e"))
print("Count of 'l':", story.count("l"))
print("Capitalized:", story.capitalize())
print("Replace 'come' with 'came':", story.replace("come", "came"))

# -------------------------------
# 📋 LIST OPERATIONS
# -------------------------------

a = [43, 43, 96, 53, 11, 9]
a[0] += 3
print(a)
a[3] += 89
print(a)

l1 = [86, 32, 97, 21, 49]
l1.sort()
print("Sorted:", l1)
l1.reverse()
print("Reversed:", l1)
l1.append(1000)
l1.insert(2, 99)
print("Modified List:", l1)

# -------------------------------
# 🧮 DICTIONARIES IN PYTHON
# -------------------------------

mydict = {
    "fast": "cheetah is fastest animal",
    "singer": "my friend is singer",
    "anotherdict": ("singer", "manoj")
}
print(mydict["fast"])
print(mydict["singer"])

# Updating dictionary
mydict.update({"dancer": "is Advik"})
print("Updated dancer:", mydict.get("dancer", "Not Found"))

# -------------------------------
# ✅ SETS IN PYTHON
# -------------------------------

a = {1, 1, 2, 2, 4, 3, 6}
print("Set a:", a)

b = set()
b.add(6)
b.add(100)
b.add(99)
print("Set b after adding:", b)
b.remove(99)
print("After remove:", b)
b.pop()
print("After pop:", b)
b.clear()
print("After clear:", b)

# Set operations
a = {1, 2, 3, 4}
b = {2, 3, 9}
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))

# -------------------------------
# 🔁 LOOPS AND TABLES
# -------------------------------

i = 7
while i <= 70:
    print(i)
    i += 7

for i in range(12, 121, 12):
    print(i)

# -------------------------------
# ✅ CONDITIONALS PRACTICE
# -------------------------------

marks = int(input("Enter your marks: "))
if marks > 43:
    print("You passed with good marks!")
elif marks > 33:
    print("You are passed.")
elif marks > 30:
    print("You barely passed.")
else:
    print("You failed.")

# -------------------------------
# ✅ AGE ACCESS CONDITION
# -------------------------------

age = int(input("Enter your age: "))
if 33 < age < 50:
    print("Access Granted.")
else:
    print("Access Denied.")

# -------------------------------
# 🎯 WHILE LOOP EXAMPLES
# -------------------------------

i = 18
while i <= 50:
    print(i)
    i += 1

i = 1
while i <= 1000:
    print(i)
    i += 1

i = 0
while i <= 10:
    print("Krishna")
    i += 1

# -------------------------------
# 🍎 TUPLE LOOP EXAMPLE
# -------------------------------

fruits = ("banana", "watermelon", "mangoes", "apple")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# -------------------------------
# 💹 PROFITS & LIST SORTING
# -------------------------------

profit1 = [1000, 2000, 1100, 4000]
print("Profits:", profit1)
profit1.sort()
print("Sorted:", profit1)
profit1.reverse()
print("Reversed:", profit1)
profit1.insert(2, 1200)
profit1.append(100000)
print("Final Profit List:", profit1)

# -------------------------------
# 🏫 MPDTE DICTIONARY EXAMPLE
# -------------------------------

mydict = {
    "mpdte": "Counselling for B.Tech college",
    "aitr": "I must try to hold my seat in this college"
}
print(mydict)
print("Keys:", mydict.keys())
mydict.update({"aitr": "A college for B.Tech"})
print("Updated AITR:", mydict["aitr"])
