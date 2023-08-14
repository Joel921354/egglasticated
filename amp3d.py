import librosa
import csv

# Load the MP3 audio file
mp3_file = "AMAR867.mp3"
audio, sample_rate = librosa.load(mp3_file)

# Perform some analysis or feature extraction
# For example, let's calculate the zero-crossing rate for each frame
zero_crossing_rate = librosa.feature.zero_crossing_rate(audio)

# Transpose the feature matrix
zero_crossing_rate = zero_crossing_rate.T

# Define the CSV filename
csv_filename = "audio_features.csv"

# Write the feature data to the CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    header = ["Frame", "Zero Crossing Rate"]
    csv_writer.writerow(header)
    
    # Write data rows
    for frame, zcr in enumerate(zero_crossing_rate):
        csv_writer.writerow([frame, zcr])

print(f"Audio features saved to {csv_filename}")
