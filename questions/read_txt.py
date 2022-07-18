import csv
# from questions.models import Question

with open("sample.txt", "r") as fp:
    for row in csv.reader(fp, delimiter=':'):
        print(row)
        # Question.objects.create(field1=row[0], field2=row[1])