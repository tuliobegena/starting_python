with open("raw_data.txt", "r") as data_file:
    raw_data = data_file.read()

separated_rows = raw_data.split("\n")
separated_words = []
final_list = []

for i in separated_rows:
    separated_words.append(i.split())

for i in separated_words:
    data = i[1].strip(",")
    final_list.append(f"{data}\n")

with open("clean_data.txt", "w") as clean_data:
    for i in final_list:
        clean_data.write(i)