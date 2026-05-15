# Video Language Switcher

**An open-source desktop application that automatically translates the audio in videos into a target language and generates a new video with replaced audio.**

**Target Users:** Domestic users in China, completely free, offline-ready.

---

## Feature Requirements

1. **Video selection and output path selection** (GUI)
2. **Audio extraction and Speech-to-Text**
   - Supports Chinese, English, and Japanese
   - Fully offline operation
3. **Text Translation**
   - Supports Chinese ↔ English ↔ Japanese
   - Uses offline or locally accessible translation models
4. **Text-to-Speech (TTS)**
   - Natural-sounding Chinese voice
   - Audio aligned with original video timeline
5. **Video audio track replacement and output**
6. **GUI features**
   - Progress bar
   - Completion notification
   - Button to open output folder

---

## Suggested Technical Stack

- GUI: **C# WPF / C++ Qt / Electron**
- Video processing: **ffmpeg**
- Speech-to-Text: **whisper.cpp / faster-whisper**
- TTS: **Coqui TTS / VITS**
- Translation: **Argos Translate / locally available translation models**

---

## Recommended Modular Development

1. Import video → extract audio via ffmpeg  
2. Audio to text → whisper.cpp  
3. Translate text → local translation model  
4. Generate speech → Coqui TTS  
5. Replace video audio track → ffmpeg  
6. GUI displays progress throughout, simple and user-friendly

---

## How to Contribute

- Fork the project  
- Submit Pull Requests  
- Areas for contribution:
  - GUI design  
  - Model download and management  
  - Audio/video processing pipeline  
  - Packaging into an executable or cross-platform app  

---

## Labels

- `help wanted`  
- `good first issue`  
- `feature request`  
- `discussion`  

---

## Contact / Discussion

- Open GitHub Issues for questions or discussions  
- Welcome suggestions for technical solutions and implementation
