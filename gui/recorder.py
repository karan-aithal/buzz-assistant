import threading
import time
import wave
import pyaudio
from utils.signal_handler import signal_handler

class AudioRecorder:
    def __init__(self):
        self.recording = False
        self.thread = None

    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        print("Starting audio recording...")
        self.recording = True
        signal_handler.recording_started.emit()
        self.thread = threading.Thread(target=self._record_audio)
        self.thread.start()

    def stop_recording(self):
        print("Stopping audio recording...")
        self.recording = False
        signal_handler.recording_stopped.emit()
        if self.thread:
            self.thread.join()

    def _record_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []

        try:
            while self.recording:
                data = stream.read(1024)
                frames.append(data)
        finally:
            stream.stop_stream()
            stream.close()
            audio.terminate()

            with wave.open("recorded_audio.wav", "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                wf.setframerate(44100)
                wf.writeframes(b"".join(frames))
            print("Audio saved as 'recorded_audio.wav'.")
