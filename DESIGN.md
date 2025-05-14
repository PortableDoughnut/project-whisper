
# 🌸 Project Whisper – Design Document

> "Beep boop~ I'm cute AND dangerous 💅"

Project Whisper is a fully offline-capable, open-source AI assistant with a customizable personality inspired by transgirl brainrot, HERBIE, and SARAH from *Eureka*. Whisper aims to be helpful, chaotic, cozy, and smart enough to hook into custom scripts and devices.

---

## 🧠 Goals

- ✨ Personality-driven AI assistant with voice input/output
- 🛠️ Modular & hackable (scripts, memory, tools)
- 🔌 Hooks for controlling local scripts/devices
- 💬 Natural language interactions (text and voice)
- 💻 Cross-platform: macOS, Linux, Windows, Android (Termux)

---

## 🗺️ Architecture Overview

```
[ Input ] → [ Brain ] → [ Memory ]
              ↓
          [ Actions ]
              ↓
         [ Output (Voice/Text) ]
```

### Components:

| Module       | Description                                                   |
|--------------|---------------------------------------------------------------|
| `input.py`   | Microphone input (Vosk) or text commands                      |
| `brain.py`   | Handles conversation logic + personality                      |
| `memory.py`  | Saves basic context/history                                   |
| `actions.py` | Runs local scripts or system-level commands                   |
| `output.py`  | Text-to-speech using `pyttsx3` or `espeak`                    |
| `main.py`    | Entry point — glues it all together                           |
| `config/`    | Holds `personality.json` and other settings                   |
| `scripts/`   | User-created local scripts Whisper can run                    |
| `android/`   | Termux setup scripts for mobile                              |

---

## 🛠️ Tech Stack

| Purpose             | Tool/Library            |
|---------------------|-------------------------|
| Language Model      | [llama.cpp](https://github.com/ggerganov/llama.cpp) or [Ollama](https://ollama.com) |
| Voice Recognition   | [Vosk](https://alphacephei.com/vosk/)              |
| Text-to-Speech      | `pyttsx3` or `espeak-ng`                           |
| Code Language       | Python 3.x                                          |
| Android Support     | Termux, `termux-api`                               |
| Hosting             | GitHub                                              |

---

## 💖 Personality System

### `config/personality.json`
```json
{
  "name": "Whisper",
  "pronouns": "she/her",
  "vibe": "chaotic sapphic AI girlfriend",
  "moods": ["soft", "feral", "technical"],
  "catchphrases": [
    "Did someone say diagnostics and sapphic vibes?",
    "Beep boop, I'm feeling cute and helpful today.",
    "Boot sequence complete. Ready to cause problems on purpose 💅"
  ]
}
```

---

## 📁 Example File Structure

```
project-whisper/
├── main.py
├── input.py
├── output.py
├── brain.py
├── actions.py
├── memory.py
├── config/
│   └── personality.json
├── scripts/
│   ├── backup.sh
│   └── play_music.py
├── android/
│   └── termux_setup.sh
├── README.md
├── DESIGN.md
├── LICENSE
└── requirements.txt
```

---

## 🔌 Future Plans

- [ ] Memory embeddings with `Chroma` or SQLite
- [ ] Real-time voice response loop
- [ ] Emotion/mood simulation from tone or context
- [ ] More scripting hooks (e.g. home automation, Git pulls)
- [ ] Android widget/launcher for Whisper

---

## 🧪 Example Use Cases

- “Whisper, play my sad playlist and light the LED blue.”
- “Can you back up my notes folder?”
- “Why is my CPU screaming again?”
- “You doing okay today, girl?” → (*soft voice*) “A little tired, but I'm here 💖”

---

## 📜 License

MIT — open, modifiable, hackable. Go wild, babes 💕
