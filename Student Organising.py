import keyword        # Checking for keyword
import builtins       # Checking for functions
import string         # Checking for symbols
import abc            # For abstract classes
import json           # For password management
import pathlib        # For password management too 
file_path = pathlib.Path("Encryp.json")

class Organisation(abc.ABC):
    schl = "SCHOOL"
    names = []


class Student(Organisation):
    def __init__(self, name, grade, roll_no, admn_no):
        self.name = name
        self.grade = grade
        self.roll_no = roll_no
        self.admn_no = admn_no

        Organisation.names.append(self.name)
        self.details = dict(zip(
            ("Name", "Grade", "Roll no", "Admn no"),
            (self.name, self.grade, self.roll_no, self.admn_no)
        ))


# ---------- LOGIN / JSON PART ----------

try:
    with open("Encryp.json", "r") as UP:
        Encryp = json.load(UP)
except FileNotFoundError:
    Encryp = {}
    with open("Encryp.json", "w") as UP:
        json.dump(Encryp, UP)

if not Encryp.get("Usr"):
    Encryp["Usr"] = input("Enter your User Name: ")
    Encryp["Pas"] = input("Enter the Password: ")
    with open("Encryp.json", "w") as UP:
        json.dump(Encryp, UP)


while True:
    User_Check = input("Enter your UserName (0 to reset): ")
    Pass_Check = input("Enter your Password (0 to reset): ")

    #  RESET OPTION
    if User_Check == "0" and Pass_Check == "0":
        if file_path.exists():
            file_path.unlink()
            print("Login data deleted. Program will exit.")
        else:
            print("No login file found.")
        exit()

    #  NORMAL LOGIN
    if User_Check == Encryp.get("Usr") and Pass_Check == Encryp.get("Pas"):
        break
    else:
        print("Incorrect Password")
        print("== Try Again ==")
        
# ---------- ORGANISATION ----------

Organisation.schl = input("Enter your Organisation: ")


# ---------- STUDENT INPUT ----------

while True:
    try:
        totl = int(input("Enter how many students you want to upload: "))
        if totl >= 1:
            break
        else:
            print("Use values greater than 0")
    except ValueError:
        print("Try again!!! Read the question clearly.")

cnt = 0

while cnt < totl:
    while True:
        name = input("Enter the name of the student: ").replace(" ", "")
        for ch in name:
            if ch in string.punctuation:
                name = name.replace(ch, "")

        if name in keyword.kwlist or name in dir(builtins) or name == "cnt":
            print("Is there someone named on python keywords?!")
        else:
            break

    while True:
        try:
            grade = int(input("Enter the Grade: "))
            break
        except ValueError:
            print("You should only put number value :)")

    while True:
        try:
            roll_no = int(input("Enter the Roll No of the student: "))
            break
        except ValueError:
            print("AGAINNN!!! You should only put number value")

    while True:
        try:
            admn_no = int(input("Enter Admission No: "))
            break
        except ValueError:
            print("How many times should I say: try number value :(")

    globals()[name] = Student(name, grade, roll_no, admn_no)
    cnt += 1


# ---------- DISPLAY ----------

print(Organisation.names)

while True:
    choi = input(
        "Enter the name of the student to get details "
        "(or 0 to exit): "
    )

    if choi == "0":
        break
    if choi == "":
        continue

    try:
        print(globals()[choi].details)
    except KeyError:
        print("== Try again ==")