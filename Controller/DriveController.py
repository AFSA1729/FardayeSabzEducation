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
