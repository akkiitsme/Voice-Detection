import librosa
import numpy as np

def extract_vocal_features(filename):
    y, sr = librosa.load(filename)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_mean = np.array(np.mean(mfccs, axis=1))
    mfcc_std = np.array(np.std(mfccs, axis=1))
    return mfcc_mean, mfcc_std

def compare_voices(voice1_filename, voice2_filename):
    voice1_mean, voice1_std = extract_vocal_features(voice1_filename)
    voice2_mean, voice2_std = extract_vocal_features(voice2_filename)

    # Calculate the Euclidean distance separately for mean and std
    distance_mean = np.linalg.norm(voice1_mean - voice2_mean)
    distance_std = np.linalg.norm(voice1_std - voice2_std)

    # Calculate the overall distance
    overall_distance = (distance_mean + distance_std) / 2

    print("distance: ",overall_distance)
    # Determine if the voices are the same
    if overall_distance < 5:
        print("The voices are same.")
    elif overall_distance < 10:
        print("The voices are closely same.")
    elif overall_distance < 20:
        print("The voices are likely the same.")
    elif overall_distance > 20 and overall_distance < 25:
        print("The voices are nearly the same.")
    elif overall_distance > 25 and overall_distance < 30:
        print("The voices may be slightly the same.")
    else:
        print("The voices are different.")

# Example usage
voice1_filename = "audios/recorded_voice.wav"
voice2_filename = "audios/recorded_voice_3.wav"

compare_voices(voice1_filename, voice2_filename)