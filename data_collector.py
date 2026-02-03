
import requests
import logging
import csv


def run_collector(config):

    try:
        #Intializing info needed from config
        paths = config["paths"]
        source = config["source"]
        extraction = config["extraction"]

        #Getting data for collection from config
        raw_data = paths["raw_data"]
        url = source["url"]
        timeout = source["timeout_seconds"]
        fields = extraction["fields"]

        logging.info("data collector started")

        #checking status code and log error/success
        response = requests.get(url ,timeout=timeout)
        if response.status_code != 200:
            logging.error("Request failed")
            return False

        #getting data and validation for right format
        data = response.json()

        if not isinstance(data, list):
            logging.error("wrong json format")
            return False

        #writing raw data to csv file using fields
        with open(raw_data, "w" ,newline="") as raw_data_file:
            writer = csv.writer(raw_data_file)
            writer.writerow(fields)

            for item in data:
                row = []
                for field in fields:
                    value = item.get(field)
                    row.append(value)
                writer.writerow(row)
            logging.info("data collected successfully")
            return True

    except requests.exceptions.RequestException as e:
        logging.error(e)
        return False