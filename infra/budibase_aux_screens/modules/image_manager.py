from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from shutil import move
import os

@dataclass
class DirNamesMannager():
    dir_path: Path
    dir_name: str

    def path(self) -> Path:
        return self.dir_path / self.dir_name


def create_dir_name(sample_id: int) -> str:
    dir_name: str

    dir_name =  sample_id + '_' + str(datetime.now())

    return dir_name


def move_to_ia_folder(images_dir: DirNamesMannager, ia_dir: str):    
    move(images_dir.path(), ia_dir)


def download_image(file, sample_id: int):
    print("HELLO WOLRD")
    '''return 0
    dir: DirNamesMannager = DirNamesMannager(Path('/infra/budibase_aux_screens/screens/statics/imgs'), create_dir_name(sample_id))

    os.mkdir(dir.path())'''


if __name__ == "__main__":
    create_dir_name(5)