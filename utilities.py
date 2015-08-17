# utility functions
from __future__ import division
from collections import OrderedDict

# imports for plots
import matplotlib 
matplotlib.use('SVG')
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
#import matplotlib.pyplot as plt
import pylab as pl
from mpld3 import fig_to_html

def sort_by_count(r):
    def key(r):
        return r[-1]        
    return sorted(r, key=key, reverse=True)

def get_total_count_tuple(tuple_list):
    sum = 0
    for eachtuple in tuple_list:
        sum += eachtuple[-1]
    return sum

def get_percentage(record, sum_of_counts):
    
    percentage = record[-1]/sum_of_counts
    percentage = round(100*percentage, 1)
    
    return percentage

################################# graphing ####################################
def create_graph(x, y):
    x.reverse()
    y.reverse()
    fig = plt.figure()

    width = .75
    ind = np.arange(len(x))
    plt.barh(ind, x)
    plt.yticks(ind + width / 2)
    ax = plt.gca()
    import textwrap
    ax.set_yticklabels([textwrap.fill(i, 25) for i in y])
    fig.tight_layout()

    figure_html=fig_to_html(fig)
    return figure_html




def create_results_dictionary(analysed_level):
    sorted_tuples = sort_by_count(analysed_level)
    sum_of_counts = get_total_count_tuple(analysed_level)
        
    # create dictionary to hold percentages
    results_dictionary = OrderedDict()
    for result in sorted_tuples:
        if result[0] != '':
            results_dictionary[result] = get_percentage(result, sum_of_counts)
        if len(results_dictionary) ==  10:
            break

    return results_dictionary, sum_of_counts

def results_graph(results_dictionary):
 	# array of descriptions
    #y = list(results_dictionary.keys())
    y = [r[0] for r in results_dictionary.keys()]
    #print(y)

    # array of counts
    x = list(results_dictionary.values())

    fig = create_graph(x, y)

    return fig