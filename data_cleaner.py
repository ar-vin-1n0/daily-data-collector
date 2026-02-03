import pandas as pd
import logging
from pathlib import Path

def run_data_cleaning(config):

    try:
        paths = config['paths']
        cleaning = config['cleaning']
        extraction = config['extraction']

        fields = extraction['fields']
        remove_empty_rows = cleaning['remove_empty_rows']
        remove_duplicates = cleaning['remove_duplicates']

        clean_data = paths['clean_data']
        raw_data = paths['raw_data']

        required_field = extraction['required_field']

        path = Path(raw_data)
        if not path.exists():
            logging.error("cleaning failed raw data doesn't exist")
            return False

        logging.info("cleaning raw data started")
        df = pd.read_csv(raw_data)
        df.replace("", pd.NA, inplace=True)

        if df.empty:
            logging.error("cleaning failed raw data empty")
            return False

        missing_columns = []
        for column in fields:
            if column not in df.columns:
                missing_columns.append(column)
        if missing_columns:
            logging.error(f"cleaning failed missing columns: {missing_columns}")

        if remove_empty_rows :
            df = df.dropna(subset=required_field)
            logging.info(f"removed empty rows | {len(df)}")


        if remove_duplicates:
            df = df.drop_duplicates()
            logging.info(f"removed duplicate rows| {len(df)}")

        df.to_csv(clean_data, index=False)
        logging.info(f"cleaned data saved | total records saved :{len(df)}")
        return True

    except Exception as e:
        logging.error(e)
        return False









