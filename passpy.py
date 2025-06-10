import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

PASSWORDS = {
    'VioletSoul': 'pass1',
    'admin': 'pass2',
    'user': 'pass3'
}

# Путь к иконке, если есть — укажи здесь, иначе None или пустая строка
ICON_PATH = 'path/to/your/icon.png'  # Замените на реальный путь или оставьте ''

def copy_password(password):
    clipboard = QApplication.clipboard()
    clipboard.setText(password)
    print(f'[INFO] Скопировано: {password}')

app = QApplication(sys.argv)

if ICON_PATH and ICON_PATH != '':
    icon = QIcon(ICON_PATH)
    if icon.isNull():
        print(f'[WARNING] Иконка по пути {ICON_PATH} не найдена или невалидна. Используется иконка по умолчанию.')
        # Создаём простую иконку
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.blue)
        icon = QIcon(pixmap)
else:
    # Создаём простую иконку
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.blue)
    icon = QIcon(pixmap)

tray = QSystemTrayIcon(icon)
menu = QMenu()

actions = []
for name, pwd in PASSWORDS.items():
    action = QAction(name, tray)
    action.triggered.connect(lambda checked, p=pwd: copy_password(p))
    menu.addAction(action)
    actions.append(action)

exit_action = QAction("Выход", tray)
exit_action.triggered.connect(app.quit)
menu.addAction(exit_action)
actions.append(exit_action)

tray.setContextMenu(menu)
tray.setVisible(True)
tray.show()

# Держим ссылки на menu и actions, чтобы их не удалил сборщик мусора
tray.menu = menu
tray.actions = actions

sys.exit(app.exec_())
