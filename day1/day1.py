import csv

left_list = []
right_list = []


right_list_dict = {}


#Given a CSV of the input lists, compute the sum of the distances and the similarity between each.
def day1_solution(file_name):
    with open(file_name, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        

        #Iterate through each row in the CSV
        for row in csv_reader:
            #Since csv_reader can't have delimiters greater than one in character length, we split the string accordingly
            left_value, right_value = row[0].split('   ')
            
            #Convert each value from string type to int type
            left_value, right_value = int(left_value), int(right_value)

            #Add each value to the list
            left_list.append(left_value)
            right_list.append(right_value)
            
            #To compute the similarity, add the number of times the right value appears in the right list using a dictionary
            if right_value not in right_list_dict:
                right_list_dict[right_value] = 1
            else:
                right_list_dict[right_value] = right_list_dict[right_value] + 1
        
        #If the list lengths aren't equal
        if(len(left_list) != len(right_list)):
            print("Error, list lengths are not equal!")
            return
        
        #Timsort the lists in nlog(n) time such to compute the distance
        left_list.sort()
        right_list.sort()

        
        sum_of_distances = 0
        similarity = 0
        for i in range(0, len(left_list)):
            #For each index of the two arrays, find the distance. Since it is sorted, the smallest values of each list will be computed and then subtracted, and so on.
            sum_of_distances = sum_of_distances + abs(left_list[i] - right_list[i])

            #If the current number at the index is inside of the right list dictionary, compute the similarity and add it to the overall similarity.
            if left_list[i] in right_list_dict:
                similarity = similarity + (left_list[i] * right_list_dict[left_list[i]])
        print(sum_of_distances)
        print(similarity)


file_name = 'personal_list.csv'

day1_solution(file_name)