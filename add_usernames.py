import json
import os
from pathlib import Path
from typing import TextIO
import argparse


def load_user_data_from_disk(user_data_path: str) -> json:
    """ Load the slack user data from the given path

    :param user_data_path: path to the file with the user data.
    :return: a json object with information about all slack users.
    """

    print('Loading user data from {}'.format(user_data_path))
    with open(user_data_path, 'r') as f:
        user_data = json.load(f)

    return user_data


def extract_usernames(user_data: json) -> dict:
    """ Extracts the usernames and ids for all the users in the given user data.

    :param user_data: the data containing information about all the slack users.
    :return: a dictionary with user ids as keys and usernames as values.
    """

    print('Extracting usernames')
    usernames_by_id = {}
    for user_info in user_data:
        user_id = user_info['id']
        username = user_info['profile']['display_name']
        usernames_by_id[user_id] = username
    return usernames_by_id


def add_usernames_to_messages_in_directory(root_path: str, usernames_by_id: dict) -> None:
    """ Goes through the given directory recursively and adds usernames to all the messages stored there.

    The updated message files will be saved in a directory called <root_path>_with_names.
    This directory is saved in the parent directory of the root folder.
    :param root_path: the path to the root directory.
    :param usernames_by_id: dict containing the usernames identified by user ids.
    """
    absolute_root_dir = Path(root_path).absolute()
    target_dir = '{}_with_names'.format(absolute_root_dir)

    print('New files saved to {}'.format(target_dir))

    paths = Path(root_path).glob('**/*.json')
    for path in paths:
        absolute_path = path.absolute()
        if absolute_path.parent == absolute_root_dir:
            continue
        print('Adding usernames to messages in {}'.format(absolute_path))
        source_path = str(absolute_path)
        target_path = source_path.replace(str(absolute_root_dir), target_dir)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(str(path), 'r') as source, open(target_path, 'w') as target:
            add_usernames_to_messages_in_file(source, target, usernames_by_id)


def add_usernames_to_messages_in_file(source_file: TextIO, target_file: TextIO, usernames_by_id: dict) -> None:
    """ Adds usernames to the messages in the source file and saves the file as as the target file.

    Notes:
     - Messages from bots (not containing any 'user' fields are not included in the output.
     - Messages from users not included in the user data will be marked as UNKNOWN

    :param source_file: the path to the source file.
    :param target_file: the path to the target file.
    :param usernames_by_id: dict containing the usernames identified by user ids.
    """

    message_list = json.load(source_file)

    for message in message_list:
        id = message.get('user', None)
        if id:
            message['user_name'] = usernames_by_id.get(id, "UNKNOWN")
    json.dump(message_list, target_file)


def process_data_dump_directory(root_folder_path: str) -> None:
    clean_root_folder_path = root_folder_path.rstrip(os.sep)
    user_data_path = os.path.join(clean_root_folder_path, 'users.json')
    user_data = load_user_data_from_disk(user_data_path)

    usernames_by_id = extract_usernames(user_data)

    add_usernames_to_messages_in_directory(clean_root_folder_path, usernames_by_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add usernames to Slack messages,')
    parser.add_argument('root_path', metavar='P', type=str, help='The path to the folder containing the data dump.')

    args = parser.parse_args()

    process_data_dump_directory(args.root_path)

