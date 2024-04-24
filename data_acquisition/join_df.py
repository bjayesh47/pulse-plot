import pandas as pd

id_df = pd.read_csv('streaming_history_complete.csv')
af_df = pd.read_csv('audio_features.csv')
result_df = pd.merge(id_df, af_df, on='id')

result_df.to_csv('final_data.csv')