import os
import sys
import time
import cv2
import pygame

# ─────────── НАСТРОЙКИ ───────────
VIDEO_PATH = "bad_apple.mp4"     # путь к видео
AUDIO_PATH = "bad_apple.mp3"     # pygame читает mp3/wav сам
WIDTH      = 180                 # ширина кадра в символах
CHARS      = " .:-=+*#%@"        # палитра от тёмного к светлому
VOLUME     = 0.5                 # 0.0 – 1.0
# ─────────────────────────────────


def frame_to_lines(frame, width):
    """Превращает BGR-кадр в список ASCII-строк."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    new_h = max(1, int(width * (h / w) * 0.5))  # символ выше, чем шире
    resized = cv2.resize(gray, (width, new_h), interpolation=cv2.INTER_NEAREST)

    n = len(CHARS)
    lines = []
    for row in resized:
        lines.append("".join(
            CHARS[min(n - 1, int(px) * n // 256)]
            for px in row
        ))
    return lines


def main():
    # ─── ВИДЕО ───
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Не могу открыть видео:", VIDEO_PATH)
        return

    fps = cap.get(cv2.CAP_PROP_FPS) or 30

    # ─── ЗВУК ───
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
    pygame.mixer.music.set_volume(VOLUME)
    try:
        pygame.mixer.music.load(AUDIO_PATH)
    except Exception as e:
        sys.stderr.write(f"[audio] не могу загрузить {AUDIO_PATH}: {e}\n")
        pygame.mixer.quit()
        cap.release()
        return

    # ─── АЛЬТЕРНАТИВНЫЙ БУФЕР ───
    sys.stdout.write("\033[?1049h")     # отдельный экран
    sys.stdout.write("\033[?25l")       # прячем курсор
    sys.stdout.write("\033[2J\033[H")   # чистим его один раз
    sys.stdout.flush()

    # ─── СТАРТ: звук и отсчёт времени с одной точки ───
    pygame.mixer.music.play()
    start = time.perf_counter()

    prev_height = 0
    frame_index = 0

    try:
        while True:
            # сколько кадров уже должно было пройти?
            elapsed = time.perf_counter() - start
            expected = int(elapsed * fps)

            # если отстали — пропускаем кадры, не рендеря их
            while frame_index < expected:
                if not cap.grab():      # grab() быстрее, чем read()
                    break
                frame_index += 1

            # берём текущий кадр
            ok, frame = cap.read()
            if not ok:
                break

            lines = frame_to_lines(frame, WIDTH)

            # собираем весь кадр в один буфер
            buf = ["\033[H"]
            for line in lines:
                buf.append(line)
                buf.append("\033[K")   # стереть хвост строки
                buf.append("\n")
            # затираем лишние строки снизу, если кадр стал короче
            for _ in range(len(lines), prev_height):
                buf.append("\033[K\n")
            prev_height = len(lines)

            sys.stdout.write("".join(buf))
            sys.stdout.flush()

            frame_index += 1
            # НЕ sleep'им — темп задаёт звук

    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        sys.stdout.write("\033[?1049l")   # выходим из альт-буфера
        sys.stdout.write("\033[?25h\n")   # возвращаем курсор
        sys.stdout.flush()


if __name__ == "__main__":
    main()