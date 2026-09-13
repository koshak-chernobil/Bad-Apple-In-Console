RU

Русский
Bad Apple в консоли — это ASCII-плеер, который проигрывает видео Bad Apple!! прямо в терминале Windows. Каждый кадр видео конвертируется в поток текстовых символов, где яркость пикселя соответствует «плотности» символа, а звук воспроизводится синхронно через pygame.

Проект написан на Python с использованием OpenCV для чтения и обработки видео. Вывод идёт в альтернативный буфер терминала, что позволяет избежать мерцания и не засорять историю команд. Кадр рисуется одним вызовом write() — это даёт плавную анимацию даже на слабых машинах. Если рендер отстаёт от звука, лишние кадры пропускаются, чтобы видео и музыка не рассинхронизировались.

Работает в Windows Terminal и любом терминале с поддержкой ANSI. Настраивается ширина кадра, палитра символов и громкость.

Зависимости
Python 3.13+

opencv-python — чтение видео, ресайз кадров, конвертация в градации серого

pygame-ce — воспроизведение звука (MP3/WAV/OGG)

Установка:

text
py -m pip install opencv-python pygame-ce
ffmpeg нужен опционально — для извлечения аудио из mp4 и конвертации форматов.

ENG

English
Bad Apple in the Terminal is an ASCII player that plays the Bad Apple!! video right inside your Windows terminal. Each video frame is converted into a stream of text characters, where pixel brightness maps to character "density", and audio is played back in sync via pygame.

The project is written in Python using OpenCV for video reading and processing. Output goes to the terminal's alternate buffer, which eliminates flickering and keeps your command history clean. Each frame is drawn with a single write() call, giving smooth animation even on weak machines. If rendering falls behind the audio, extra frames are dropped so video and music stay in sync.

Works in Windows Terminal and any ANSI-capable terminal. Frame width, character palette, and volume are configurable.

Dependencies
Python 3.13+

opencv-python — video reading, frame resizing, grayscale conversion

pygame-ce — audio playback (MP3/WAV/OGG)

Install:

text
py -m pip install opencv-python pygame-ce
ffmpeg is optional — for extracting audio from mp4 and converting formats.

