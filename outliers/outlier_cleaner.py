#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    ### your code goes here

    import numpy as np

    errors = [abs(net_worths[key][0] - value[0]) for key, value in enumerate(predictions)]
    
    to_keep_count = len(errors) - len(errors)/10
    to_keep = np.argsort(errors)[:to_keep_count]

    return [(ages[i], net_worths[i], errors[i]) for i in to_keep]

