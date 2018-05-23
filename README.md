# Slack Usernames 
A small script to add usernames to Slack messages in a Slack data dump.

### Prerequisites
- Python 3
- A data dump from Slack containing messages and user data.

### Usage
```
python3 add_usernames.py [path_to_data]
```
where `path_to_data` is the path to the folder containing the unpacked Slack data dump. The path can either be relative or absolute.
This folder has to contain the file `users.json` containing the list of Slack users. It should be included in
the data dump by default.

The output of the script will be added to a new folder called `[path_to_data]_with_names` placed in the same location as the original data folder.

### Example
Folder structure before the script is called:
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

Folder structure after the script has been called:
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

### License
This project is licensed under the terms of the MIT license.