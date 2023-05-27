from Controller.DriveController import DriveController
from Controller.CourseController import CourseController
from Controller.StudentController import StudentController
from Model.Course import Course

week_count = 14
CourseController.init_courses(week_count)
# for course in CourseController.get_all_courses():
#     print(course.students())
#     print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")


# CourseController.update_students_docs(14)

CourseController.get_unfilled_teachers_list(week_count)

print("adgal;sdkgjl;ksjk")
