import whisper
import sounddevice as sd
import soundfile as sf

model = whisper.load_model("base")

def record_audio(filename="input.wav", duration=5, samplerate=16000):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, recording, samplerate)
    print("🛑 Done recording.")
    return filename

def transcribe_audio(filename="input.wav"):
    result = model.transcribe(filename)
    return result["text"]
