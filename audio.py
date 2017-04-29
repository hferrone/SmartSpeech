import pyaudio
import wave


def play_audio(filename):
    chunk = 1024
    wav_file = wave.open(filename, 'r')
    py_audio = pyaudio.PyAudio()
    data_stream = wav_file.readframes(chunk)

    stream = py_audio.open(
        format = py_audio.get_format_from_width(wav_file.getsampwidth()),
        channels = wav_file.getnchannels(),
        rate = wav_file.getframerate(),
        output = True
    )

    while data_stream:
        stream.write(data_stream)
        data_stream = wav_file.readframes(chunk)

    stream.close()
    py_audio.terminate()


play_audio("./audio/wet.wav")