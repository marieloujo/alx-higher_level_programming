#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary)[0]
        for key, value in a_dictionary.items():
            if value > a_dictionary[max]:
                max = key
        return max
    return None
