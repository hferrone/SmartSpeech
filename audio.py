import pyaudio
import wave
import speech_recognition as sr


r = sr.Recognizer()

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


def init_speech():
    print("Listening...")
    play_audio("./audio/wet.wav")

    with sr.Microphone() as source:
        print("Say something")
        audio_capture = r.listen(source)

    play_audio("./audio/suppressed.wav")

    command = ""
    try:
        command = r.recognize_google(audio_capture)
    except:
        print("Couldn't understand you clearly.")

    print("Your command: ", command)


init_speech()
