from Controller.DriveController import DriveController
import pandas as pd


class Course:
    def __init__(self, gsheet_key: str, sex: str, grade: int, name: str):
        self.gsheet_key = gsheet_key
        self.sex = sex
        self.grade = grade
        self.name = name
        self.students: list[str]
        self.students = []
        self.teacher = ""

    # TODO add setter getters
    def add_student(self, student_name: str):
        self.students.append(student_name)

    def create_new_week_sheet(self, week_count: int, date: str):
        spreadsheet = DriveController.gsheets.open_by_key(self.gsheet_key)
        worksheet = spreadsheet.add_worksheet("هفته " + week_count.__str__())
        df = worksheet.get_as_df()
        df['نام'] = self.students + ['مدرس', 'تاریخ', 'مبحث']
        nan = [''] * df['نام'].shape[0]
        df['حضور غیاب'] = nan
        df['مشارکت در کلاس'] = nan
        df['انجام تکالیف'] = nan
        df['ارزیابی مدرس'] = nan
        df['توضیحات'] = nan
        df['حضور غیاب'][df['نام'] == 'مدرس'] = self.teacher
        df['حضور غیاب'][df['نام'] == 'تاریخ'] = date
        worksheet.set_dataframe(df, (1, 1))
