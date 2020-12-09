DoctorDictionary = dict()
def TellDoctor():
    global DoctorDictionary
    with open('doctors_dataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        print(line_count)
TellDoctor()