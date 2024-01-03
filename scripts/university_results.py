
def extract_data():
    print("[INFO] Extracting files from university_results.")
    from scripts.helper_functions import list_unprocessed_local_csvs, extract_csv
    from os.path import join 

    file_path = join("sources", "university_results")
    unprocessed = list_unprocessed_local_csvs(file_path)
    extracted_data = [extract_csv(file_name, file_path) for file_name
                      in unprocessed]
    print("[INFO] Extracted " + str(len(unprocessed)) 
          + " files from university results for loading.")
    return extracted_data

def transform_data(table):
    table = table.rename(columns={
        "Subject ID": "subject_id",
        "Subject Name": "subject_name",
        "Semester Taken": "semester",
        "Year Taken": "year",
        "Course Score": "score"
    })
    table['letter_grade'] = table.apply(lambda x: get_letter_grade(x['score']),
                                        axis = 1)
    print(table)

def load_data(table, cursor, connection):
    pass

###

def get_letter_grade(score):
    if   score >= 0  and score <= 49:
        return "F"
    elif score >= 50 and score <= 59:
        return "P"
    elif score >= 60 and score <= 69:
        return "CR"
    elif score >= 70 and score <= 79:
        return "D"
    elif score >= 80 and score <= 100:
        return "HD"
    else:
        return "Invalid"