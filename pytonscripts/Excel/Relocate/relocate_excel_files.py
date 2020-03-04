from pytest import mark
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

folder_to_track = "/Users/orir/Downloads/"
folder_destination = "/Users/orir/Downloads/ExcelDownloads"


# הנדלר שנועד לדגום תקיית הורדות עבור קבצי אקסל, אשר לוקח הורדות אקסל חדשות ומעביר אותן לתקיה נגררת של הרודות לקבצי אקסל
def test_relocate_excel_files_from_downloads_folder():
    event_handler = MyHandlerTests()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()
    return observer


# try:
#    while True:
#       time.sleep(10)
# except KeyboardInterrupt:
#    observer.stop()


@mark.smoke
@mark.orderdiff
class MyHandlerTests(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for index, filename in enumerate(os.listdir(folder_to_track), 1):
            if filename.endswith('xlsx'):
                self.i = index
                new_name = f"{filename}_{str(self.i)}.xlsx"
                file_exists = os.path.isfile(f"{folder_destination}/{new_name}")
                while file_exists:
                    new_name = f"{filename}_{str(self.i)}.xlsx"
                    file_exists = os.path.isfile(f"{folder_destination}/{new_name}")
                src = f"{folder_to_track}/{filename}"
                new_dest = f"{folder_destination}/{new_name}"
                os.rename(src, new_dest)
