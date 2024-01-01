import tomllib
import sqlite3
import csv

with open("config/config.toml","rb") as file_path:
    config = tomllib.load(file_path)

source_names = config['source']['name']

print("Running ETL process for " + str(source_names))
for source in source_names:
    exec("from scripts import " + source)
    connection = sqlite3.connect("sources/" + source + ".db")
    cursor = connection.cursor()
    data = eval(source + ".extract_data()")
    transformed_data = eval(source + ".transform_data(data)")
    load_data = eval(source + ".load_data(data, cursor, connection)")
    print("ETL completed for " + source)

