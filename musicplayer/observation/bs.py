"""
import pyaudio
p=pyaudio.PyAudio(...)  ->instantiate pyaudio
stream=p.open(...)   ->create stream
stream.start_stream()   ->start stream
sream.close   ->close stream
"""
import pyaudio
import wave
import time
import numpy as np
def record(outputfile):

	#DEFINE
	CHUNK=1024 #number of samples
	FORMAT=pyaudio.paInt16
	RATE=44100
	time=3 #sec
	#############################
	p=pyaudio.PyAudio()
	
	stream=p.open(format=FORMAT, channels=2, rate=RATE, input=True, frames_per_buffer=CHUNK)
	
	print("rec...")
	frame_list=np.array([], dtype=np.int16)
	for i in range(0, int(RATE/CHUNK*time)):
		data=stream.read(CHUNK)
		frame = np.frombuffer(data, dtype=np.int16)#this just overwrites each time
		frame_list=np.concatenate((frame_list,frame))

	#frame_list=(frame_list).astype(np.int16)
	print("rec done!")
	print(frame_list)
	stream.stop_stream()
	stream.close()
	p.terminate()

	#############################
	wv=wave.open(outputfile, "wb")
	#below are must_require parameters
	wv.setnchannels(2)
	wv.setframerate(RATE)
	wv.setsampwidth(p.get_sample_size(FORMAT))
	wv.writeframes(b''.join(frame_list))
	wv.close()
record('output1.wav')

time.sleep(3)

print(...)