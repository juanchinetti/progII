#Merge de diccionarios:

def merge_diccionarios(dic1, dic2):
    dic_merged = dic1.copy()
    dic_merged.update(dic2)
    return dic_merged

print(merge_diccionarios({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  
