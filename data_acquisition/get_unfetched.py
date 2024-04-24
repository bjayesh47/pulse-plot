import requests
import pandas as pd
from config import *
from history import get_token, get_id

all_features = {}
def get_unfetched_ids():
    file_path = './streaming_history.csv'
    df = pd.read_csv(file_path)
    token = get_token(username, client_id, client_secret, redirect_uri, scope)
    for index, row in df.iterrows():
        if (pd.isnull(row['id'])):
            id_obtained = get_id(row['name'], token)
            print(id_obtained)
            all_features[row['name']] = id_obtained
        else: 
            all_features[row['name']] = row['id']
    

get_unfetched_ids()
with_features = []
for track_name, track_id in all_features.items():
    with_features.append({'name': track_name, 'id': track_id})

df = pd.DataFrame(with_features)
df.to_csv('streaming_history_complete.csv')