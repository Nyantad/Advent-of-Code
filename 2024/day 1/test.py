from collections import Counter

def read_file(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            try:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
            except ValueError:
                print(f"Skipping line due to ValueError: {line.strip()}")
    
    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    
    total_distance = 0
    for left, right in zip(sorted_left_list, sorted_right_list):
        total_distance += abs(left - right)
    
    return total_distance


def calculate_similarity_score(left_list, right_list):
    right_counter = Counter(right_list)
    similarity_score = 0
    for left in left_list:
        similarity_score += left * right_counter[left]
    
    return similarity_score


FILENAME = 'data.txt'

left_list, right_list = read_file(FILENAME)

total_distance = calculate_total_distance(left_list, right_list)
print("Total distance:", total_distance)

similarity_score = calculate_similarity_score(left_list, right_list)
print("Similarity score:", similarity_score)
