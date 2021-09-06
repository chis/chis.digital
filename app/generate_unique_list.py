def generate_unique_list(unique_list):
    unique_set = set()
    for unique in unique_list:
        unique_set.add(unique)
    unique_set_list = list(unique_set)
    unique_set_list.sort()
    return unique_set_list
