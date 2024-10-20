import logging
import datetime

def Logger():
    dt = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
    print(dt)
    file_path=fr"..\Logs\logs-{dt}.txt"
    print(file_path)
    logging.basicConfig(handlers=[logging.FileHandler(filename=file_path, mode="w"),
                                  logging.StreamHandler()],
                        level=logging.INFO,
                        format="%(asctime)s::%(levelname)s::%(msg)s",
                        force=True)
    return logging