import os


def chech_path(path):
    if not os.path.exists(path):
        print('Path is invalid or does not exist.\nPress Enter to close.')
        input()
        exit(1)

    if not os.path.exists(path + 'Beat Saber_Data/CustomLevels'):
        print('Cannot find Beat Saber_Data or Custom Levels folder, please check the path.\nPress Enter to close.')
        input()
        exit(1)

    if not os.path.exists(path + 'Playlists'):
        print('Cannot find Playlists folder, please check the path.\nPress Enter to close.')
        input()
        exit(1)