
from collections import Counter


def read_file(file_name):
    file = open(file_name, 'r')
    data_list = file.read().splitlines()
    file.close()
    return data_list


numbers_list = read_file('sirens_fxt.txt')

occurrences = Counter(numbers_list)

values = tuple(occurrences.values())

counter_uniques = Counter(values)
number_unique = counter_uniques[1]
number_repeating = len(values) - counter_uniques[1]

print(
    f"Le fichier contient {number_unique} numéros SIREN uniques et {number_repeating} numéros répétés au moins deux fois.")
