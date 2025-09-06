import threading
import time
from datetime import datetime, timedelta
import platform

# ----------------------------
# 1. SoundPlayer (периодический "звук")
# ----------------------------
sound_timer = None  # глобальная переменная для периодического таймера

def sound_player():
    global sound_timer
    # звук (только для Windows, иначе пропустить)
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 200)  # частота 1000 Гц, 200 мс
    print("Sound played")
    # запускаем следующий таймер через 2 сек
    sound_timer = threading.Timer(2, sound_player)
    sound_timer.start()

# ----------------------------
# 2. Таймер через 5 секунд для остановки sound_timer
# ----------------------------
def stop_sound_timer():
    global sound_timer
    print("5 seconds have passed")
    if sound_timer:
        sound_timer.cancel()  # останавливаем периодический таймер

# ----------------------------
# 3. Таймер на конкретное время (например, через 10 сек от запуска для теста)
# ----------------------------
def clock_message():
    print("Salut, Salut, Salut!!!")

# ----------------------------
# Запуск таймеров
# ----------------------------
print("Start")

# Периодический SoundPlayer каждые 2 секунды
sound_timer = threading.Timer(0, sound_player)
sound_timer.start()

# Таймер через 5 секунд для остановки периодического таймера
threading.Timer(5, stop_sound_timer).start()

# Таймер на определённое время (через 10 секунд от старта)
threading.Timer(10, clock_message).start()

# Чтобы программа не завершилась сразу
while True:
    time.sleep(1)
