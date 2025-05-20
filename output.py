from TTS.api import TTS
import soundfile as sf
import sounddevice as sd
import tempfile

tts = TTS(model_name="tts_models/en/vctk/vits")

def speak(text):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        speaker = tts.speakers[0] if tts.speakers else None
        tts.tts_to_file(text=text, speaker=speaker, file_path=tmpfile.name)
        data, sr = sf.read(tmpfile.name)
        sd.play(data, sr)
        sd.wait()
