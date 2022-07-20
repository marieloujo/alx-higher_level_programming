#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # return list(map(lambda x : replace if x is search x replace, my_list))
    return [replace if elm is search else elm for elm in my_list]
