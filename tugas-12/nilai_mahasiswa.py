import pandas as pd
from tabulate import tabulate 

class Student:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_list_student():
        result = []
        for i in range(5):
            name = "Dian" if i == 0 else "Adit" if i == 1 else "Fardani" if i == 2 else "Cintya" if i == 3 else "Kamelia"
            value = 78 if i == 0 else 70 if i == 1 else 85 if i == 2 else 65 if i == 3 else 95
            result.append(Student(name=name, value=value))

        if result:
            student_df = [{"Nama": item.name, "Nilai": item.value} for item in result]
            df = pd.DataFrame(student_df)
            print(tabulate(df.values, headers=df.columns, tablefmt="grid"))

        return result
    
    def search_student(self, student_data):
        if student_data:
            choice = input("Cari nama mahasiswa : ")
            for e in student_data:
                if choice.lower() == e.name.lower():
                    return True
            retry_choice = str(input("Siswa tidak ditemukan, Apakah anda ingin mengulanginya (y/n) ? : "))
            if retry_choice.lower() == 'y':
                return self.search_student(self, student_data)
            elif retry_choice.lower() == 'n':
                print("Baiklah...")
                return False
            else:
                print("Inputan anda tidak valid (y/n)")
                return self.search_student(self, student_data)                   

        else:
            print("Data siswa tidak diteukan")
            return False
    

if __name__ == "__main__":
    siswa = Student
    data_siswa = siswa.get_list_student()
    siswa_result = siswa.search_student(siswa, data_siswa)
    print(siswa_result)
