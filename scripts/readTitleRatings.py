import csv
import sys

""" [0] = titleId
    [1] = averageRating
    [2] = numOfVotes
"""
csv.field_size_limit(sys.maxsize)
"""titleId, averageRating"""
titlesData = [[0, 0]]

with open("title.ratings.tsv") as file:
    titles = csv.reader(file, delimiter="\t")
    i = 0
    for line in titles:
        temp = []
        if i != 0:
                temp.append(int(line[0][2:]))  # titleID
                temp.append(line[1])  # averageRating
                titlesData.append(temp)
        i += 1

sqlFile = open("title.ratings.sql", "w")
for value in titlesData:
    preparedSql = "update media set imdbRating=%s where titleid = %s;\n" % (value[1], value[0])
    sqlFile.write(preparedSql)
