# Приложение Password Tray

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=flat&logo=qt&logoColor=white)
![Tray App](https://img.shields.io/badge/Tray_App-✓-blue)
![Cross-platform](https://img.shields.io/badge/Cross--platform-✓-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
[![Stars](https://img.shields.io/github/stars/VioletSoul/PassPy.svg?style=social)](https://github.com/VioletSoul/PassPy)
[![Last Commit](https://img.shields.io/github/last-commit/VioletSoul/PassPy.svg)](https://github.com/VioletSoul/PassPy/commits/main)

Простое и кроссплатформенное приложение для системного трея, написанное на Python с использованием PyQt5.  
Позволяет быстро копировать пароли для разных аккаунтов и ресурсов прямо из системного трея.

---

## ✨ Возможности

- **Быстрый доступ** к паролям из меню трея
- **Поддержка нескольких ресурсов и логинов** (например, несколько аккаунтов "admin" для разных сервисов)
- **Поддержка пользовательской иконки** трея (с запасной стандартной синей иконкой)
- **Кроссплатформенность:** работает на Windows, macOS и Linux

---

## 🚀 Установка

1. **Склонируйте репозиторий или скачайте скрипт.**
2. **Установите PyQt5** (если ещё не установлен):

    ```
    pip install PyQt5
    ```

3. *(Необязательно)* Поместите свой файл `icon.png` в ту же папку, что и скрипт, чтобы использовать свою иконку трея.

---

## 🛠️ Использование

1. Запустите скрипт:

    ```
    python passpy.py
    ```

2. Иконка приложения появится в системном трее.
3. **Кликните правой кнопкой мыши** по иконке трея, чтобы открыть меню.
4. Кликните по пункту меню (в формате `Ресурс — Логин`), чтобы **скопировать его пароль** в буфер обмена.
5. Выберите **"Выход"**, чтобы закрыть приложение.

---

## ⚙️ Настройка

- **Добавить или удалить аккаунты:**  
  Отредактируйте список `ACCOUNTS` в скрипте, чтобы указать свои ресурсы, логины и пароли.

    ```
    ACCOUNTS = [
        {'resource': 'GitHub', 'login': 'admin', 'password': 'ghp_pass'},
        {'resource': 'Email', 'login': 'admin', 'password': 'mail_admin_pass'},
        {'resource': 'Server', 'login': 'root', 'password': 'server_root_pass'},
    ]
    ```

- **Изменить иконку трея:**  
  Поместите свой `icon.png` в ту же папку, что и скрипт.  
  Если иконка отсутствует или не загружается, будет использована стандартная синяя иконка.

---

## 🐞 Устранение неполадок

- **Иконка трея не появляется:**  
  Убедитесь, что ваша ОС поддерживает иконки трея и установлен PyQt5.
- **ModuleNotFoundError:**  
  Установите PyQt5 с помощью `pip install PyQt5`.
- **Иконка не отображается:**  
  Проверьте, что файл `icon.png` находится в той же папке, что и скрипт, и является корректным PNG-файлом.

---

## 📄 Лицензия

MIT License

---

## 👤 Автор

Создано VioletSoul