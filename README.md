# QR Code Decoder

Dies ist eine einfache Web-Anwendung, die entwickelt wurde, um QR-Codes zu erkennen und zu entschlüsseln. Sie ist in Python mit der Flask-Web-Framework und der OpenCV-Bibliothek für die QR-Code-Erkennung und -Entschlüsselung implementiert.


## Verwendung

Um die Anwendung zu starten, führen Sie das Python-Skript `app.py` aus:
python app.py


Öffnen Sie einen Webbrowser und navigieren Sie zu `http://localhost:5000`. Hier können Sie QR-Codes einfügen und die Anwendung versucht diese zu entschlüsseln. 

## Funktionsweise

Diese Anwendung nimmt einen QR-Code entgegen, entschlüsselt die darin enthaltenen Informationen und gibt diese zurück. 

Beim Einfügen eines Bildes in das Browserfenster wird ein `POST`-Request an den Server gesendet, welcher das eingefügte Bild enthält. Der Server entschlüsselt die in dem QR-Code enthaltenen Daten und sendet diese als Antwort zurück. Die Daten werden dann auf der Seite angezeigt und können in die Zwischenablage kopiert werden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. 
