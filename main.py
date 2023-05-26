from Controller.DriveController import DriveController
from Controller.CourseController import CourseController
from Model.Course import Course

drive_controller = DriveController()
CourseController.add_course(Course("1KV1KDJy4ytjE2V0lkl56L96Lnn0UlAbIhAia2CmBa10", "پسر", 7, 1))
CourseController.add_course(Course("1ke2oT1HakhGf4aAPsiHmX7zCebQ8TZIQDWTdN-GqEoM", "پسر", 7, 2))
CourseController.add_course(Course("1ldMOeJW9xSDUGNkCJJCwJF7HiEAh4kAVZIaUjNIAgos", "دختر", 7, 1))
CourseController.add_course(Course("1EmIPoZicQTBZPipCDYl_BgbsKdk379J6qHAhiSsGqmc", "دختر", 7, 2))

CourseController.add_course(Course("1r4r63RAOT-9t1mioOxnz0DJJw7jDDRpE4alUmVaYiTY", "پسر", 8, 1))
CourseController.add_course(Course("164zb0jnGwjmPQsVq4sjTgyJ9RENiN2W8hm0IWbj-Pno", "پسر", 8, 2))
CourseController.add_course(Course("1S4C9NDhoEMoo77wkIwgGu-BA1qUKZMyD_YXFaMkp1Vk", "دختر", 8, 1))
CourseController.add_course(Course("1VIKxBWufZ38st7hsjb7kZ6ATulbrVstuDDkFZidg_ms", "دختر", 8, 2))

CourseController.add_course(Course("1c5fbWK7Q6ZLmBI2ccDE086Va8RKqzVLgeOvvgdzmDcw", "پسر", 9, 1))
CourseController.add_course(Course("1lZ92HcWYfqytQ5DEs6CB4Ib-tBKQcy_nBmjqhYJ1iH0", "پسر", 9, 2))

CourseController.update_students()
CourseController.update_teachers()

CourseController.create_week_sheets(14, "5-18-2023")

print("adgal;sdkgjl;ksjk")
