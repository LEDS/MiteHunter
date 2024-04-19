from modules.jsons_folder_read import *
import schedule
import time

def main():
    schedule.every(1).seconds.do(checkExistsFilesFolder)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()