#!/usr/bin/env python3
import os
import argparse
import requests

def download_dataset(url, output_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        with open(output_path, "wb") as file:
            file.write(response.content)

        print("Dataset downloaded successfully and saved to:", output_path)
    except requests.exceptions.RequestException as e:
        print("Failed to download dataset:", e)

def main():
    parser = argparse.ArgumentParser(
        description="Download the raw Major Safety Events dataset from transportation.gov."
    )
    parser.add_argument(
        "--url", 
        default="https://data.transportation.gov/api/views/9ivb-8ae9/rows.csv?accessType=DOWNLOAD",
        help="The URL to download the dataset from."
    )
    parser.add_argument(
        "--data-dir", 
        default="data",
        help="The directory to save the downloaded dataset."
    )
    parser.add_argument(
        "--filename", 
        default="raw_data.csv",
        help="The filename to save the downloaded dataset as."
    )
    args = parser.parse_args()

    # Ensure the data directory exists
    os.makedirs(args.data_dir, exist_ok=True)
    output_path = os.path.join(args.data_dir, args.filename)

    download_dataset(args.url, output_path)

if __name__ == "__main__":
    main()
