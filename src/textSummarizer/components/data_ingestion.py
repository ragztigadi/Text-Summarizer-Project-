import os
import urllib.request as request
import zipfile
from src.textSummarizer.utils.common import get_size

from pathlib import Path
from src.textSummarizer.entity import DataIngestionConfig




import os
import requests
import zipfile
import logging
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config
        # Create the necessary directories
        self.create_directories()

    def create_directories(self):
        """Create necessary directories for data ingestion."""
        try:
            os.makedirs(self.config['root_dir'], exist_ok=True)
            logger.info(f"Root directory created at: {self.config['root_dir']}")
        except Exception as e:
            logger.error(f"Error creating root directory: {e}")

        try:
            os.makedirs(os.path.dirname(self.config['local_data_file']), exist_ok=True)
            logger.info(f"Directory for local data file created at: {os.path.dirname(self.config['local_data_file'])}")
        except Exception as e:
            logger.error(f"Error creating directory for local data file: {e}")

        try:
            os.makedirs(self.config['unzip_dir'], exist_ok=True)
            logger.info(f"Unzip directory created at: {self.config['unzip_dir']}")
        except Exception as e:
            logger.error(f"Error creating unzip directory: {e}")

    def download_file(self):
        """Download file from the source URL."""
        try:
            logger.info(f"Downloading file from {self.config['source_url']}...")
            response = requests.get(self.config['source_url'])
            if response.status_code == 200:
                with open(self.config['local_data_file'], 'wb') as file:
                    file.write(response.content)
                logger.info("File downloaded successfully.")
            else:
                logger.error(f"Failed to download file: {response.status_code}")
        except Exception as e:
            logger.error(f"Error downloading file: {e}")

    def extract_zip_file(self):
        """Extract the downloaded zip file."""
        try:
            logger.info(f"Extracting {self.config['local_data_file']} to {self.config['unzip_dir']}...")
            with zipfile.ZipFile(self.config['local_data_file'], 'r') as zip_ref:
                zip_ref.extractall(self.config['unzip_dir'])
            logger.info("Files extracted successfully.")
        except zipfile.BadZipFile:
            logger.error("Error: The downloaded file is not a valid zip file.")
        except Exception as e:
            logger.error(f"An error occurred while extracting the zip file: {e}")

# Load configuration from the YAML file
try:
    with open("D:/Text Summarizer Project/Text-Summarizer-Project-/config/config.yaml", 'r') as config_file:
        config = yaml.safe_load(config_file)
        logger.info("Configuration loaded successfully.")
except FileNotFoundError as e:
    logger.error(f"Configuration file not found: {e}")
    raise

# Usage
data_ingestion_config = config['data_ingestion']
data_ingestion = DataIngestion(data_ingestion_config)

# Run the download and extraction processes
data_ingestion.download_file()
data_ingestion.extract_zip_file()
