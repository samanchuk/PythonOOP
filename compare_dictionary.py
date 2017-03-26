#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

basic_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'j': 88}

comp_dict_1 = {'k': 5, 'n': 2, 'c': 11}
comp_dict_2 = {'a': 1, 'b': 2, 'c': 3}
comp_dict_3 = {'a': 1, 'b': 77, 'c': 88, 'd': 6}
comp_dict_4 = {'a': 100, 'b': 77, 'c': 88, 'd': 6}
comp_dict_5 = {'a': 1, 'b': 1}


def dict_comparison(dict_to_comp):
    founded = False
    for key in dict_to_comp.keys():
        founded = True if key in basic_dict.keys() and dict_to_comp.get(key) == basic_dict.get(key) else False
    return founded

print(dict_comparison(comp_dict_1))
print(dict_comparison(comp_dict_2))
print(dict_comparison(comp_dict_3))
print(dict_comparison(comp_dict_4))
print(dict_comparison(comp_dict_5))