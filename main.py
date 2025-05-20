from input import record_audio, transcribe_audio
from output import speak
from brain import generate_response

def main():
    while True:
        audio_file = record_audio()
        user_text = transcribe_audio(audio_file)
        print("🧍You:", user_text)

        reply = generate_response(user_text)
        print("🤖 Bot:", reply)

        speak(reply)

if __name__ == "__main__":
    main()
