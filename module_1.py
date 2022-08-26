import glob
from lyric_analysis import *
import os
import numpy as np
import pandas as pd

songs_df = pd.DataFrame(
    columns=['song_name', 'user_volume', 'song_lyrics', 'lyric_sentiment'])


def FileRunner(filename, info_print):
    global songs_df
    wav_file = convert_to_wav(filename)

    if songs_df['song_name'].str.contains(wav_file).any():
        print('Skip Reprocessing')
        return

    else:
        volume_file = get_volume(wav_file)
        text_file = transcribe_audio(wav_file)
        sentiment_file = analyze_text(text_file)
        dict_row = {'song_name': wav_file, 'user_volume': volume_file, 'song_lyrics': text_file,
                    'lyrics_sentiment': sentiment_file}
        songs_df = songs_df.append(dict_row, ignore_index=True)

        if info_print:
            show_file_info(wav_file, text_file, sentiment_file)
        return dict_row


def newest_file():
    new_file = max(glob.glob('song_files/*'), key=os.path.getctime)
    return new_file.split('/')[1]


def show_file_info(wav_file, text_file, sentiment_file):
    print(' ------- RUNNING NEW AUDIO FILE ------- ')
    print('File: ', wav_file.split('/')[1])
    print('Song Transcription: ', text_file)
    print('Song Sentiment: ', sentiment_file)


def show_song_df():
    print('songs_df: ', songs_df, type(songs_df), songs_df.columns)


def run_all_audio(info_print):
    all_files = np.array(os.listdir('song_files'))
    all_files = all_files[all_files != '.DS_Store']
    print(len(all_files), 'files will be run:', all_files)
    for i in all_files:
        FileRunner(i, info_print)


run_all_audio(info_print=True)
