#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Use the symmetric difference operator to find elements in only one set
    diff_set = set_1 ^ set_2
    return diff_set

# Example usage:
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
