import csv
import json

output_data = []

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")
    for row in reader:
        title = row["PRIMARYTITLE"]
        if row["DIRECTOR"].strip():
            directors = [d.strip() for d in row["DIRECTOR"].split(",")]
        else:
            directors = []

        if row["CAST"].strip():
            cast = [c.strip() for c in row["CAST"].split(",")]
        else:
            cast = []

        genres = [g.strip() for g in row["GENRES"].split(",")]
        year = int(row["STARTYEAR"])
        decade = year - (year % 10)

        movie_dict = {
            "title": title,
            "directors": directors,
            "cast": cast,
            "genres": genres,
            "decade": decade
        }
        output_data.append(movie_dict)

with open("hw02_output.json", mode="w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4)