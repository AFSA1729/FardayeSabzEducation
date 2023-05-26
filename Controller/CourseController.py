import pygsheets

from Controller.DriveController import DriveController
from Model.Course import Course
import pandas as pd


# TODO add classes from کلاس ها folder in drive automatically

class CourseController:
    __all_courses: list[Course]
    __all_courses = []
    __teachers_sheet_key = "1pesjG4J8GyqUZC-PXK7dNGiugnPLWSzo9kL5YEiB2Cc"
    __students_sheet_key = "1fQaRzEVVOX4RTszCSXIhDP88NvUJrYEEayVVYeWwUhw"
    __classes_folder_id = "1sXJvKUNpmkppBm6PvVX5RDyIRrZNPeG2"

    @staticmethod
    def init_courses():
        gsheets = DriveController.get_children(CourseController.__classes_folder_id)
        for gsheet in gsheets:
            title = gsheet['title'].split('-')
            print(title)

    pass

    @staticmethod
    def add_course(course: Course):
        CourseController.__all_courses.append(course)

    @staticmethod
    def find_course(sex: str, grade: int, number: int):
        for course in CourseController.__all_courses:
            if course.sex == sex and course.grade == grade and course.number == number:
                return course
        return None

    @staticmethod
    def update_students(week_count: int):
        for course in CourseController.__all_courses:
            course.clear_students()
        df = DriveController.open_gsheet_as_df(key=CourseController.__students_sheet_key,
                                               sheet="هفته " + week_count.__str__())
        for i in range(df['شماره دانش‌آموزی'].shape[0]):
            sex = df['جنسیت'][i]
            grade = df['پایه'][i]
            student_name = df['نام'][i]
            student_number = df['شماره دانش‌آموزی'][i]

            if CourseController.find_course(sex, grade, 1) is not None:
                course = CourseController.find_course(sex, grade, 1)
                course.add_student(student_number, student_name)
            else:
                raise ValueError("Course with this details not found: sex=%s grade=%s number=1" % (sex, grade))

            if CourseController.find_course(sex, grade, 2) is not None:
                course = CourseController.find_course(sex, grade, 2)
                course.add_student(student_number, student_name)
            else:
                raise ValueError("Course with this details not found: sex=%s grade=%s number=2" % (sex, grade))

    @staticmethod
    def update_teachers(week_count: int):
        df: pd.DataFrame = DriveController.open_gsheet_as_df(key=CourseController.__teachers_sheet_key,
                                                             sheet="هفته " + week_count.__str__())
        if "نام" not in df.columns:
            raise ValueError("The gsheet file named \"مدرسین\" not filled.")

        for i in range(df['نام'].shape[0]):
            if CourseController.find_course(df['جنسیت'][i], df['پایه'][i], df['زنگ'][i]) is not None:
                course = CourseController.find_course(df['جنسیت'][i], df['پایه'][i], df['زنگ'][i])
                course.teacher = df['نام'][i]
                course.topic = df['درس'][i]
            else:
                raise ValueError("Course with this details not found: sex=%s grade=%s number=%s" % (
                    df['جنسیت'][i], df['پایه'][i], df['زنگ'][i]))

    @staticmethod
    def create_week_sheets(week_count: int, date: str):
        for course in CourseController.__all_courses:
            course.create_week_sheet(week_count, date)

    @staticmethod
    def get_all_courses():
        return CourseController.__all_courses
