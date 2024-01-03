import tomllib
import sqlite3

with open("config/config.toml","rb") as file_path:
    config = tomllib.load(file_path)
source_names = config['source']['name']

if __name__ == '__main__':
    print("[INFO] Running ETL process for " + str(source_names))
    for source in source_names:
        exec("from scripts import " + source)
        connection = sqlite3.connect("sources/" + source + ".db")
        cursor = connection.cursor()
        tables = eval(source + ".extract_data()")
        for table in tables:
            transformed_data = eval(source + ".transform_data(table)")
            load_data = eval(source + ".load_data(table, cursor, connection)")
        print("[INFO] ETL completed for " + source)

