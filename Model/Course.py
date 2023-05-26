from Controller.DriveController import DriveController
import pandas as pd


class Course:
    def __init__(self, gsheet_key: str, sex: str, grade: int, number: int, name="NA"):
        self.gsheet_key = gsheet_key
        self.sex = sex
        self.grade = grade
        self.number = number
        self.name = name
        # self.students: list[str]
        self.students: dict[int, str]
        self.students = {}
        self.teacher = ""

    # TODO add setter getters
    # TODO مدرسین excel not filled
    # TODO class excel not filled
    # TODO Telegram Bot
    # TODO remove excels
    # TODO add column
    def add_student(self, student_number: int, student_name: str):
        self.students[student_number] = student_name

    def create_week_sheet(self, week_count: int, date: str):
        df, worksheet = DriveController.open_gsheet_as_df(self.gsheet_key, "هفته " + week_count.__str__())
        df['نام'] = list(self.students.values()) + ['مدرس', 'تاریخ', 'مبحث','عنوان کلاس']
        df['شماره دانش‌آموزی'] = list(self.students.keys())
        nan = [''] * df['نام'].shape[0]
        df['حضور غیاب'] = nan
        df['مشارکت در کلاس'] = nan
        df['انجام تکالیف'] = nan
        df['ارزیابی مدرس'] = nan
        df['توضیحات'] = nan
        df['حضور غیاب'][df['نام'] == 'مدرس'] = self.teacher
        df['حضور غیاب'][df['نام'] == 'تاریخ'] = date
        df['حضور غیاب'][df['نام'] == 'عنوان کلاس'] = self.name
        worksheet.set_dataframe(df, (1, 1))
