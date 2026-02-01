import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QStyle
# from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import QTimer
from datetime import datetime

# Простейший работающий вариант
app = QApplication(sys.argv)

# Иконка
icon = app.style().standardIcon(QStyle.SP_MediaPlay)  # Иконка вперед

# Создаем иконку в трее
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setToolTip("Break Reminder\nПКМ → меню")

# Меню
menu = QMenu()

# Перерыв сейчас
action1 = QAction("Перерыв сейчас")
def break_now():
    tray.showMessage(
        "Перерыв!",
        "Сделайте перерыв на 1-2 минуты.",
        QSystemTrayIcon.Information,
        3000
    )
action1.triggered.connect(break_now)
menu.addAction(action1)

menu.addSeparator()

# ВЫХОД (обязательно!)
action_exit = QAction("ВЫХОД")
action_exit.triggered.connect(app.quit)  # Вот это ключевая строка!
menu.addAction(action_exit)

# Устанавливаем меню
tray.setContextMenu(menu)

# Показываем иконку
tray.show()

# Таймер на 20 минут
timer = QTimer()
def notify():
    time_str = datetime.now().strftime("%H:%M")
    tray.showMessage(
        "⏰ Время перерыва!",
        f"{time_str}\nПрошло 20 минут работы.\nОтдохните!",
        QSystemTrayIcon.Information,
        5000
    )

timer.timeout.connect(notify)
timer.start(20 * 60 * 1000)  # 20 минут

# Первое уведомление
tray.showMessage(
    "Break Reminder",
    "Программа запущена!\nУведомления каждые 20 мин.",
    QSystemTrayIcon.Information,
    3000
)

print("=" * 40)
print("Break Reminder запущен!")
print("=" * 40)
print("Инструкция:")
print("1. Найдите ЗЕЛЕНУЮ иконку в трее (рядом с часами)")
print("2. Нажмите на неё ПРАВОЙ кнопкой мыши")
print("3. В появившемся меню выберите:")
print("   - 'Перерыв сейчас' - для немедленного перерыва")
print("   - 'ВЫХОД' - для завершения программы")
print("=" * 40)
print("Программа работает в фоне...")

sys.exit(app.exec_())