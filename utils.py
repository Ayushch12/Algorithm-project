from datetime import datetime

# Insertion sort by category
def sort_by_category(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j]["category"].lower() > key["category"].lower():
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Insertion sort by YEAR only
def sort_by_year(data):
    for i in range(1, len(data)):
        key = data[i]
        key_year = int(key["time"][:4])
        j = i - 1
        while j >= 0 and int(data[j]["time"][:4]) > key_year:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Insertion sort by datetime only
def sort_by_datetime(data):
    for i in range(1, len(data)):
        key = data[i]
        key_time = datetime.strptime(key["time"], "%Y-%m-%d %H:%M:%S")
        j = i - 1
        while j >= 0:
            current_time = datetime.strptime(data[j]["time"], "%Y-%m-%d %H:%M:%S")
            if current_time > key_time:
                data[j + 1] = data[j]
                j -= 1
            else:
                break
        data[j + 1] = key
    return data


# Linear search to filter by category
def filter_by_category(data, category):
    result = []
    for item in data:
        if item["category"].lower() == category.lower():
            result.append(item)
    return result
