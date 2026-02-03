import logging
import json
import schedule
import time

from pathlib import Path
from data_cleaner import run_data_cleaning
from data_collector import run_collector


# main pipline
def main(con):
    logging.info("pipline started")

    # collection
    if not run_collector(con):
        logging.error("Collector failed | pipline stopped")
        return False
    logging.info("Collection finished")

    # cleaning
    if not run_data_cleaning(con):
        logging.error("Data cleaning failed | pipline stopped")
        return False
    logging.info("Data cleaning completed")

    logging.info("pipline completed successfully")
    return True

if __name__ == "__main__":
    # logger
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO,
                        filename="logs/logs.log",
                        filemode='a')

    # config loader
    config_path = Path("config/config.json")
    if not config_path.is_file() or not config_path.exists():
        logging.error("Config file not found")
        SystemExit(1)
    with open(config_path) as json_file:
        config = json.load(json_file)


    #scheduler
    def do(comfig):
        main(config)

    scheduler = config['schedule']
    type_ = scheduler['type']
    frequency = scheduler['frequency']

    if type_ == 'daily':
        schedule.every().day.at(frequency).do(do, config)
    if type_ == 'hourly':
        schedule.every(int(frequency)).hours.do(do,config)
    if type_ == 'minutely':
        schedule.every(int(frequency)).minutes.do(do,config)

    while True:
        schedule.run_pending()
        time.sleep(1)
