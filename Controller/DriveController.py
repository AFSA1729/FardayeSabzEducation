from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import pygsheets
from pygsheets import Spreadsheet


class DriveController:
    __credentials_path = "credentials.json"
    __client_secret_path = ".\Controller\client_secret.json"
    __settings_path = "settings.yaml"
    gauth = GoogleAuth(__client_secret_path)
    __drive = GoogleDrive(gauth)
    __gsheets = pygsheets.authorize(__client_secret_path)

    @staticmethod
    def get_sheet_names(gsheet: Spreadsheet):
        return [s.title for s in gsheet.worksheets()]

    @staticmethod
    def get_drive():
        return DriveController.__drive

    @staticmethod
    def get_gsheets():
        return DriveController.__gsheets

    @staticmethod
    def open_gsheet_as_df(key: str, sheet: str) -> (pd.DataFrame, pygsheets.Worksheet):
        """
        opens a Google sheet as pd.DataFrame
        :param key: key of gsheet
        :param sheet: name of the sheet
        :return: dataframe of that sheet
        """
        spreadsheet = DriveController.get_gsheets().open_by_key(key)
        worksheet: pygsheets.Worksheet
        worksheet = spreadsheet.worksheet_by_title(sheet)
        df = worksheet.get_as_df()
        return df, worksheet

    ### Some basic helper functions ###
    @staticmethod
    def get_children(root_folder_id):
        str = "\'" + root_folder_id + "\'" + " in parents and trashed=false"
        file_list = DriveController.__drive.ListFile({'q': str}).GetList()
        return file_list

    @staticmethod
    def get_folder_id(root_folder_id, root_folder_title):
        file_list = DriveController.get_children(root_folder_id)
        for file in file_list:
            if file['title'] == root_folder_title:
                return file['id']
