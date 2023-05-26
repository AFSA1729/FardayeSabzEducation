from Controller.DriveController import DriveController
import pandas as pd


class Course:
    def __init__(self, gsheet_id: str, sex: str, grade: int, number: int, topic=None):
        self.__gsheet_key = gsheet_id
        self.__sex = sex
        self.__grade = grade
        self.__number = number
        self.__topic: str = topic
        # self.students: list[str]
        self.__students: dict[int, str]
        self.__students = {}
        self.__teacher = ""

    # TODO add setter getters
    # مدرسین excel not filled
    # TODO test مدرسین excel not filled
    # TODO class excel not filled
    # TODO Telegram Bot
    # TODO remove excels
    # TODO add column

    def create_week_sheet(self, week_count: int, date: str):
        df, worksheet = DriveController.open_gsheet_as_df(self.__gsheet_key, "هفته " + week_count.__str__())
        df['نام'] = list(self.__students.values()) + ['مدرس', 'تاریخ', 'مبحث', 'عنوان کلاس']
        df['شماره دانش‌آموزی'] = list(self.__students.keys())
        nan = [''] * df['نام'].shape[0]
        df['حضور غیاب'] = nan
        df['مشارکت در کلاس'] = nan
        df['انجام تکالیف'] = nan
        df['ارزیابی مدرس'] = nan
        df['توضیحات'] = nan
        df['حضور غیاب'][df['نام'] == 'مدرس'] = self.__teacher
        df['حضور غیاب'][df['نام'] == 'تاریخ'] = date
        df['حضور غیاب'][df['نام'] == 'عنوان کلاس'] = self.__topic
        worksheet.set_dataframe(df, (1, 1))

    def sex(self):
        return self.__sex

    def number(self):
        return self.__number

    def grade(self):
        return self.__grade

    @property
    def topic(self) -> str:
        return self.__topic

    @topic.setter
    def topic(self, value: str):
        self.__topic = value

    def add_student(self, student_number: int, student_name: str):
        self.__students[student_number] = student_name

    def clear_students(self):
        self.__students.clear()

    def students(self) -> dict[int, str]:
        return self.__students.copy()
