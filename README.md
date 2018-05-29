# Slack Usernames 
A small script to add usernames to Slack messages in a Slack data dump.

## Prerequisites
- Python 3
- A data dump from Slack containing messages and user data.

## Usage

### Processing single unpacked data dump
```
python3 add_usernames.py [path_to_data]
```
where `path_to_data` is the path to the folder containing the unpacked Slack data dump. The path can either be relative or absolute.
This folder has to contain the file `users.json` containing the list of Slack users. It should be included in
the data dump by default.

The output of the script will be added to a new folder called `[path_to_data]_with_names` placed in the same location as the original data folder.

#### Example
Folder structure before processing the data dump:
```
data/
    slack_data_dump/
        users.json
        /slack_channel_1
            2017-02-21.json
            2017-02-22.json
            2017-02-23.json
        /slack_channel_2
            2017-02-21.json
            2017-02-25.json
        ...
```

Call to process the data dump:
```
python3 add_usernames.py data/slack_data_dump
```

Folder structure after processing the data dump:
```
data/
    slack_data_dump/
        users.json
        /slack_channel_1
            2017-02-21.json
            2017-02-22.json
            2017-02-23.json
        /slack_channel_2
            2017-02-21.json
            2017-02-25.json
        ...
    slack_data_dump_with_names/
        /slack_channel_1
            2017-02-21.json
            2017-02-22.json
            2017-02-23.json
        /slack_channel_2
            2017-02-21.json
            2017-02-25.json
        ...

```

### Processing multiple zip files containing data dumps
```
python3 process_dump.py [path_to_data_folder]
```
where `path_to_data_folder` is the path to the folder containing the zip files for the data dumps. The path can either be relative or absolute.

An output zip file will be created for each input zip file in the data folder. The output zip files will contain the same messages as the input zip files with usernames added to the messages.

#### Example
Folder structure before processing the data dump:
```
data/
    slack_data_dump_1.zip
    slack_data_dump_2.zip
    slack_data_dump_3.zip
    ...
```

Call to process the data dump:
```
python3 process_dump.py data
```

Folder structure after processing the data dump:
```
data/
    slack_data_dump_1 with names.zip
    slack_data_dump_1.zip
    slack_data_dump_2 with names.zip
    slack_data_dump_2.zip
    slack_data_dump_3 with names.zip
    slack_data_dump_3.zip
    ...
```

## License
This project is licensed under the terms of the MIT license.