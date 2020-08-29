import pandas as pd
import numpy as np
import math

def get_columns(df: pd.DataFrame):
    return list(df.columns)

def describe_clm(df: pd.DataFrame, clm_name):
    report = {}

    unique_elements = df[clm_name].unique()
    clm = df[clm_name].to_list()
    
    elements = len(clm)
    missing = get_missing(clm)
    coverage = get_coverage(elements, missing, True)

    report['column'] = clm_name.split(':')[-1]
    report['elements'] = elements
    report['unique_elements'] = len(unique_elements)
    report['NaN'] = missing
    report['coverage'] = coverage

    return report


def get_coverage(total, elements, inverse=False, fields=3):
    if inverse:
        elements = total - elements
        
    coverage = elements / total * 100

    return round(coverage, fields)

def get_missing(values: list):
    def is_missing(value):
        try:
            if isinstance(value, str):
                return value.upper() is 'UNKNOWN' or value.upper() is 'MISSINMG'

            return value is np.nan or math.isnan(value)
        except TypeError as error:
            return False

    return len(list(filter(lambda x: x, map(is_missing, values))))
    
