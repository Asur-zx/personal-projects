    
import pyaudio
import subprocess
import wave

def play_mp3_with_pyaudio(file_path):
    # Convert MP3 to WAV using ffmpeg
    wav_file_path = "temp.wav"
    subprocess.run(["ffmpeg", "-i", file_path, wav_file_path])

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream
    

    # Read and play the WAV file
    with wave.open(wav_file_path, 'rb') as wav_file:#here using *with open() will open only file and does not allow to return framerate, but wave.open allows
    	framerate = wav_file.getframerate()
    	stream = p.open(format=p.get_format_from_width(2),
                    channels=wav_file.getnchannels(),
                    rate=framerate,
                    output=True)
    	
    	print(f'Frame rate: {framerate} Hz')

    	wav_data = wav_file.readframes(1024)#readframes instead of read
    	while wav_data:
        	stream.write(wav_data)
        	wav_data = wav_file.readframes(1024)


    # Cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Remove temporary WAV file
    subprocess.run(["rm", wav_file_path])

# File path of the MP3 file you want to play
mp3_file_path = "f:\\folder\\folder\\STORAGE\\MUSICS\\Centuries - Fall Out Boy.m4a"

# Play the MP3 file
play_mp3_with_pyaudio(mp3_file_path)
