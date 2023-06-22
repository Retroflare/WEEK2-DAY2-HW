# Exercise 1 
# Given a list as a parameter, write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]., Your output should [1,5,8,9#

def numbers_less_than_ten(input_list):
    result = []
    for num in input_list:
        if num < 10:
            result.append(num)
    return result

# Example usage:
input_list = [1, 11, 14, 5, 8, 9]
output_list = numbers_less_than_ten(input_list)
print(output_list)


#Exercise 2 
#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2  (Merge the two lists here)
    merged_list.sort()   (Sort the merged list here)
    return merged_list


list1 = [1, 5, 3]
list2 = [2, 4, 6]
merged_sorted_list = merge_and_sort_lists(list1, list2)
print(merged_sorted_list)
