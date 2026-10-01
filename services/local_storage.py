import os
import shutil


class LocalStorage:

    def __init__(self):

        self.upload_dir = "uploads"

        os.makedirs(
            self.upload_dir,
            exist_ok=True
        )

    def upload_file(self, source_path):

        filename = os.path.basename(
            source_path
        )

        destination = os.path.join(
            self.upload_dir,
            filename
        )

        shutil.copy2(
            source_path,
            destination
        )

        return destination

    def download_file(
        self,
        source_path,
        destination_path
    ):

        shutil.copy2(
            source_path,
            destination_path
        )

    def delete_file(self, file_path):

        if os.path.exists(file_path):
            os.remove(file_path)