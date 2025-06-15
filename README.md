# Password Tray App

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=flat&logo=qt&logoColor=white)
![Tray App](https://img.shields.io/badge/Tray_App-✓-blue)
![Cross-platform](https://img.shields.io/badge/Cross--platform-✓-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

A simple and cross-platform system tray application written in Python using PyQt5.  
It allows you to quickly copy passwords for different accounts and resources directly from your system tray.

---

## ✨ Features

- **Quick access** to passwords from the tray menu
- **Supports multiple resources and logins** (e.g., several "admin" accounts for different services)
- **Custom tray icon** support (with fallback to a default blue icon)
- **Cross-platform:** works on Windows, macOS, and Linux

---

## 🚀 Installation

1. **Clone the repository or download the script.**
2. **Install PyQt5** (if not already installed):

    ```
    pip install PyQt5
    ```

3. *(Optional)* Place your `icon.png` file in the same directory as the script for a custom tray icon.

---

## 🛠️ Usage

1. Run the script:

    ```
    python passpy.py
    ```

2. The app icon will appear in your system tray.
3. **Right-click** the tray icon to open the menu.
4. Click a menu item (formatted as `Resource — Login`) to **copy its password** to the clipboard.
5. Select **"Exit"** to close the application.

---

## ⚙️ Customization

- **Add or remove accounts:**  
  Edit the `ACCOUNTS` list in the script to set your own resources, logins, and passwords.

    ```
    ACCOUNTS = [
        {'resource': 'GitHub', 'login': 'admin', 'password': 'ghp_pass'},
        {'resource': 'Email', 'login': 'admin', 'password': 'mail_admin_pass'},
        {'resource': 'Server', 'login': 'root', 'password': 'server_root_pass'},
    ]
    ```

- **Change the tray icon:**  
  Place your own `icon.png` in the same directory as the script.  
  If the icon is missing or fails to load, a default blue icon will be used.

---

## 🐞 Troubleshooting

- **No tray icon appears:**  
  Make sure your OS supports tray icons and you have PyQt5 installed.
- **ModuleNotFoundError:**  
  Install PyQt5 with `pip install PyQt5`.
- **Icon not showing:**  
  Ensure `icon.png` is in the same folder as the script and is a valid PNG file.

---

## 📄 License

MIT License

---

## 👤 Author

Created by VioletSoul
