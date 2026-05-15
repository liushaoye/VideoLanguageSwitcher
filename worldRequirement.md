# Video Language Switcher

**An open-source desktop application that automatically translates the audio in videos into a target language and generates a new video with replaced audio.**  
**目标用户**: 国内用户，完全免费，离线可用。  
**対象ユーザー**: 中国国内ユーザー向け、完全無料、オフライン対応。  
**Usuarios objetivo**: Usuarios en China, completamente gratuito y funcional sin conexión.

---

## 1️⃣ English

### Feature Requirements

1. Video selection and output path selection (GUI)  
2. Audio extraction and Speech-to-Text (offline, supports Chinese / English / Japanese)  
3. Text Translation (offline or locally accessible models)  
4. Text-to-Speech (TTS, natural voice, timeline-aligned)  
5. Video audio track replacement and output  
6. GUI: progress bar, completion notification, open output folder button  

### Suggested Technical Stack

- GUI: C# WPF / C++ Qt / Electron  
- Video processing: ffmpeg  
- Speech-to-Text: whisper.cpp / faster-whisper  
- TTS: Coqui TTS / VITS  
- Translation: Argos Translate / offline translation models  

---

## 2️⃣ 中文

### 功能需求

1. 视频选择与输出路径选择（GUI）  
2. 音频提取和语音转文字（离线，支持中/英/日）  
3. 文本翻译（离线或本地可用模型）  
4. 文本转语音（自然语音，与原视频时间轴对齐）  
5. 视频音轨替换与输出  
6. GUI: 显示进度条、完成弹窗、打开输出文件夹按钮  

### 技术方案建议

- GUI: C# WPF / C++ Qt / Electron  
- 视频处理: ffmpeg  
- 语音转文字: whisper.cpp / faster-whisper  
- TTS: Coqui TTS / VITS  
- 翻译: Argos Translate / 本地翻译模型  

---

## 3️⃣ 日本語 (Japanese)

### 機能要件

1. ビデオ選択と出力パス選択（GUI）  
2. 音声抽出と音声→文字変換（オフライン、中国語・英語・日本語対応）  
3. 文章翻訳（オフラインまたはローカルモデル）  
4. テキスト→音声（自然音声、元動画のタイムラインに同期）  
5. ビデオ音声トラックの置換と出力  
6. GUI: プログレスバー、完了通知、出力フォルダを開くボタン  

### 推奨技術スタック

- GUI: C# WPF / C++ Qt / Electron  
- 動画処理: ffmpeg  
- 音声→文字: whisper.cpp / faster-whisper  
- TTS: Coqui TTS / VITS  
- 翻訳: Argos Translate / オフライン翻訳モデル  

---

## 4️⃣ Español (Spanish)

### Requisitos de Funcionalidad

1. Selección de video y ruta de salida (GUI)  
2. Extracción de audio y conversión de voz a texto (offline, soporta Chino / Inglés / Japonés)  
3. Traducción de texto (offline o modelos locales)  
4. Texto a voz (TTS, voz natural, sincronizado con la línea de tiempo del video)  
5. Reemplazo de la pista de audio del video y exportación  
6. GUI: barra de progreso, notificación de finalización, botón para abrir carpeta de salida  

### Stack Técnico Sugerido

- GUI: C# WPF / C++ Qt / Electron  
- Procesamiento de video: ffmpeg  
- Voz a texto: whisper.cpp / faster-whisper  
- TTS: Coqui TTS / VITS  
- Traducción: Argos Translate / modelos de traducción offline  

---

## Contribution / 贡献 / 貢献 / Contribución

- Fork this repository  
- Submit Pull Requests  
- Areas for contribution: GUI design, module interface, audio/video processing, packaging  
- 请贡献 GUI 界面、模块接口、音视频处理流程、打包  
- GUIデザイン、モジュールインターフェース、音声・動画処理、パッケージ化  
- Diseño de GUI, interfaces de módulos, procesamiento de audio/video, empaquetado
