# QR Code Decoder (English version below)

Dies ist eine einfache Web-Anwendung, die entwickelt wurde, um QR-Codes zu erkennen und zu entschlüsseln. Sie ist in Python mit der Flask-Web-Framework und der OpenCV-Bibliothek für die QR-Code-Erkennung und -Entschlüsselung implementiert.

## Vorteile

Diese Anwendung zeichnet sich durch folgende Eigenschaften aus:

- **Minimalistisch**: Die Anwendung ist extrem schlank und auf das Wesentliche beschränkt, ohne unnötige Funktionen oder Komplexität.
- **Einfache Bedienung**: Sie können mit dem Windows-Shortcut "Win + Shift + S" einfach QR-Codes ausschneiden und mit "Strg + V" in die Anwendung einfügen.
- **Keine Werbung oder Cookies**: Die Anwendung läuft vollkommen werbefrei und ohne Cookies oder ähnliche Tracking-Technologien.

## Verwendung

Um die Anwendung zu starten, führen Sie das Python-Skript `app.py` aus:
python app.py


Öffnen Sie einen Webbrowser und navigieren Sie zu `http://localhost:5000`. Hier können Sie QR-Codes einfügen und die Anwendung versucht diese zu entschlüsseln. 

## Funktionsweise

Diese Anwendung nimmt einen QR-Code entgegen, entschlüsselt die darin enthaltenen Informationen und gibt diese zurück. 

Beim Einfügen eines Bildes in das Browserfenster wird ein `POST`-Request an den Server gesendet, welcher das eingefügte Bild enthält. Der Server entschlüsselt die in dem QR-Code enthaltenen Daten und sendet diese als Antwort zurück. Die Daten werden dann auf der Seite angezeigt und können in die Zwischenablage kopiert werden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. 

# QR Code Decoder

This is a simple web application designed to recognize and decrypt QR codes. It is implemented in Python using the Flask web framework and the OpenCV library for QR code detection and decryption.

## Benefits

This application stands out due to the following features:

- **Minimalist**: The application is extremely lean and focuses on the essentials, without unnecessary functions or complexity.
- **Easy to Use**: You can easily cut out QR codes with the Windows shortcut "Win + Shift + S" and paste them into the application with "Ctrl + V".
- **No Ads or Cookies**: The application runs completely ad-free and without cookies or similar tracking technologies.

## Usage

To start the application, run the Python script `app.py`:python app.py


Open a web browser and navigate to `http://localhost:5000`. Here, you can paste QR codes and the application will attempt to decrypt them.

## How it Works

This application takes a QR code, decrypts the information contained within it, and returns it. 

When you paste an image into the browser window, a `POST` request is sent to the server containing the pasted image. The server decrypts the data contained in the QR code and sends it back as a response. The data is then displayed on the page and can be copied to the clipboard.

## License

This project is under the MIT License.


