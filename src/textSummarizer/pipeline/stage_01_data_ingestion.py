from src.textSummarizer.config.configurtion import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import logger
import os
import yaml

class DataIngestionTrainingPipeline:
    def __init__(self):
        self.config = self.load_config()  # Load configuration on initialization
        self.data_ingestion = DataIngestion(self.config['data_ingestion'])  # Pass data ingestion config to DataIngestion

    def load_config(self):
        # Load configuration from the correct YAML file path
        try:
            # Use the correct path to your config.yaml file
            with open("D:/Text Summarizer Project/Text-Summarizer-Project-/config/config.yaml", 'r') as config_file:
                config = yaml.safe_load(config_file)
                logger.info("Configuration loaded successfully.")
                return config
        except FileNotFoundError as e:
            logger.error(f"Configuration file not found: {e}")
            raise  # Optionally re-raise the error after logging

    def main(self):
        # Example of how to use data ingestion
        logger.info(f"Data ingestion configuration: {self.config['data_ingestion']}")
        # Check for specific config items
        if 'source_url' in self.config['data_ingestion']:
            logger.info(f"Source URL: {self.config['data_ingestion']['source_url']}")
            self.data_ingestion.download_file() # Call the method to download data
        else:
            logger.warning("Source URL not found in the configuration.")

# You can now run the pipeline
if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
