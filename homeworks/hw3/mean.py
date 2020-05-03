import csv

def mean() -> str:

    with open('hw.csv') as f:
        reader = csv.reader(f)
        next(reader)

        pounds_kg = 0.453592
        inches_cm = 2.54
        total_num_people = 0
        height_sum = 0
        weight_sum = 0

        for i in reader:
            total_num_people += 1
            height_sum += float(i[1])
            weight_sum += float(i[2])

        height_avg = round((height_sum / total_num_people) * inches_cm, 2)
        weight_avg = round((weight_sum / total_num_people) * pounds_kg, 2)

        return f' avg_height: {height_avg}  avg_weight: {weight_avg} '