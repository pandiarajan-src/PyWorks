"""FTP Utility module that sync a local folder and remote FTP server path.

Copyright (c) to Pandiarajan
Licensed under the MIT License

Purpose:
    This utility can be used as a export module or a script to sync a local folder and remote FTP path
    It is assumed that the remote FTP path directly lands into the required folder.
    It means the destination is FTP server landing path once it is connected.
    It copies the local folder file to FTP folder if it doesn't exists, if it exists then don't copy.
    TODO: This script will not check for property of the file (e.g: latest version or update file will not be copied)

"""
import os
import sys
import argparse
from io import StringIO
from ftplib import FTP
from FileNameChecker import check_spaces_in_filename_and_replace_with_underscore

my_arg_parser = argparse.ArgumentParser(prog='ftputils', description="FTP Utils need server name, user credentials")
my_arg_parser.add_argument('ServerName', metavar='servername', type=str, help="FTP server name to connect")
my_arg_parser.add_argument('Path', metavar='path', type=str, help="FTP server's directory location to sync")
my_arg_parser.add_argument('UserName', metavar='username', type=str, help="FTP server's user-name to connect")
my_arg_parser.add_argument('Password', metavar='password', type=str, help="FTP server's user-password to connect")


def validate_ftp_inputs(server_name, search_path, user_name, passwd):
    """Validate the given input before proceeding with FTP transaction.

    Arguments:
        server_name : Name of the FTP server where the files to be transfered
        search_path : Local folder path which needs to be synced with the given FTP server
        user-name   : User Name of FTP server to connect
        passwd      : Password of FTP server to connect

    Returns:
        True : If server_name and search_path is valid (no empty)
        False : If anyone server_name or search_path is not valid

    """
    if (len(server_name) <= 0) or (len(search_path) <= 0):
        print("server_name is empty")
        return False
    # It doesn't work quite well at this point.
    # if(len(user_name) <= 0) or (len(passwd) <= 0):
    #     user_name = passwd = "anonymous"
    print("server_name: {0}, search_path: {1}, user_name: {2}, password: {3}".format(server_name, search_path, user_name, passwd))
    return True


def sync_ftp_dir(local_folder_path_to_sync, server_name, user_name, passwd):
    """Syncronize the FTP server folder with the given local folder content. Copy new files and ignore old files.

    Arguments:
        local_folder_path_to_sync : Local folder path which needs to be synced with the given FTP server
        server_name : Name of the FTP server where the files to be transfered
        user-name   : User Name of FTP server to connect
        passwd      : Password of FTP server to connect

    Returns:
        A list of all the files that are transfered newly to the destination

    """
    # Files to be transfered to server via FTP
    files_transfered = []

    # Status of this method
    status = False

    # validate the given input
    if not validate_ftp_inputs(local_folder_path_to_sync, server_name, user_name, passwd):
        return (files_transfered, status)

    try:
        # Connect to FTP server with the given server-name, user credentials
        ftp = FTP(server_name)
        print("Connecting server {0} - State: {1} \n".format(server_name, ftp.login(user=user_name, passwd=passwd)))

        # Run recursively on all the files in the parent_folder and its sub folder.
        for local_dir_name, local_subdir_list, local_file_list in os.walk(local_folder_path_to_sync):
            remote_file_list = []
            print('Local: Files availability: dir_name {0}, it has subdir {1} and files {2}...'.format(local_dir_name, local_subdir_list, local_file_list))
            # print("Current FTP dir: {0}".format(ftp.pwd()))

            # Create a directory if it doesn't exists.
            # If the directory exists in FTP server then don't stop the program (exception error_perm with code 550)
            # If the exception is other than 550 (dir exists), then raise the exception to catch at outer exception block.
            # This exception block is required
            dir_index_from_parent = 0
            if local_dir_name != local_folder_path_to_sync:
                dir_to_sync = local_dir_name.replace(local_folder_path_to_sync, "")
                dir_exist_list = []
                dir_new_list = []
                for dir_part in dir_to_sync.split("\\"):
                    try:
                        if dir_part.strip() == "":
                            continue
                        ftp.mkd(str(dir_part))
                        dir_new_list.append(str(dir_part))
                    except Exception as in_ex:
                        if str(in_ex.args).find("550"):
                            dir_exist_list.append(dir_part)
                        else:
                            print(dir_part, str(in_ex.args))
                            raise in_ex
                    finally:
                        if dir_part.strip() != "":
                            ftp.cwd(dir_part)
                            dir_index_from_parent += 1
                        pass
                print("Remote: {0} directories are existing and {1} are newly created for the path {2}".format(dir_exist_list, dir_new_list, dir_to_sync))
            print("Remote: Current FTP dir: {0}\n".format(ftp.pwd()))
            # FTP gives the list of directory to std-out format
            # Hence store the given value in String stream and then parse it to get the list of files
            old_sysout = sys.stdout
            new_sysout = StringIO()
            sys.stdout = new_sysout
            ftp.dir()
            sys.stdout = old_sysout
            dir_result = new_sysout.getvalue().splitlines()
            for file_in_dir in dir_result:
                remote_file_list.append(file_in_dir.split(sep=" ")[-1])
            for file_name in local_file_list:
                if file_name in remote_file_list:
                    continue
                file_path = os.path.join(local_dir_name, file_name)
                ftp.storbinary('STOR ' + file_name, open(file_path, 'rb'))
                files_transfered.append(file_path)

            # Once all the file transfer to the specific FTP server directory is over go back to root dir
            index = dir_index_from_parent
            while index > 0:
                index -= 1
                ftp.cwd("..")

        ftp.quit()
        print("All FTP file transfer were completed successfully.")
        status = True
    except Exception as ex:
        ftp.quit()
        print("something went wrong : {0}".format(ex))
    return (files_transfered, status)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = my_arg_parser.parse_args()
        try:
            # Before passing the parameter to sync FTP, rename any files with space by underscore
            # This step is requested to avoid any issues coming due to space in the file name in both source and destination direcotry
            print("***********************************************************************")
            print("Remove Space in any file name before sync to Remote FTP directory")
            print("***********************************************************************")
            check_spaces_in_filename_and_replace_with_underscore(args.Path.strip())
            print("***********************************************************************")

            print("***********************************************************************")
            print("Start Executing Local Direcotry Sync to Remote FTP server")
            print("***********************************************************************")
            # Sync the local folder to a remote FTP server path
            files_transfered, status = sync_ftp_dir(local_folder_path_to_sync=args.Path.strip(), server_name=args.ServerName.strip(), user_name=args.UserName.strip(), passwd=args.Password.strip())
            if len(files_transfered) > 0:
                print("\nFollowing files are successfully synced between local and FTP server")
                for file_transfered in files_transfered:
                    print(file_transfered)
            else:
                print("\nBoth local dir {0} and FTP server {1} are in sync, no files are requrired to transfered".format(args.Path.strip(), args.ServerName.strip()))
            if status is True:
                print("SUCCESS: Execution Successful")
            else:
                print("FAILURE: Execution Failure, please analyze logs for more details")
        except Exception as ex:
            print("\nException occured at Main level {0}".format(ex))
            print("FAILURE: Execution Failure, please analyze logs for more details")
        pass
    pass
