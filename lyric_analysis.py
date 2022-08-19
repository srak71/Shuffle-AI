"""
Public file for conversion of audio in natural language processing.
@saranshrakshak
Oct-24-2021
"""
from pydub import AudioSegment
import speech_recognition as sr
import os
from nlkt.sentiment.vader import SentimentIntensityAnalyzer

## changing format of incoming file from .m4a (or other) to .wav
# returns an AudioSegment object
def convert_to_wav(filename):
    filename = 'audio_files/' + filename
    file_type = filename.split(".")[1]

    if file_type != '.wav':
        filename.split(".")[0] + ".wav"
        audio = AudioSegment.from_file(filename)
        audio.export(new_name, format = 'wav')
        return new_name
    else:
        if os.path.exists(filename,__contains__('.wav')):
            print('File <<', filename, '>> already converted to wav and removed.')
            return filename.split(".")[0] + '.wav'
        else:
            print('File <<', filename, '>> non-existant.')
            return filename.split(".")[0] + '.wav'

# get the lyrics to our song file
def transcribe_audio(wav_file):
    if not wav_file: return False
    recognizer = sr.Recognizer()
    # Import the audio file and get song lyrics
    audio_file = sr.AudioFile(wav_file)
    with audio_file as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)

# get sentiment of lyrics
def analyze_text(text_file):
    if not text_file: return False
    intensity = SentimentIntensityAnalyzer().polarity_score(text_file)
    return SentimentIntensityAnalyzer

# get volume user is listening song to
def get_volume():
    return AudioSegment.from_file(filename).dBFS
