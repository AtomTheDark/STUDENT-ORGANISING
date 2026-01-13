import keyword
import builtins
import string
class Organisation():
    schl="SCHOOL"
    names=list()
    
    
class Student(Organisation):
    def __init__(self,name,grade,roll_no,admn_no):
        self.name=name
        self.grade=grade
        self.roll_no=roll_no
        self.admn_no=admn_no
        Organisation.names.append(self.name)
        self.details=dict(zip(("Name","Grade","Roll no","Admn no"),
        (self.name,self.grade,self.roll_no,self.admn_no)))
        
    
Organisation.schl=input("Enter your Organisation: ")
while True:
    try:
        totl=int(input("Enter how many students you want to upload: "))
        if totl>=1:
            break
        else:
            print("Use values greater than 0")
    except ValueError:
        print("Try again!!!, Read the question clearly.")    
cnt=0
while cnt<totl:
    while True:
            name=input("Enter the name of the student: ").replace(" ","_")
            for i in range(0,len(name)):
                if name[i] in string.punctuation:
                    name.replace(name[i],"_")
            if name in keyword.kwlist or name in dir(builtins):
                print("is there someone named on python keywords?!" )
                continue
            else:
                break    
    print()
    while True:
        try:
            grade=int(input("Enter the Grade: "))
            break
        except ValueError:
            print("You should only put number value :)")
    while True:
        try:        
            roll_no=int(input("Enter the Roll No of the student: "))
            break
        except ValueError:
            print("AGAINNN!!! You should only put number value")
    while True:
        try:                
            admn_no=int(input("Enter Admission No: "))
            break
        except ValueError:
            print("How many times Should I have to say Try number value :(")    
    globals()[name]=Student(name,grade,roll_no,admn_no)
    print()
    #print(globals()[name].details)
    print()
    cnt+=1
else:
    while True:
        print(Organisation.names)
        print()
        while True:
            choi=input("Enter the name of the student to get his details\
         for: (or 0 to exit: )")
            if choi=="0":
                break
            if choi=="":
                continue          
            print()
            try:
                print(globals()[choi].details)
            except KeyError:
                print(" == Try again == ")
            print()