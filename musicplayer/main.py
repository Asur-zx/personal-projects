#send data to visual.cpp using subprocess.run('filepath.exe') from here
import pyaudio
import wave
import numpy as np
import subprocess
import os
def playaudio(raw_file):
    file='file.wav'
    CHUNK=1024
    wf=wave.open(file, 'rb')
    p=pyaudio.PyAudio()
    subprocess.run(['ffmpeg', '-i', raw_file, file])

    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()), rate=wf.getframerate(), channels=wf.getnchannels(), output=True)#get samplewidth from file and get format from it
    data=wf.readframes(CHUNK)
    mag_array=np.array([],dtype=np.int16)
    freq_array=np.array([],dtype=np.int16)

    os.system('cls')

    while len(data)>0: 
        frames=np.frombuffer(data, dtype=np.int16)
        fftresult=np.fft.fft(frames)#convert time domain samples to freq domain->magnitude as amplitude and dirn as phase
        frequences=np.fft.fftfreq(len(fftresult), 1.0/wf.getframerate())#length of fftreasult and inverst of framerate->distance betn adjacent data points
        freq_array=np.concatenate((freq_array,frequences))
        mag_spectrum=np.abs(fftresult) #magnitude of fftresult gives frequescies
        #print(mag_spectrum)
        mag_array=np.concatenate((mag_array,mag_spectrum))


        #frames=(frames*1).astype(np.int16)  to increase volume
        stream.write(frames.tobytes())
        print(frequences,"####################", mag_spectrum)
        #stream.write(data)
        data=wf.readframes(CHUNK)

    print(mag_array)
    print(freq_array)
    finalplot(freq_array, mag_array)

    stream.stop_stream()
    stream.close()

    p.terminate()

def finalplot(freqs, mags):
    pass
playaudio("C:/Users/Acer/Music/I Ain't Worried - OneRepublic.m4a")