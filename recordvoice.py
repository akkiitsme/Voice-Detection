import pyaudio
import wave

# Set up the recording parameters
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16-bit audio
channels = 1  # Mono
rate = 48000  # Record at 44,100 Hz

# Open the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=sample_format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

# Print a message to let the user know to start speaking
print("Speak now...")

# Record for 5 seconds
frames = []
for i in range(0, int(rate / chunk * 5)):
    data = stream.read(chunk)
    frames.append(data)

# Stop the stream
stream.stop_stream()
stream.close()

# Close PyAudio
p.terminate()

# Save the recorded data to a WAV file
wf = wave.open('audios/recorded_voice.wav', 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()

# Print a message to let the user know that the recording has been saved
print("Recording saved to 'audios/recorded_voice.wav'")