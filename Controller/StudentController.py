from Controller.DriveController import DriveController
import pandas as pd


class StudentController:
    __student_documents_folder_id = "10iONxv6qOQCRYZoRGw7Cb6785jcYblVS"

    @staticmethod
    def update_student_doc_folder(student_name: str, student_id: str, s: pd.Series):

        pass
    @staticmethod
    def create_student_doc_folder(student_name: str, student_id: str, s: pd.Series):
        title = student_id + '-' + student_name
        folder = DriveController.create_folder(title, StudentController.__student_documents_folder_id)
        gsheet = DriveController.create_gsheet(title, folder['id'])
        df1, worksheet = DriveController.open_gsheet_as_df(gsheet['id'])
        df = pd.DataFrame(columns=s.index.tolist())
        df.loc[0] = s
        worksheet.set_dataframe(df, (1, 1))

    @staticmethod
    def student_id(student_id: int) -> str:
        string = student_id.__str__()
        while len(string) < 3:
            string = "0" + string
        return string
