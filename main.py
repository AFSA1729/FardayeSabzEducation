from Controller.DriveController import DriveController
from Controller.CourseController import CourseController
from Model.Course import Course

CourseController.init_courses(14)

# for course in CourseController.get_all_courses():
#     print(course.students())
#     print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")

course = CourseController.find_course("پسر", 7, 1)
print(course.students())
print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")
course.update_course_students_docs(14)

print("adgal;sdkgjl;ksjk")
