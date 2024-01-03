
def extract_data():
    print("[INFO] Extracting files from university_results.")
    from scripts.helper_functions import list_unprocessed_local_files, extract_csv
    from os.path import join 

    file_path = join("sources", "university_results")
    unprocessed = list_unprocessed_local_files(file_path)
    extracted_data = [extract_csv(file_name, file_path) for file_name
                      in unprocessed]
    print("[INFO] Extracted " + str(len(unprocessed)) 
          + " files from university results for loading.")
    return extract_data

def transform_data(table):
    pass

def load_data(table, cursor, connection):
    pass