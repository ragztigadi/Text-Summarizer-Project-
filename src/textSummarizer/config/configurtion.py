
from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories

from src.textSummarizer.entity import (DataIngestionConfig)


from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from pathlib import Path
from dataclasses import dataclass

from pathlib import Path

# Use absolute paths for the config and params file
CONFIG_FILE_PATH = Path("D:/Text Summarizer Project/Text-Summarizer-Project-/config/config.yaml")
PARAMS_FILE_PATH = Path("D:/Text Summarizer Project/Text-Summarizer-Project-/params.yaml")


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

class ConfigurationManager:
    def __init__(
            self,
            config_filepath: Path = CONFIG_FILE_PATH,
            params_filepath: Path = PARAMS_FILE_PATH):
        
        # Reading the YAML configuration files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Creating the directories mentioned in the config file
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Create directories for data ingestion
        create_directories([config.root_dir])

        # Creating the data ingestion configuration object
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),         # Converting to Path object if not already
            source_URL=config.source_URL,           # URL for data source
            local_data_file=Path(config.local_data_file),  # Path for the local data file
            unzip_dir=Path(config.unzip_dir)        # Path for the directory to unzip files
        )

        return data_ingestion_config
