class Employee:
    def __init__(self, name, punctuality, quality_of_work, team_collaboration):
        self.name = name
        self.punctuality = punctuality
        self.quality_of_work = quality_of_work
        self.team_collaboration = team_collaboration

    @staticmethod
    def init_employee_data():
        employee_data = []
        for i in range(5):
            name = "Fadil" if i == 0 else "Shinta" if i == 1 else "Anggita" if i == 2 else "Rahman" if i == 3 else "Failsal"
            punctuality = 70 if i == 0 else 65 if i == 1 else 90 if i == 2 else 60 if i == 3 else 80
            quality_of_work = 80 if i == 0 else 75 if i == 1 else 85 if i == 2 else 70 if i == 3 else 75
            team_collaboration = 85 if i == 0 else 70 if i == 1 else 95 if i == 2 else 65 if i == 3 else 85
            employee_data.append(Employee(name, punctuality, quality_of_work, team_collaboration))
        return employee_data

def average_employee_performance(data):
    result = []
    for e in data:
        average = (e.punctuality + e.quality_of_work + e.team_collaboration) / 3
        result.append({"name": e.name, "average": average})
    return result

def shorting_data(data):
    result = data
    for i in range(len(result)):
        max_index = i
        for j in range(i+1, len(result)):
            if result[j]["average"] > result[max_index]["average"]:
                max_index = j
        result[i], result[max_index] = result[max_index], result[i]
    return result

if __name__ == "__main__":
    data = Employee.init_employee_data()
    average_data = average_employee_performance(data)
    shorted_data = shorting_data(average_data)
    print("Hasil evaluasi kinerja karyawan (diurutkan dari yang tertinggi):")
    for e in shorted_data:
        print(f"Name: {e['name']}, Average Performance: {e['average']}")