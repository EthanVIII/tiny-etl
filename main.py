import tomllib
import sqlite3

with open("config.toml","rb") as file_path:
    config = tomllib.load(file_path)
source_names = config['source']['name']

if __name__ == '__main__':
    print("[INFO] Running ETL process for " + str(source_names))
    for source in source_names:
        exec("from scripts import " + source)
        connection = sqlite3.connect("sources/" + source + ".db")
        cursor = connection.cursor()
        tables = eval(source + ".extract_data()")
        print("[INFO] Extracted " + str(len(tables)) 
              + " files from university results for loading.")
        table_count = 1
        for table in tables:
            transformed_data = eval(source + ".transform_data(table)")
            print("[INFO] Data transformation complete for table " 
                  + str(table_count) 
                  + "/" + str(len(tables)))
            load_data = eval(source + ".load_data(table, cursor, connection)")
            print("[INFO] Data loading complete for table " 
                  + str(table_count) 
                  + "/" + str(len(tables)))
            table_count += 1
        print("[INFO] ETL completed for " + source)

