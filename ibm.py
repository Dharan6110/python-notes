import math
from statistics import mode

def euclidean_distance(point1, point2):
    return math.floor(math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2))

def calculate_distances(point_list):
    distances = [euclidean_distance(point_list[i], point_list[i+1]) for i in range(len(point_list)-1)]
    return distances

point_coordinates = [(4,2),(-11, 3), (8, 5), (-3, 2), (9, 17)]
distances = calculate_distances(point_coordinates)
result_mode = mode(distances)

print(result_mode)



# import re

# def classify_switch(model_number, port_count, is_stacked):
#     model_short = re.search(r'[A-Za-z]+(\d+)[A-Za-z]*', model_number).group(1)
    
#     if model_short in ['5200', '5250', '5270'] and port_count <= 24:
#         return "Type 1 switch"
#     elif model_short in ['5200', '5250', '5270', '5300', '5350', '5370'] and model_short != '5400' and port_count > 24:
#         return "Type 2 switch"
#     elif is_stacked:
#         return "Core switch"
#     else:
#         return "Unknown switch type"

# # Example usage:
# model_number_1 = "C5200L-12P"
# port_count_1 = 12
# is_stacked_1 = False

# model_number_2 = "C5250L-32P-2T"
# port_count_2 = 32
# is_stacked_2 = False

# model_number_3 = "C5400-48P"
# port_count_3 = 48
# is_stacked_3 = True

# print(classify_switch(model_number_1, port_count_1, is_stacked_1))
# print(classify_switch(model_number_2, port_count_2, is_stacked_2))
# print(classify_switch(model_number_3, port_count_3, is_stacked_3))



# import re

# def classify_switch(model_number, port_count, is_stacked):
#     model_short = re.search(r'[A-Za-z]+(\d+)[A-Za-z]*', model_number).group(1)
    
#     if model_short in ['5200', '5250', '5270'] and port_count <= 24:
#         return "Type 1 switch"
#     elif model_short in ['5200', '5250', '5270', '5300', '5350', '5370'] and model_short != '5400' and port_count > 24:
#         return "Type 2 switch"
#     elif is_stacked:
#         return "Core switch"
#     else:
#         return "Unknown switch type"

# # Example usage:
# model_1, port_1, stacked_1 = "C5200L-12P", 12, False
# model_2, port_2, stacked_2 = "C5250L-32P-2T", 32, False
# model_3, port_3, stacked_3 = "C5400-48P", 48, True

# print(classify_switch(model_1, port_1, stacked_1))
# print(classify_switch(model_2, port_2, stacked_2))
# print(classify_switch(model_3, port_3, stacked_3))


# def classify switch(model_number, placementlelo): 
#     model_numeric.join(c for c in model_number if c.isdigit())

#     placementlelo = int(placementlelo)

#     if model_numeric in ['5200', '5250', '5270'] and placementlelo <= 24:
#         return "Type 1"

#     elif model_numeric in ['5200', '5250', '5270', '5300', '5350', '5370'] and placementlel0 >24 or model_numeric == '5400':
#         return "Type 2"

#     elif "-S" in model_number or model_number.endswith("NX"): 
#         return "Core"

#     else:
#         return "Unknown"
# from scipy.spatial.distance import euclidean
# from statistics import mode

# def calculate_euclidean_distance(point1, point2):
#     return euclidean(point1, point2)

# def calculate_distances(coordinates):
#     distances = [calculate_euclidean_distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(i + 1, len(coordinates))]
#     return distances

# def find_mode_of_distances(distances):
#     return mode(distances)

# # Example usage:
# point_coordinates = [(-11, 3), (20, 21)]
# distances = calculate_distances(point_coordinates)
# mode_distance = find_mode_of_distances(distances)

# print(f"The Euclidean distances are: {distances}")
# print(f"The mode of the distances is: {mode_distance}")