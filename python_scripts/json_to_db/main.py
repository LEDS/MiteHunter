from python_modules.job import job

from schedule import run_pending
from time import sleep


def main():
    """
    Feature: the main function just execute in infinit loop the functio job, who is defined in job.py;
    the loop time and operations are defined in job.py, not here
    """

    while True:
        run_pending()
        sleep(1)


# Test Function
if __name__ == "__main__":
    main()


