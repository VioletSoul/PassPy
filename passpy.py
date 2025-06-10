import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

# Словарь с именами аккаунтов и паролями
PASSWORDS = {
    'VioletSoul': 'pass1',
    'admin': 'pass2',
    'user': 'pass3'
}

# Путь к пользовательской иконке (PNG). Если пусто — будет создана синяя иконка.
ICON_PATH = 'path/to/your/icon.png'  # Укажи свой путь или оставь пустым

def copy_password(password):
    """Копирует переданный пароль в системный буфер обмена."""
    clipboard = QApplication.clipboard()
    clipboard.setText(password)
    print(f'[INFO] Скопировано: {password}')

app = QApplication(sys.argv)

# Загружаем пользовательскую иконку или создаём синюю по умолчанию
if ICON_PATH and ICON_PATH != '':
    icon = QIcon(ICON_PATH)
    if icon.isNull():
        print(f'[WARNING] Не удалось загрузить иконку: {ICON_PATH}. Используется иконка по умолчанию.')
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.blue)
        icon = QIcon(pixmap)
else:
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.blue)
    icon = QIcon(pixmap)

# Создаём иконку в системном трее
tray = QSystemTrayIcon(icon)

# Формируем контекстное меню для иконки
menu = QMenu()

# Сохраняем действия, чтобы они не были удалены сборщиком мусора
actions = []

# Добавляем пункты меню для каждого аккаунта
for name, pwd in PASSWORDS.items():
    action = QAction(name, tray)
    action.triggered.connect(lambda checked, p=pwd: copy_password(p))
    menu.addAction(action)
    actions.append(action)

# Добавляем пункт для выхода из приложения
exit_action = QAction("Выход", tray)
exit_action.triggered.connect(app.quit)
menu.addAction(exit_action)
actions.append(exit_action)

# Привязываем меню к иконке и показываем её в трее
tray.setContextMenu(menu)
tray.setVisible(True)
tray.show()

# Сохраняем ссылки на меню и действия для предотвращения их удаления
tray.menu = menu
tray.actions = actions

# Запускаем основной цикл приложения
sys.exit(app.exec_())
