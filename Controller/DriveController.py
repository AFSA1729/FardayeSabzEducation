from typing import Tuple

import pydrive.files
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import pygsheets
from pygsheets import Spreadsheet


class DriveController:
    __client_secret_path = ".\Resources\client_secret.json"
    __settings_path = ".\Resources\settings.yaml"
    gauth = GoogleAuth(__settings_path)
    __drive = GoogleDrive(gauth)
    __gsheets = pygsheets.authorize(credentials_directory="./Resources/",
                                    client_secret=__client_secret_path)

    @staticmethod
    def open_gsheet_as_df(key: str, sheet: str) -> Tuple[pd.DataFrame, pygsheets.Worksheet]:
        """
        opens a Google sheet as pd.DataFrame
        :param key: key of gsheet
        :param sheet: name of the sheet
        :return: dataframe of that sheet
        """
        spreadsheet = DriveController.get_gsheets().open_by_key(key)
        worksheet: pygsheets.Worksheet
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
    def get_folder_id(root_folder_id, root_folder_title: str) -> str:
        file_list = DriveController.get_children(root_folder_id)
        for file in file_list:
            if file['title'] == root_folder_title:
                return file['id']

    @staticmethod
    def create_folder(title: str, parent_id: str):
        file_metadata = {
            'title': title,
            'parents': [{'id': parent_id}],  # parent folder
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = DriveController.__drive.CreateFile(file_metadata)
        folder.Upload()

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
