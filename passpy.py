import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

# Dictionary with account names and passwords
PASSWORDS = {
    'VioletSoul': 'pass1',
    'admin': 'pass2',
    'user': 'pass3'
}

# Define the path to the icon relative to the project folder
BASE_DIR = Path(__file__).parent.resolve()
ICON_PATH = BASE_DIR / 'icon.png'

def copy_password(password):
    """Copies the given password to the system clipboard."""
    clipboard = QApplication.clipboard()
    clipboard.setText(password)
    print(f'[INFO] Copied: {password}')

app = QApplication(sys.argv)

# Load the custom icon or create a default blue one
if ICON_PATH.exists():
    icon = QIcon(str(ICON_PATH))
    if icon.isNull():
        print(f'[WARNING] Failed to load icon: {ICON_PATH}. Using default icon.')
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.blue)
        icon = QIcon(pixmap)
else:
    print(f'[WARNING] Icon not found: {ICON_PATH}. Using default icon.')
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.blue)
    icon = QIcon(pixmap)

# Create a system tray icon
tray = QSystemTrayIcon(icon)

# Create the context menu for the tray icon
menu = QMenu()

# Store actions to prevent them from being garbage collected
actions = []

# Add menu items for each account
for name, pwd in PASSWORDS.items():
    action = QAction(name, tray)
    action.triggered.connect(lambda checked, p=pwd: copy_password(p))
    menu.addAction(action)
    actions.append(action)

# Add an exit action
exit_action = QAction("Exit", tray)
exit_action.triggered.connect(app.quit)
menu.addAction(exit_action)
actions.append(exit_action)

# Attach the menu to the tray icon and show it
tray.setContextMenu(menu)
tray.setVisible(True)
tray.show()

# Store references to menu and actions to prevent garbage collection
tray.menu = menu
tray.actions = actions

# Run the main application loop
sys.exit(app.exec_())
