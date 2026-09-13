# Bad Apple в консоли / Bad Apple in the Terminal

---

## RU

Bad Apple в консоли — это ASCII-плеер, который проигрывает видео Bad Apple!! прямо в терминале Windows. Каждый кадр видео конвертируется в поток текстовых символов, где яркость пикселя соответствует «плотности» символа, а звук воспроизводится синхронно через pygame.

Проект написан на Python с использованием OpenCV для чтения и обработки видео. Вывод идёт в альтернативный буфер терминала, что позволяет избежать мерцания и не засорять историю команд. Кадр рисуется одним вызовом `write()` — это даёт плавную анимацию даже на слабых машинах. Если рендер отстаёт от звука, лишние кадры пропускаются, чтобы видео и музыка не рассинхронизировались.

Работает в Windows Terminal и любом терминале с поддержкой ANSI. Настраивается ширина кадра, палитра символов и громкость.

### Использование

Открой **Windows Terminal** или **PowerShell**, перейди в полноэкранный режим (`Alt + Enter` или `F11`) и запусти:

```bash
py BadApple.py
```

Выход — `Ctrl+C`.

### Зависимости

- **Python 3.13+**
- **opencv-python** — чтение видео, ресайз кадров, конвертация в градации серого
- **pygame-ce** — воспроизведение звука (MP3/WAV/OGG)

### Установка
```bash
py -m pip install opencv-python pygame-ce
```

`ffmpeg` нужен опционально — для извлечения аудио из mp4 и конвертации форматов.
```bash
winget install Gyan.FFmpeg
```

---

## ENG

Bad Apple in the Terminal is an ASCII player that plays the Bad Apple!! video right inside your Windows terminal. Each video frame is converted into a stream of text characters, where pixel brightness maps to character "density", and audio is played back in sync via pygame.

The project is written in Python using OpenCV for video reading and processing. Output goes to the terminal's alternate buffer, which eliminates flickering and keeps your command history clean. Each frame is drawn with a single `write()` call, giving smooth animation even on weak machines. If rendering falls behind the audio, extra frames are dropped so video and music stay in sync.

Works in Windows Terminal and any ANSI-capable terminal. Frame width, character palette, and volume are configurable.

### Usage

Open **Windows Terminal** or **PowerShell**, switch to fullscreen (`Alt + Enter` or `F11`), and run:

```bash
py BadApple.py
```

Exit with `Ctrl+C`.

### Dependencies

- **Python 3.13+**
- **opencv-python** — video reading, frame resizing, grayscale conversion
- **pygame-ce** — audio playback (MP3/WAV/OGG)

### Install
```bash
py -m pip install opencv-python pygame-ce
```

`ffmpeg` is optional — for extracting audio from mp4 and converting formats.
```bash
winget install Gyan.FFmpeg
```
