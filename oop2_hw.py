# class playlist:
#     def __init__(self,owner:str):
#         self.owner=owner
#         self.tracks=[]
#     def add_tracks(self,title:str,artist:str):
#         self.tracks.append((title,artist))
#     def remove_last(self):
#         if len(self.tracks)==0:
#             return None
#         return self.tracks.pop()
#     def total_tracks(self):
#         return len(self.tracks)
#     def unique_tracks(self):
#         unique=[]
#         for t in self.tracks:
#             if t not in unique:
#                 unique.append(t)
#         return unique
#     def filter_by_artist(self,artist):
#         result=[]
#         for t in self.tracks:
#             if t[1]==artist:
#                 result.append(t)
#         return result
# pl = playlist("Muhammad")
# print(pl.total_tracks())
# pl.add_tracks("Yomg'irlar", "Shahzoda")
# pl.add_tracks("Gulim", "Yulduz Usmonova")
# pl.add_tracks("Yomg'irlar", "Shahzoda")
# pl.add_tracks("Xayr edi", "Lola")
# pl.add_tracks("Kel", "Ulug'bek Rahmatullayev")
# print(pl.total_tracks()) 
# print(pl.unique_tracks())
# print(pl.remove_last())
# print(pl.total_tracks())
# print(pl.filter_by_artist("Yomg'irlar"))
# print(pl.filter_by_artist("Yulduz Usmonova"))

# -------------------------------------------------------

# class Employee:
#     def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0) -> None:
#         self.name = name
#         self.employee_id = employee_id
#         self.__working_hours = []
#         self.hourly_rate = hourly_rate
#     def log_hours(self,hour:int):
#         if 0<=hour<=24:
#             self.__working_hours.append(hour)
#             return True
#         return False
#     def total_hours(self):
#         return sum(self.__working_hours)
#     def calculate_salary(self)->float:
#         return self.total_hours()*self.hourly_rate
#     def reset_hours(self)-> None:
#         self.__working_hours.clear()

# employee = Employee("toshmat", "E101", hourly_rate=20.0)
# print(employee.log_hours(8))
# print(employee.log_hours(9))
# print(employee.log_hours(10))
# print(employee.log_hours(25))
# print(employee.total_hours())
# print(employee.calculate_salary())
# employee.reset_hours()
# print(employee.total_hours())
# print(employee.calculate_salary())

# --------------------------------------------------

# class Student:
#     def __init__(self, name: str, student_id: str) -> None:
#         self.name = name
#         self.student_id = student_id
#         self.__grades = []
#     def add_grade(self,grade:str)-> None:
#         if 0<=grade<=100:
#             self.__grades.append(grade)
#         else:
#             print("xato baho kiritdingi")
#     def calculate_average(self)-> float:
#         if len (self.__grades)==0:
#             return 0.0
#         return sum (self.__grades)/len(self.__grades)
#     def get_status(self) -> str:
#             avg = self.calculate_average()
#             if 90 <= avg <= 100:
#                 return "A'lo"
#             elif 80 <= avg < 90:
#                 return "Yaxshi"
#             elif 70 <= avg < 80:
#                 return "Qoniqarli"
#             else:
#                 return "Qoniqarsiz"

# student = Student("Nodira", "S123")
# student.add_grade(85)
# student.add_grade(90)
# print(student.calculate_average())
# print(student.get_status())
# student.add_grade(150)
