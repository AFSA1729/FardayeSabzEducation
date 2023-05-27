from Controller.DriveController import DriveController


class StudentController:
    __student_documents_folder_id = "10iONxv6qOQCRYZoRGw7Cb6785jcYblVS"

    @staticmethod
    def student_id(student_id: int) -> str:
        string = student_id.__str__()
        while len(string) < 3:
            string = "0" + string
        return string

    @staticmethod
    def create_student_doc_folder(student_name: str, student_id: str):
        title = student_name + '-' + student_id
        DriveController.create_folder(title, StudentController.__student_documents_folder_id)
