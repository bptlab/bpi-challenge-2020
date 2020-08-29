import os
from pprint import pprint
import pandas as pd

from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.conversion.log import converter as log_converter

wd = os.path.join('..', 'data', 'cleaned_logs')

DOM_DEC = os.path.join(wd, 'DomesticDeclarations.xes')
INT_DEC = os.path.join(wd, 'InternationalDeclarations.xes')
PER = os.path.join(wd, 'PermitLog.xes')
PRE = os.path.join(wd, 'PrepaidTravelCost.xes')
REQ = os.path.join(wd, 'RequestForPayment.xes')


def read_log(file):
    return xes_importer.apply(file)

def to_dataframe(log):
    log = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)
    return log
