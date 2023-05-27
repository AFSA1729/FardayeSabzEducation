import pygsheets

from Controller.DriveController import DriveController
import pandas as pd


class Course:
    def __init__(self, gsheet_id: str, sex: str, grade: int, number: int, topic=None):
        self.__gsheet_key = gsheet_id
        self.__sex = sex
        self.__grade = grade
        self.__number = number
        self.__topic: str = topic
        self.__students: dict[int, str]
        self.__students = {}
        self.__teacher = ""

    # TODO class excel not filled
    # TODO Telegram Bot

    def update_course_students_docs(self, week_count: int):
        sheet_name = "هفته " + week_count.__str__()
        df, worksheet = DriveController.open_gsheet_as_df(self.__gsheet_key, sheet_name)

        students_num = len(df) - 4

        date = df['شماره دانش‌آموزی'][df['نام'] == 'تاریخ']
        mabhas = df['شماره دانش‌آموزی'][df['نام'] == 'مبحث']
        new_index = df.columns.tolist()
        new_index = ['مدرس', 'تاریخ', 'مبحث', 'عنوان کلاس'] + new_index[2:]

        for i in range(students_num):
            print(df['نام'][i])
            s: pd.Series = df.iloc[i].copy()
            s.drop(labels=['شماره دانش‌آموزی', 'نام'])
            s['مدرس'] = self.__teacher
            s['تاریخ'] = date
            s['مبحث'] = mabhas
            s['عنوان کلاس'] = self.__topic
            s.reindex(index=new_index)

    def create_week_sheet(self, week_count: int, date: str):
        df, worksheet = DriveController.open_gsheet_as_df(self.__gsheet_key, "هفته " + week_count.__str__())
        df['نام'] = list(self.__students.values()) + ['مدرس', 'تاریخ', 'مبحث', 'عنوان کلاس']
        df['شماره دانش‌آموزی'] = list(self.__students.keys()) + [""] * (len(df.index) - len(self.__students.keys()))
        nan = [''] * df['نام'].shape[0]
        df['حضور غیاب'] = nan
        df['مشارکت در کلاس'] = nan
        df['انجام تکالیف'] = nan
        df['ارزیابی مدرس'] = nan
        df['توضیحات'] = nan
        df['شماره دانش‌آموزی'][df['نام'] == 'مدرس'] = self.__teacher
        df['شماره دانش‌آموزی'][df['نام'] == 'تاریخ'] = date
        df['شماره دانش‌آموزی'][df['نام'] == 'عنوان کلاس'] = self.__topic
        worksheet.set_dataframe(df, (1, 1))

    def add_std_id(self, week_count: int, date: str):
        if ("هفته " + week_count.__str__()) not in DriveController.get_sheet_names(self.__gsheet_key):
            return
        df, worksheet = DriveController.open_gsheet_as_df(self.__gsheet_key, "هفته " + week_count.__str__())

        df['شماره دانش‌آموزی'] = list(self.__students.keys()) + [""] * (len(df.index) - len(self.__students.keys()))
        df['شماره دانش‌آموزی'][df['نام'] == 'مدرس'] = self.__teacher
        df['شماره دانش‌آموزی'][df['نام'] == 'تاریخ'] = date
        # df['شماره دانش‌آموزی'][df['نام'] == 'عنوان کلاس'] = self.__topic

        df['حضور غیاب'][df['نام'] == 'مدرس'] = ""
        df['حضور غیاب'][df['نام'] == 'تاریخ'] = ""
        df['حضور غیاب'][df['نام'] == 'عنوان کلاس'] = ""

        col = df.columns.tolist()
        col = ([col[0]] + col[-1:]) + col[1:-1]
        df = df[col]
        string = ["عنوان کلاس", self.__topic] + [""] * (len(col) - 2)
        df.loc[len(df)] = string

        worksheet.set_dataframe(df, (1, 1))

    @property
    def sex(self):
        return self.__sex

    @property
    def number(self):
        return self.__number

    @property
    def grade(self):
        return self.__grade

    @property
    def topic(self):
        return self.__topic

    @topic.setter
    def topic(self, value: str):
        self.__topic = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value: str):
        self.__teacher = value
        pass

    def add_student(self, student_number: int, student_name: str):
        self.__students[student_number] = student_name

    def clear_students(self):
        self.__students.clear()

    def students(self) -> dict[int, str]:
        return self.__students.copy()
