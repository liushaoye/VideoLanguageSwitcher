# Video Language Switcher

**一个开源桌面应用程序，能将视频中的语音自动翻译为目标语言，并生成替换音轨的视频。**  

**目标用户**：国内用户，完全免费、离线可用。

---

## 功能需求

1. **视频选择与输出路径选择**（GUI）
2. **音频提取和转文字（Speech-to-Text）**
   - 支持中文/英文/日语
   - 完全离线运行
3. **文本翻译**
   - 支持中、英、日互译
   - 使用国内可访问的翻译模型或离线方案
4. **文本转语音（TTS）**
   - 中文自然语音
   - 音频与原视频时间轴对齐
5. **视频音轨替换并生成新视频**
6. **GUI 显示进度条、完成弹窗、打开输出文件夹按钮**

---

## 技术方案建议

- GUI: **C# WPF / C++ Qt / Electron**
- 视频处理: **ffmpeg**
- 音频转文字: **whisper.cpp / faster-whisper**
- TTS: **Coqui TTS / VITS**
- 翻译: **Argos Translate / 国内可用离线模型**

---

## 可行的模块化开发方案

1. 视频导入 -> ffmpeg 提取音频  
2. 音频转文字 -> whisper.cpp  
3. 文本翻译 -> 本地翻译模型  
4. TTS 生成语音 -> Coqui TTS  
5. 替换原视频音轨 -> ffmpeg 合成  
6. GUI 显示整个流程进度，操作简单  

---

## 如何贡献

- Fork 本项目  
- 提交 Pull Request  
- 贡献方向：
  - GUI 界面  
  - 模型下载管理与加载  
  - 音视频处理流程封装  
  - 打包成 exe 或跨平台应用  

---

## 标签

- `help wanted`  
- `good first issue`  
- `feature request`  
- `discussion`  

---

## 联系方式

- 可在 GitHub Issues 提问或提交讨论  
- 欢迎提出方案和技术路线
