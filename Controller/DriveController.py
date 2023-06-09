from typing import Tuple

import pydrive.files
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import pygsheets
from pygsheets import Spreadsheet


class DriveController:
    __student_documents_folder_id = "10iONxv6qOQCRYZoRGw7Cb6785jcYblVS"
    __client_secret_path = ".\Resources\client_secret.json"
    __settings_path = ".\Resources\settings.yaml"
    gauth = GoogleAuth(__settings_path)
    __drive = GoogleDrive(gauth)
    __gsheets = pygsheets.authorize(credentials_directory="./Resources/",
                                    client_secret=__client_secret_path)

    @staticmethod
    def add_sheet(key: str, sheet_name: str):
        spreadsheet = DriveController.get_gsheets().open_by_key(key)
        spreadsheet.add_worksheet(sheet_name)

    @staticmethod
    def open_gsheet_as_df(key: str, sheet: str = None) -> Tuple[pd.DataFrame, pygsheets.Worksheet]:
        """
        opens a Google sheet as pd.DataFrame
        :param key: key of gsheet
        :param sheet: name of the sheet
        :return: dataframe of that sheet
        """
        spreadsheet = DriveController.get_gsheets().open_by_key(key)
        worksheet: pygsheets.Worksheet
        if sheet is None:
            worksheet = spreadsheet.worksheets()[0]
        else:
            worksheet = spreadsheet.worksheet_by_title(sheet)
        df = worksheet.get_as_df(include_tailing_empty=False)
        return df, worksheet

    @staticmethod
    def get_children(root_folder_id: str) -> list[pydrive.files.GoogleDriveFile]:
        string = "\'" + root_folder_id + "\'" + " in parents and trashed=false"
        file_list = DriveController.__drive.ListFile({'q': string}).GetList()
        return file_list

    # Some basic helper functions
    @staticmethod
    def get_folder_id(root_folder_id, root_folder_title: str) -> str | None:
        file_list = DriveController.get_children(root_folder_id)
        for file in file_list:
            if file['title'] == root_folder_title:
                return file['id']
        return None

    @staticmethod
    def get_student_folder_id(student_id: str) -> str | None:
        folder_list = DriveController.get_children(DriveController.__student_documents_folder_id)
        for folder in folder_list:
            print(folder['title'])
            if folder['title'].split("-")[0] == student_id or folder['title'].split("-")[1] == student_id:
                return folder['id']
        return None

    @staticmethod
    def get_student_gsheet_id(folder_id: str, student_id: str) -> str | None:
        file_list = DriveController.get_children(folder_id)
        for file in file_list:
            if file['title'].split('-')[0] == student_id or file['title'].split('-')[1] == student_id:
                return file['id']
        return None

    @staticmethod
    def create_folder(title: str, parent_id: str) -> pydrive.files.GoogleDriveFile:
        file_metadata = {
            'title': title,
            'parents': [{'id': parent_id}],  # parent folder
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = DriveController.__drive.CreateFile(file_metadata)
        folder.Upload()
        return folder

    @staticmethod
    def create_gsheet(title: str, parent_id: str):
        file_metadata = {
            'title': title,
            'parents': [{'id': parent_id}],  # parent folder
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        gsheet = DriveController.__drive.CreateFile(file_metadata)
        gsheet.Upload()
        return gsheet

    @staticmethod
    def get_sheet_names(key: str):
        spreadsheet = DriveController.get_gsheets().open_by_key(key)
        return [s.title for s in spreadsheet.worksheets()]

    @staticmethod
    def get_drive():
        return DriveController.__drive

    @staticmethod
    def get_gsheets():
        return DriveController.__gsheets
