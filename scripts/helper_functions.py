
def list_unprocessed_local_csvs(file_path):
    from os import listdir
    from os.path import isfile, join, splitext
    
    file_list = [file for file 
                 in listdir(file_path) 
                 if isfile(join(file_path, file))]
    unprocessed_files = [file_name for file_name 
                         in file_list 
                         if not file_name.startswith("LOADED-")
                         and splitext(file_name)[1] == ".csv"]
    return unprocessed_files

def extract_csv(file_name, file_path):
    from pandas import read_csv
    from os.path import join
    
    return read_csv(join(file_path, file_name))
