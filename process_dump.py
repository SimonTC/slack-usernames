import zipfile
from tempfile import TemporaryDirectory
import argparse
import os
from pathlib import Path
import shutil

from add_usernames import process_data_dump_directory

def process_zip_file(path_to_zip, extraction_dir) -> str:
    """ Process the data dump in the given zip file.

    :param path_to_zip: Path to the zip file for the data dump.
    :param extraction_dir: Path to the directory where the zip contains are extracted for processing.
    :return: Path to the directory of the processed messages in the data dump.
    """

    print("Processing data dump in {}".format(path_to_zip))
    zip_ref = zipfile.ZipFile(path_to_zip, 'r')
    zip_ref.extractall(extraction_dir)
    zip_ref.close()

    output_dir = process_data_dump_directory(extraction_dir)

    return output_dir

def process_data_dir(root_path: str) -> None:
    """ Process all data dump zip files in given directory.

    :param root_path: Path to the directory with the data dump zip files.
    """

    clean_root_folder_path = root_path.rstrip(os.sep)
    clean_root_folder_path = str(Path(clean_root_folder_path).absolute())

    with TemporaryDirectory(dir=clean_root_folder_path) as temp_root_dir:
        print("Temp root: " + temp_root_dir)

        for file in os.listdir(clean_root_folder_path   ):
            if file.endswith(".zip"):
                zip_path = os.path.join(clean_root_folder_path, file)
                filename = os.path.splitext(file)[0]
                extraction_dir = os.path.join(temp_root_dir, filename)

                output_dir = process_zip_file(zip_path, extraction_dir )

                output_zip_file_path = os.path.join(root_path, '{} with names'.format(filename))
                shutil.make_archive(output_zip_file_path, 'zip', output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add usernames to messages from Slack data dumps')
    parser.add_argument('root_path', metavar='P', type=str, help='The path to the folder containing the zip files with the slack data')

    args = parser.parse_args()

    process_data_dir(args.root_path)

