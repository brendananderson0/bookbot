def get_num_words(x):
    counter = len(x)
    return counter

def char_counter(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def report(dict_x):
    emptyl = []
    for i, count in dict_x.items():

        x = {
            "Letter": i,
            "Count": count
        }
        emptyl.append(x)

    def sort_by_count(i):
        return i["Count"]

    emptyl.sort(reverse=True, key=sort_by_count)
    return emptyl