import librosa
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def extract_features(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Extract mel-frequency cepstral coefficients (MFCCs)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

    # Calculate the mean and standard deviation of the MFCCs
    mean_mfccs = np.mean(mfccs, axis=1)
    std_mfccs = np.std(mfccs, axis=1)

    # Combine the mean and standard deviation into a single feature vector
    features = np.hstack((mean_mfccs, std_mfccs))

    return features

def compare_voices(audio_file1, audio_file2):
    # Extract features from both audio files
    features1 = extract_features(audio_file1)
    features2 = extract_features(audio_file2)

    # Calculate the cosine similarity between the two feature vectors
    similarity = cosine_similarity(features1.reshape(1, -1), features2.reshape(1, -1))

    return similarity

# Example usage
audio_file1 = "audios/recorded_voice.wav"
audio_file2 = "./recorded_voice_5.wav"

similarity = compare_voices(audio_file1, audio_file2)
print("similarity: ",similarity)

if similarity > 0.9:
    print("The two voices are likely the same person.")
else:
    print("The two voices are likely different people.")