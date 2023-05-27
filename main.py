from Controller.DriveController import DriveController
from Controller.CourseController import CourseController
from Controller.StudentController import StudentController
from Model.Course import Course

CourseController.init_courses(14)

# for course in CourseController.get_all_courses():
#     print(course.students())
#     print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")

# course = CourseController.find_course("پسر", 7, 1)
# print(course.students())
# print(f"--> sex:{course.sex} grade:{course.grade} number:{course.number}")
# course.update_course_students_docs(14)

print(StudentController.student_id(42))
# file_metadata = {
#     'title': "salam",
#     'parents': [{'id': "10iONxv6qOQCRYZoRGw7Cb6785jcYblVS"}],  # parent folder
#     'mimeType': 'application/vnd.google-apps.folder'
# }
#
# folder = DriveController.get_drive().CreateFile(file_metadata)
# folder.Upload()
# DriveController.create_folder("salam2", "10iONxv6qOQCRYZoRGw7Cb6785jcYblVS")
StudentController.create_student_doc_folder("Ashkan Majidi", "007")
# DriveController.create_folder("Ashkan Majidi", "007")
print("adgal;sdkgjl;ksjk")
