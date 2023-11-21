import os
import numpy as np
from scipy.io import wavfile

# Function to calculate audio fingerprint
def fingerprint(audio_signal, frame_size=2048, hop_size=512):
    fingerprint = []
    for i in range(0, len(audio_signal) - frame_size, hop_size):
        frame = audio_signal[i:i + frame_size]
        fingerprint.append(hash(frame.tobytes()))
    return fingerprint

# Function to detect duplicate voice using fingerprints
def detect_duplicate_voice(source_audio, db_wav_directory):
    source_rate, source_audio_signal = wavfile.read(source_audio)

    source_fingerprint = fingerprint(source_audio_signal)

    # Iterate through the WAV files in the database directory
    for wav_file in os.listdir(db_wav_directory):
        wav_file_path = os.path.join(db_wav_directory, wav_file)
        db_rate, db_audio_signal = wavfile.read(wav_file_path)

        fingerprint_db = fingerprint(db_audio_signal)

        # Compare fingerprints to detect duplicates
        match_threshold = 100
        match_count = sum(f1 == f2 for f1, f2 in zip(source_fingerprint, fingerprint_db[:match_threshold]))
        print ("Match : ",match_count)

        if match_count >= match_threshold:
            print(f"Duplicate voice detected with file: {wav_file}")

# Replace with the path to your source WAV file
source_wav_file_path = './recorded_voice_5.wav'

# Replace with the directory containing the WAV files for the database
db_wav_directory = 'audios/'

# Call the function to detect duplicate voice for the source voice against the database
detect_duplicate_voice(source_wav_file_path, db_wav_directory)