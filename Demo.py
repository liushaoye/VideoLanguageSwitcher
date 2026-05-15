import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from googletrans import Translator
import edge_tts
import asyncio
import tempfile
import shutil
import requests

# ====== ffmpeg 和 whisper.cpp 路径 ======
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # ffmpeg.exe路径
WHISPER_CPP = r"D:\workspace\whispercpp\main.exe"  # whisper.cpp exe路径
WHISPER_MODEL_DIR = r"D:\workspace\whispercpp\models2\ggml-small.bin"  # 模型文件路径
WHISPER_MODEL = os.path.join(WHISPER_MODEL_DIR, "ggml-small.bin")
WHISPER_MODEL_URL = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin"


class App:
    def __init__(self, master):
        self.master = master
        master.title("视频换语音（免费）")

        # 视频路径
        tk.Label(master, text="选择视频文件:").grid(row=0, column=0, sticky="w")
        self.video_path_var = tk.StringVar()
        tk.Entry(master, textvariable=self.video_path_var, width=50).grid(row=0, column=1)
        tk.Button(master, text="浏览", command=self.select_video).grid(row=0, column=2)

        # 输出文件夹
        tk.Label(master, text="输出文件夹:").grid(row=1, column=0, sticky="w")
        self.output_path_var = tk.StringVar()
        tk.Entry(master, textvariable=self.output_path_var, width=50).grid(row=1, column=1)
        tk.Button(master, text="浏览", command=self.select_output).grid(row=1, column=2)

        # 进度条
        self.progress = ttk.Progressbar(master, length=400, mode="determinate")
        self.progress.grid(row=2, column=0, columnspan=3, pady=10)

        # 开始按钮
        tk.Button(master, text="开始转换", command=self.start_conversion).grid(row=3, column=1)

    def select_video(self):
        path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if path:
            self.video_path_var.set(path)

    def select_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path_var.set(path)

    def download_model(self):
        os.makedirs(WHISPER_MODEL_DIR, exist_ok=True)
        if os.path.exists(WHISPER_MODEL):
            return True

        messagebox.showinfo("提示", "模型文件未找到，开始下载约50MB...")
        with requests.get(WHISPER_MODEL_URL, stream=True) as r:
            total_length = int(r.headers.get('content-length', 0))
            with open(WHISPER_MODEL, 'wb') as f:
                dl = 0
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        dl += len(chunk)
                        percent = int(dl / total_length * 100)
                        self.progress["value"] = percent
                        self.master.update()
        messagebox.showinfo("提示", "模型下载完成！")
        return True

    def start_conversion(self):
        video_path = self.video_path_var.get()
        output_dir = self.output_path_var.get()
        if not video_path or not output_dir:
            messagebox.showerror("错误", "请填写视频文件和输出文件夹！")
            return

        try:
            self.progress["value"] = 5
            self.master.update()

            # 下载模型
            self.download_model()
            self.progress["value"] = 10
            self.master.update()

            # 临时目录
            tmp_dir = tempfile.mkdtemp(prefix="video_voice_")
            audio_temp = os.path.join(tmp_dir, "temp.wav")
            txt_temp = os.path.join(tmp_dir, "temp.txt")
            tts_file = os.path.join(tmp_dir, "tts.mp3")

            # 提取音频
            cmd_audio = [FFMPEG_PATH, "-i", video_path, "-ac", "1", "-ar", "16000", audio_temp, "-y"]
            subprocess.run(cmd_audio, check=True)
            self.progress["value"] = 30
            self.master.update()

            if not os.path.exists(audio_temp):
                raise FileNotFoundError("音频提取失败，temp.wav 不存在")

            # WhisperCpp 识别
            cmd_whisper = [
                WHISPER_CPP,
                "-f", audio_temp,
                "-otxt", txt_temp,
                "-m", WHISPER_MODEL,
                "-lang", "en"
            ]
            subprocess.run(cmd_whisper, check=True)

            if not os.path.exists(txt_temp):
                raise FileNotFoundError("whisper.cpp 输出文件未生成")

            with open(txt_temp, "r", encoding="utf-8") as f:
                recognized_text = f.read()

            self.progress["value"] = 50
            self.master.update()

            # 翻译文本
            translator = Translator()
            translated_text = translator.translate(recognized_text, src='en', dest='zh-cn').text

            self.progress["value"] = 70
            self.master.update()

            # TTS
            communicate = edge_tts.Communicate(translated_text, "zh-CN-XiaoxiaoNeural", tts_file)
            asyncio.run(communicate.run())

            self.progress["value"] = 90
            self.master.update()

            # 合成视频
            final_video = os.path.join(output_dir, "output.mp4")
            cmd_merge = [
                FFMPEG_PATH, "-i", video_path, "-i", tts_file,
                "-c:v", "copy", "-map", "0:v:0", "-map", "1:a:0",
                final_video, "-y"
            ]
            subprocess.run(cmd_merge, check=True)

            self.progress["value"] = 100
            messagebox.showinfo("完成", f"转换完成！文件保存为:\n{final_video}")
            os.startfile(output_dir)

        except subprocess.CalledProcessError as e:
            messagebox.showerror("转换失败", f"命令执行失败:\n{e}")
        except Exception as e:
            messagebox.showerror("转换失败", str(e))
        finally:
            if os.path.exists(tmp_dir):
                shutil.rmtree(tmp_dir)


# 启动GUI
root = tk.Tk()
app = App(root)
root.mainloop()
