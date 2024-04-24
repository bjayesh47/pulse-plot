import ast
import requests
from datetime import datetime
from typing import List
import spotipy
import spotipy.util as util
import pandas as pd
from config import *

def get_token(
        user: str,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        scope: str) -> str:
    token = util.prompt_for_user_token(
        user,
        scope,
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_uri)
    return token

def get_streamings(file: str = 'data/StreamingHistory_music_0.json') -> List[dict]:
    all_streamings = []
    
    with open(file, 'r', encoding='UTF-8') as f:
        new_streamings = ast.literal_eval(f.read())
        all_streamings += [streaming for streaming in new_streamings]

    return all_streamings

def get_id(track_name: str, token: str) -> str:
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer ' + token,
    }
    params = [
        ('q', track_name),
        ('type', 'track'),
    ]
    try:
        response = requests.get(
            'https://api.spotify.com/v1/search', 
            headers = headers,
            params = params, 
            timeout = 5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None
    
def get_features(track_id: str, token: str) -> dict:
    sp = spotipy.Spotify(auth = token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None
    
def get_features_in_batch(file_path: str, token: str) -> dict:
    df = pd.read_csv(file_path)
    name_list = df['name'].to_list()
    id_list = df['id'].to_list()
    print(len(id_list))
    chunk_size = 100
    chunks = [id_list[i: i + chunk_size] for i in range(0, len(id_list), chunk_size)]
    for chunk in chunks:
        print(len(chunk))
    all_features = {}

    
token = get_token(username, client_id, client_secret, redirect_uri, scope)
print(token)
get_features_in_batch('streaming_history_complete.csv', token)

# streamings = get_streamings()
# unique_tracks = list(set[streaming['trackName']] for streaming in streamings)
# all_features = {}
# all_ids = {}
# # f = open('songs.txt', 'w')
# print(unique_tracks)
# for i, track in enumerate(unique_tracks):
#     print(track)
    # f.write(str(track) + "\n")
    # print(i, " out of ", len(unique_tracks), "\n")
    # track_id = get_id(track, token)
    # print(track_id)
    # all_ids[track] = track_id
    # features = get_features(track_id, token)
    # print(features)
    # if features:
    #     all_features[track] = features
# f.close()

# with_ids = []
# for track_name, track_id in all_ids.items():
#     with_ids.append({'name': track_name, 'id': track_id})

# df = pd.DataFrame(with_ids)
# df.to_csv('streaming_history.csv')