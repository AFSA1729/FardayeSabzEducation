import pygsheets

from Controller.DriveController import DriveController
from Model.Course import Course
import pandas as pd


class CourseController:
    __all_courses: list[Course]
    __all_courses = []
    __teachers_sheet_key = "1pesjG4J8GyqUZC-PXK7dNGiugnPLWSzo9kL5YEiB2Cc"
    __students_sheet_key = "1fQaRzEVVOX4RTszCSXIhDP88NvUJrYEEayVVYeWwUhw"

    @staticmethod
    def add_course(course: Course):
        CourseController.__all_courses.append(course)

    @staticmethod
    def find_course(sex: str, grade: int, name: str):
        for course in CourseController.__all_courses:
            if course.sex == sex and course.grade == grade and course.name == name:
                return course
        return None

    @staticmethod
    def update_students(week_count: int):
        for course in CourseController.__all_courses:
            course.students.clear()
        df = DriveController.open_gsheet_as_df(key=CourseController.__students_sheet_key,
                                               sheet="هفته " + week_count.__str__())
        for i in range(df['نام'].shape[0]):
            if CourseController.find_course(df['جنسیت'][i], df['پایه'][i], 'ریاضی') is not None:
                course = CourseController.find_course(df['جنسیت'][i], df['پایه'][i], 'ریاضی')
                course.add_student(df['نام'][i])

            if CourseController.find_course(df['جنسیت'][i], df['پایه'][i], 'زبان') is not None:
                course = CourseController.find_course(df['جنسیت'][i], df['پایه'][i], 'زبان')
                course.add_student(df['نام'][i])

    @staticmethod
    def update_teachers(week_count: int):
        df = DriveController.open_gsheet_as_df(key=CourseController.__teachers_sheet_key,
                                               sheet="هفته " + week_count.__str__())
        for i in range(df['نام'].shape[0]):
            if CourseController.find_course(df['جنسیت'][i], df['پایه'][i], df['درس'][i]) is not None:
                course = CourseController.find_course(df['جنسیت'][i], df['پایه'][i], df['درس'][i])
                course.teacher = df['نام'][i]

    @staticmethod
    def create_week_sheets(week_count: int, date: str):
        for course in CourseController.__all_courses:
            course.create_week_sheet(week_count, date)

    @staticmethod
    def get_all_courses():
        return CourseController.__all_courses
