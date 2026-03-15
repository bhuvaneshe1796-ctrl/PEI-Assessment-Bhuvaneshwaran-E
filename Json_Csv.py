import pandas as pd

file1 = "Shipping.json"
file2 = "Shipping_table.csv"

source_data = pd.read_json(file1)
target_data = pd.read_csv(file2)

common_columns = list(set(source_data.columns) & set(target_data.columns))

source_data = source_data[common_columns]
target_data = target_data[common_columns]

total_source_records = len(source_data)
total_target_records = len(target_data)

matched_records = source_data.merge(target_data, on=common_columns).drop_duplicates()
matched_count = len(matched_records)

source_only_records = source_data.merge(target_data, on=common_columns, how="left", indicator=True)
source_only_records = source_only_records[source_only_records["_merge"] == "left_only"]
source_only_count = len(source_only_records)

target_only_records = target_data.merge(source_data, on=common_columns, how="left", indicator=True)
target_only_records = target_only_records[target_only_records["_merge"] == "left_only"]
target_only_count = len(target_only_records)

print("\nComparison Results:")
print(file1, "vs", file2)
print("Total records in", file1, ":", total_source_records)
print("Total records in", file2, ":", total_target_records)
print("Matched records:", matched_count)
print("Records only in", file1, ":", source_only_count)
print("Records only in", file2, ":", target_only_count)