import wave
import pyaudio
from config import RECORD_PATH


class AudioRecording:
    def __int__(self):
        pass

    @staticmethod
    def recording(second=60):
        chunk = 1024
        formats = pyaudio.paInt16
        channels = 2
        rate = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=formats,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
        frames = []

        for i in range(0, int(rate / chunk * second)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(RECORD_PATH, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(formats))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()
