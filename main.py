from Controller.DriveController import DriveController
from Controller.CourseController import CourseController
from Controller.StudentController import StudentController
from Model.Course import Course

week_count = 15
CourseController.init_courses(week_count)

# for course in CourseController.get_all_courses():
#     print(course.students())
#     print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")


CourseController.create_week_sheets(week_count, "1401-03-04")
# CourseController.update_students_docs(week_count)
# print("docs.done")
# print(CourseController.get_unfilled_teachers_list(week_count))

print("adgal;sdkgjl;ksjk")
