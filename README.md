# Daily Data Collector 🕒📊

A Python automation project that periodically collects data from a public API, cleans it, and stores structured output.  
The project is fully config-driven, logged, and runs automatically using a scheduler.

---

## 🚀 Features

- API data collection using `requests`
- Config-driven architecture (no hardcoded values)
- Data cleaning using `pandas`
- CSV-based data storage
- Centralized logging
- Time-based scheduling (minutely / hourly / daily)
- Safe and repeatable pipeline execution

---

## 📁 Project Structure

    project/
    ├── main.py               # Entry point & scheduler
    ├── data_collector.py     # API data collection logic
    ├── data_cleaner.py       # Data cleaning logic
    ├── config/
    │   └── config.json       # Central configuration
    ├── data/
    │   ├── raw.csv           # Raw collected data
    │   └── output.csv        # Cleaned data
    ├── logs/
    │   └── app.log           # Application logs
    ├── requirements.txt
    └── README.md
▶️ How It Works

Loads configuration from config.json

Sends an HTTP request to the configured API

Validates the response

Saves raw data to CSV

Cleans the data (removes empty rows / duplicates)

Saves cleaned data to output CSV

Logs each step

Repeats automatically based on schedule

▶️ How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start the automation
python main.py


The pipeline will now run automatically according to the configured schedule.

📝 Logging

Logs are written to the file defined in the config:

logs/app.log


Each run records:

Pipeline start and completion

Collection status

Cleaning status

Errors (if any)

🧠 Design Notes

The pipeline is idempotent: each run creates a fresh snapshot of data.

The scheduler controls when the pipeline runs, not what data is returned.

The project is designed to be easily extended to:

Database storage

Historical data tracking

Multiple data sources

✅ Status

This project demonstrates a complete, real-world Python automation workflow and serves as a strong foundation for advanced automation and data engineering tasks.


---
