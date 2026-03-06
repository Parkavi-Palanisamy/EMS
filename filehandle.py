employees = [
    "101, Kavi, Developer",
    "102, Arun, Tester",
    "103, Priya, HR"
]
file = open("employees.txt", "w")

for emp in employees:
    file.write(emp + "\n")

file.close()
print("Employee list saved successfully")
file = open("employees.txt", "r")

for line in file:
    print(line.strip())

file.close()