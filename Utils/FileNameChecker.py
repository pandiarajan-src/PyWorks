"""Check space character in a file, if it exists replace it with _ (underscore).

Copyright (c) to Pandiarajan
Licensed under the MIT License

Purpose:
    In many situation we encounter a problem due to the presence of space in file name.
    This file can be used to rename all the files in a direcotry and its sub-directory with space by using _.

Arguments:
    dir_path : Directory name where the files and its sub-directory to be searched.

"""
import os
import sys
import argparse

my_arg_parser = argparse.ArgumentParser(prog='FileNameChecker', description="File name check and replace if space exists")
my_arg_parser.add_argument('DirName', metavar='directoryname', type=str, help="Directory name to search for file and sub-directory")


def check_spaces_in_filename_and_replace_with_underscore(dir_path):
    """Check all the files in the given directory and sub-directory has space in its name, if so replace it with _ (underscore).

    Arguments:
        dir_path = Direcotry path where to search for files and sub-directory files

    Return:
        status = True for success or False
        it may raise an exception if there is any problem in the code execution.

    """
    for dir_name, subdir, file_list in os.walk(dir_path):
        print('\nFiles availability: dir_name {0}, it has subdir {1} and files {2}...'.format(dir_name, subdir, file_list))
        try:
            renamed_files = []
            for file_name in file_list:
                if ' ' in file_name:
                    src_file = os.path.join(dir_name, file_name)
                    dest_file = os.path.join(dir_name, file_name.replace(" ", "_"))
                    os.rename(src_file, dest_file)
                    renamed_files.append(dest_file)
            if len(renamed_files) > 0:
                print("Renamed files are following:")
                print('\n'.join(map(str, renamed_files)))
            else:
                print('No files in "{0}" contains space, so no change'.format(dir_name))
        except Exception as ex:
            print("Exception occured: {0}".format(ex))


if __name__ == "__main__":
    args = my_arg_parser.parse_args()
    check_spaces_in_filename_and_replace_with_underscore(dir_path=args.DirName)
    pass
