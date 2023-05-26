from Controller.DriveController import DriveController
from Controller.CourseController import CourseController
from Model.Course import Course

import pydrive.files
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import pygsheets
from pygsheets import Spreadsheet

# drive_controller = DriveController()
# CourseController.add_course(Course("1KV1KDJy4ytjE2V0lkl56L96Lnn0UlAbIhAia2CmBa10", "پسر", 7, 1))
# CourseController.add_course(Course("1ke2oT1HakhGf4aAPsiHmX7zCebQ8TZIQDWTdN-GqEoM", "پسر", 7, 2))
# CourseController.add_course(Course("1ldMOeJW9xSDUGNkCJJCwJF7HiEAh4kAVZIaUjNIAgos", "دختر", 7, 1))
# CourseController.add_course(Course("1EmIPoZicQTBZPipCDYl_BgbsKdk379J6qHAhiSsGqmc", "دختر", 7, 2))
#
# CourseController.add_course(Course("1r4r63RAOT-9t1mioOxnz0DJJw7jDDRpE4alUmVaYiTY", "پسر", 8, 1))
# CourseController.add_course(Course("164zb0jnGwjmPQsVq4sjTgyJ9RENiN2W8hm0IWbj-Pno", "پسر", 8, 2))
# CourseController.add_course(Course("1S4C9NDhoEMoo77wkIwgGu-BA1qUKZMyD_YXFaMkp1Vk", "دختر", 8, 1))
# CourseController.add_course(Course("1VIKxBWufZ38st7hsjb7kZ6ATulbrVstuDDkFZidg_ms", "دختر", 8, 2))
#
# CourseController.add_course(Course("1c5fbWK7Q6ZLmBI2ccDE086Va8RKqzVLgeOvvgdzmDcw", "پسر", 9, 1))
# CourseController.add_course(Course("1lZ92HcWYfqytQ5DEs6CB4Ib-tBKQcy_nBmjqhYJ1iH0", "پسر", 9, 2))
#
# CourseController.add_course(Course("1nQxCm66eUX58pY-djWsfJDyOnIi76arQMIcPZkD7QDA", "پسر", 12, 1))
# CourseController.add_course(Course("1XCBB8vPoBbnTWApvHkvSmUL1z75Vr_C5vG3s3b7EF18", "پسر", 12, 2))
# CourseController.add_course(Course("1AvqdW6NQOLd7m9tg4V5wunBAaiY3yURyTTQWgFe3tO8", "دختر", 12, 1))
# CourseController.add_course(Course("1TzhqtTAOEAS78UFcYrYuzcwsheFYQJr8QdNjVgZpyCc", "دختر", 12, 2))
#
# CourseController.update_students(15)
# CourseController.update_teachers(15)
#
# flag = True
# for course in CourseController.get_all_courses():
#     if flag:
#         print(course.students())
#         flag = False
#     print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")

# CourseController.create_week_sheets(14, "5-18-2023")

# --------------------------------------------------------------------------------------------------------


CourseController.init_courses(15)

for course in CourseController.get_all_courses():
    print(course.students())
    print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")

print("adgal;sdkgjl;ksjk")
