from datetime import datetime

def sort_by_category_and_time(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        key_time = datetime.strptime(key["time"], "%Y-%m-%d %H:%M:%S")

        while j >= 0:
            curr_time = datetime.strptime(data[j]["time"], "%Y-%m-%d %H:%M:%S")

            if (data[j]["category"] > key["category"]) or \
               (data[j]["category"] == key["category"] and curr_time > key_time):
                data[j + 1] = data[j]
                j -= 1
            else:
                break

        data[j + 1] = key
    return data

def filter_by_category(data, category):
    return [item for item in data if item["category"].lower() == category.lower()]
