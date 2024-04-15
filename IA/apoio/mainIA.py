from modules.email_processor import EmailProcessor
from modules.email_client import EmailClient
from modules.check_email import check_emails
from modules.read_process_ia import OutputCounter
from dotenv import dotenv_values
from ultralytics import YOLO
from pathlib import Path
from time import sleep
import schedule

def main(*, model_path: Path, input_images_path: Path, processed_images_path: Path, bouding_box_processed_images_path: Path, error_images_path: Path, yolo_predict_path: Path,
            schedule_time_seconds: float, schedule_time_frequency_seconds: float):

    model = YOLO(model = model_path)

    counter = OutputCounter(
        model = model,
        input_images_path = input_images_path,
        processed_images_path = processed_images_path,
        bouding_box_processed_images_path = bouding_box_processed_images_path,
        error_images_path = error_images_path,
        yolo_predict_path = yolo_predict_path
    )

    schedule.every(schedule_time_seconds).seconds.do(counter.count)

    #print("Executando verificação leitura de emails...")
    #print("Executando rotina de leitura das imagens...")
    #print("Use CTRL+C para interromper a execução.")
    while True:
        try:
            sleep(schedule_time_frequency_seconds)
            schedule.run_pending()

            #print("Sobre o processamento das imagens...")
            #print("Processado:", counter.processed_images)
            #print("Error:", counter.error_images, "\n")

        except KeyboardInterrupt:
            break
    
    print("Finalizando a rotina...")
    

if __name__ == "__main__":
    env_variables = dotenv_values(".env")

    model_path = Path(env_variables["MODEL_PATH"])
    input_images_path = Path(env_variables["INPUT_IMAGES_PATH"])
    processed_images_path = Path(env_variables["PROCESSED_IMAGES_PATH"])
    error_images_path = Path(env_variables["ERROR_IMAGES_PATH"])
    bouding_box_processed_images_path = Path(env_variables["BOUDING_BOX_PROCESSED_IMAGES_PATH"])
    yolo_predict_path = Path(env_variables["YOLO_PREDICT_PATH"])
    schedule_time_seconds = float(env_variables["SCHEDULE_TIME_SECONDS"])
    schedule_time_frequency_seconds = float(env_variables["SCHEDULE_TIME_FREQUENCY_SECONDS"])
    #imap_url = env_variables["IMAP_URL"]

    main(
        #imap_url = imap_url,
        model_path = model_path,
        input_images_path = input_images_path,
        processed_images_path = processed_images_path,
        error_images_path = error_images_path,
        bouding_box_processed_images_path = bouding_box_processed_images_path,
        yolo_predict_path = yolo_predict_path,
        schedule_time_seconds = schedule_time_seconds,
        schedule_time_frequency_seconds = schedule_time_frequency_seconds
    )