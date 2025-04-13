# Updating Components
import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        """
        Function to download the file from the URL
        Function returns None
        """
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from: {self.config.source_URL}")

            filename, ext = os.path.splitext(os.path.basename(self.config.source_URL))

            # Download the file
            request.urlretrieve(self.config.source_URL, self.config.local_data_file)

            # Check if the file is downloaded
            if os.path.exists(self.config.local_data_file):
                logger.info(f"File downloaded: {filename}{ext}")
                # logger.info(f"File size: {get_size(self.config.local_data_file)}")
            else:
                raise Exception("File not downloaded")
        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)