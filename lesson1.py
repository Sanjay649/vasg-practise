print("welcome to programming")
print("virginia")
print("sanjay")
age = 21
height = 6
name="jhon"
is_student = True

print(name)
print(age)
print(height)
print(is_student)

def clean_age(age):
    if age == "":
        return 0
    return int(age)

value = clean_age("15")
print(value)

