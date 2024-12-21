import csv

left_list = []
right_list = []

def day1_solution(file_name):
    with open(file_name, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            left_value, right_value = row[0].split('   ')
            left_list.append(int(left_value))
            right_list.append(int(right_value))
        left_list.sort()
        right_list.sort()
        if(len(left_list) != len(right_list)):
            print("Error, list lengths are not equal!")
            return
        some_of_distances = 0
        for i in range(0, len(left_list)):
            some_of_distances = some_of_distances + abs(left_list[i] - right_list[i])
        print(some_of_distances)


file_name = 'personal_list.csv'

day1_solution(file_name)