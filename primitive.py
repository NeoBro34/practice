print("===== number =====")
# in JAVA, variable is a name storage location!
# in Python, variable is named referance!

count = 100
count_type = type(count)
# buyerda (f) nodeJsdagi (``) super string bilan bir xil vazifada
print(f"the count: {count} and type: {count_type}")

# (Pythonda xamma narsa objectdir xox u number bo'lsin xox u string bo'lsin!) !!! STATE hamda METHODlariga egadir!

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("===== string =====")
# . METHODS: upper() lower() title() find() replace()


course = "AI Python FullStack"

result = type(course)
print(f"the result(1): {result}")
# the result(1): <class 'str'>

result = course.title()
print(f"the result(2): {result}")
# the result(2): Ai Python Fullstack

result = course.upper()
print(f"the result(3):  {result}")
# the result(3):  AI PYTHON FULLSTACK

result = course.replace("FullStack", "MasterClass")
print(f"the result(4):  {result}")
# the result(4):  AI Python MasterClass
