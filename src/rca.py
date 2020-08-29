import pandas as pd

def flat_log(log, tuple_size: int):
    '''
    1. transform events into dataframe:
    '''
    features = []

    for trace in log:
        for idx, event in enumerate(trace[:-1]):
            pre = event
            post = trace[idx+1]

            time_delta = post['time:timestamp'] - pre['time:timestamp']

            pair = {'pre': pre['concept:name'], 
                    'post': post['concept:name'],
                    'pre_ts': pre['time:timestamp'],
                    'post_ts': post['time:timestamp'],
                    'ts_delta': time_delta,
                    'pre_role': pre['org:role'],
                    'post_role': post['org:role']}
            features.append(pair)
        
    return pd.DataFrame(features)
   
