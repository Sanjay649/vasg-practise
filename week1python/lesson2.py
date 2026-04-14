print("Hello, World!")
import json
student = {
    "id": 1,
    "name": "Ravi",
    "age": 15
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)



