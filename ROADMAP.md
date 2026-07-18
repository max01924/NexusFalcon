# **NEXUS FALCON \- Entwicklungs\-Roadmap**
## **PHASE 1: Projektsetup & Grundstruktur ✅**
**Status:** Bereit zu starten
**Ziel:** Funktionierende Entwicklungsumgebung mit sauberer Projektstruktur etablieren
**Features:**
- Python Virtual Environment
- Projektordner\-Struktur
- Dependency Management \(requirements\.txt\)
- Git Repository mit \.gitignore
- Basis\-Konfigurationsdatei
**Tasks:**
- \[ \] **✅** Virtual Environment erstellen und aktivieren
- \[ \] **✅** Projektordner\-Struktur anlegen \(src/, config/, data/, logs/\)
- \[ \] **✅** requirements\.txt mit initialen Dependencies \(tkinter sollte built\-in sein\)
- \[ \] **✅** \.gitignore erstellen \(venv, \.env, \*\.db, credentials\)
- \[ \] **✅** config\.py für zentrale Einstellungen \(Polling\-Intervall, etc\.\)
**Deliverables:**
- Lauffähige Python\-Umgebung
- Strukturiertes Projekt\-Verzeichnis
- Git\-Repository
**Timeline:** 1\-2 Stunden
**Was wird gebaut?** Die technische Grundlage \- kein funktionaler Code, nur Setup\.
**Warum jetzt?** Ohne saubere Basis wird später alles chaotisch\. Credential\-Management und Strukturierung müssen von Anfang an stimmen\.
**Tools/Libraries:**
- Python 3\.9\+
- venv
- git
**Wie wird getestet?** python \-\-version läuft, venv aktivierbar, Ordnerstruktur vorhanden\.
**Was danach?** Gmail API Anbindung kann starten, weil Credentials sicher gespeichert werden können\.
## **PHASE 2: Gmail API Integration ✅**
**Status:** Abhängig von Phase 1
**Ziel:** Erfolgreiches Abrufen von ungelesenen E\-Mails via Gmail API mit OAuth
**Features:**
- OAuth 2\.0 Flow für Gmail
- Credentials sicher speichern \(token\.json\)
- Ungelesene E\-Mails abrufen
- E\-Mail\-Metadaten parsen \(Absender, Betreff, Datum, Body\)
**Tasks:**
- \[ \] **✅** Google Cloud Project anlegen \(falls noch nicht vorhanden\)
- \[ \] **✅** Gmail API aktivieren
- \[ \] **✅** OAuth Credentials \(Desktop App\) erstellen und runterladen
- \[ \] **✅** google\-auth \+ google\-api\-python\-client installieren
- \[ \] **✅** OAuth Flow implementieren \(erster Start = Browser\-Login\)
- \[ \] **✅** Token\-Refresh\-Logik implementieren
- \[ \] **✅** Funktion: get\_unread\_emails\(\) \- gibt Liste von E\-Mail\-Objekten zurück
- \[ \] **✅** E\-Mail\-Body extrahieren \(Plain Text bevorzugt, HTML fallback\)
**Deliverables:**
- Python\-Modul gmail\_client\.py
- Gespeicherter OAuth Token \(token\.json\)
- Testskript das 5 ungelesene Mails abruft und auf Console printet
**Timeline:** 3\-5 Stunden \(inklusive Google Cloud Setup\)
**Was wird gebaut?** Die Verbindung zu Gmail \- Herzstück des Datenabrufs\.
**Warum jetzt?** Ohne E\-Mails gibt's nichts zu analysieren\. OAuth ist komplex und braucht früh Debugging\-Zeit\.
**Tools/Libraries:**
- google\-auth\-oauthlib
- google\-auth\-httplib2
- google\-api\-python\-client
**Wie wird getestet?** Standalone\-Script das authentifiziert, 5 ungelesene Mails holt und Subject \+ Sender printet\.
**Was danach?** Datenbank kann gebaut werden, weil wir wissen welche Datenstruktur gespeichert werden muss\.
## **PHASE 3: Datenbank\-Layer \(SQLite\) ✅**
**Status:** Abhängig von Phase 2
**Ziel:** Persistente Speicherung von E\-Mails in strukturierter Form
**Features:**
- SQLite\-Datenbank mit Schema
- Tabellen: emails \(full, summarized, tagged versions\)
- CRUD\-Operationen
- Duplikat\-Erkennung \(Gmail Message ID\)
**Tasks:**
- \[ \] **✅** Datenbank\-Schema entwerfen \(welche Felder brauchst du?\)
- \[ \] **✅** database\.py mit SQLite\-Connection erstellen
- \[ \] **✅** Tabelle emails anlegen \(id, gmail\_message\_id, sender, subject, date\_received, body\_full, body\_summary, ai\_tag\_sentence, is\_read, created\_at, replied\_at\)
- \[ \] **✅** Funktion: insert\_email\(\) \- speichert neue Mail
- \[ \] **✅** Funktion: get\_all\_emails\(\) \- gibt alle Mails zurück
- \[ \] **✅** Funktion: get\_email\_by\_id\(\) \- einzelne Mail
- \[ \] **✅** Funktion: update\_email\_summary\(\) \- KI\-Zusammenfassung nachträglich speichern
- \[ \] **✅** Duplikat\-Check \(gmail\_message\_id bereits in DB?\)
**Deliverables:**
- database\.py Modul
- SQLite DB\-Datei \(nexus\_falcon\.db\)
- Testskript das 3 Mails einfügt und wieder abruft
**Timeline:** 2\-4 Stunden
**Was wird gebaut?** Datenpersistenz \- der "Speicher" deiner App\.
**Warum jetzt?** Bevor wir KI\-Analysen machen, müssen wir wissen wo die gespeichert werden\. DB\-Design früh festlegen verhindert Refactoring\.
**Tools/Libraries:**
- sqlite3 \(built\-in Python\)
**Wie wird getestet?** Testskript fügt Mock\-E\-Mail ein, ruft sie ab, prüft ob Felder korrekt sind, löscht Testdaten\.
**Was danach?** KI\-Integration kann starten, weil wir Analyse\-Ergebnisse speichern können\.
## **PHASE 4: KI\-Integration \(Groq\) ✅**
**Status:** Abhängig von Phase 3
**Ziel:** E\-Mail\-Inhalte via Groq API analysieren und zusammenfassen
**Anpassung \(Nachtrag\):** Ursprünglich war OpenAI vorgesehen\. Aus finanziellen Gründen \(kein eigener OpenAI\-API\-Key\) wurde auf Groq umgestellt \- kostenloses Kontingent, gleiches Grundprinzip \(Chat\-Completion mit JSON\-Response\-Format\)\.
**Features:**
- Groq API Client
- Prompt Engineering für E\-Mail\-Analyse
- Zusammenfassung in Bulletpoints
- Ein\-Satz\-Tag generieren
- Floskeln entfernen
**Tasks:**
- \[ \] **✅** Groq Python Library installieren \(groq\)
- \[ \] **✅** API Key sicher speichern \(Umgebungsvariable GROQ\_API\_KEY\)
- \[ \] **✅** ai\_analyzer\.py Modul erstellen
- \[ \] **✅** Funktion: analyze\_email\(email\_body\) \- gibt Dict zurück \{body\_summary, ai\_tag\_sentence\}
- \[ \] **✅** Prompt schreiben: "Fasse folgende E\-Mail zusammen, entferne Floskeln\.\.\."
- \[ \] **✅** Modell\-Auswahl \(llama\-3\.3\-70b\-versatile über Groq \- kostenlos nutzbar\)
- \[ \] **✅** Error Handling \(leere Antwort, abgeschnittene Antwort durch Token\-Limit, ungültiges JSON\)
- \[ \] **✅** Integration mit DB: Nach Gmail\-Abruf \-> AI\-Analyse \-> DB speichern
**Deliverables:**
- ai\_analyzer\.py Modul
- Testskript das 3 echte E\-Mails analysiert und Output zeigt
- Pipeline: Gmail \-> AI \-> DB läuft durch
**Timeline:** 3\-4 Stunden
**Was wird gebaut?** Die "Intelligenz" \- Kern\-Feature deiner App\.
**Warum jetzt?** Wir haben Daten \(Gmail\) und Speicher \(DB\)\. Jetzt kommt die Verarbeitung\. Prompt Engineering braucht Iteration, daher früh starten\.
**Tools/Libraries:**
- groq
**Wie wird getestet?** 5 Test\-E\-Mails \(unterschiedliche Längen/Inhalte\) analysieren, Output manuell prüfen ob sinnvoll\.
**Was danach?** GUI kann gebaut werden, weil Backend\-Pipeline komplett ist\.
## **PHASE 5: Basic GUI \(Tkinter\) ⏳**
**Status:** Abhängig von Phase 4
**Ziel:** Minimale funktionsfähige Benutzeroberfläche zur E\-Mail\-Anzeige
**Features:**
- Hauptfenster mit E\-Mail\-Liste
- Detail\-Ansicht beim Klick
- Anzeige von: Absender, Betreff, Zusammenfassung, Original\-Text \(toggle\)
**Tasks:**
- \[ \] ⏳ gui\.py Hauptmodul erstellen
- \[ \] ⏳ Tkinter Hauptfenster mit Grundlayout
- \[ \] ⏳ Listbox/Treeview für E\-Mail\-Liste \(Absender, Betreff, Datum\)
- \[ \] ⏳ Detail\-Frame rechts: Zeigt selected E\-Mail
- \[ \] ⏳ Button: "Voller Inhalt" \(toggle zwischen Summary und Original\)
- \[ \] ⏳ DB\-Anbindung: Lädt E\-Mails beim Start und zeigt sie an
- \[ \] ⏳ Refresh\-Button \(lädt DB neu\)
**Deliverables:**
- Lauffähige GUI\-App \(main\.py startet GUI\)
- Zeigt gespeicherte E\-Mails aus DB an
- Klickbare Liste mit Details
**Timeline:** 4\-6 Stunden \(Tkinter\-Lernkurve\)
**Was wird gebaut?** Das Fenster zur Welt \- erste Interaktion mit deinem System\.
**Warum jetzt?** Backend läuft, jetzt visuelles Feedback\. Noch ohne Polling \- erst statische Anzeige von DB\-Daten\.
**Tools/Libraries:**
- tkinter \(built\-in\)
**Wie wird getestet?** App starten, 5 Test\-Mails in DB manuell einfügen, prüfen ob sie in GUI erscheinen und klickbar sind\.
**Was danach?** Background\-Polling kann integriert werden\.
## **PHASE 6: Background Polling & Threading ⏳**
**Status:** Abhängig von Phase 5
**Ziel:** Automatisches Abrufen neuer E\-Mails im Hintergrund ohne GUI\-Freeze
**Features:**
- Threading für Polling\-Loop
- Alle 5 Minuten Gmail abfragen
- Neue Mails \-> AI\-Analyse \-> DB speichern
- GUI aktualisiert sich automatisch
**Tasks:**
- \[ \] ⏳ polling\.py Modul mit Threading
- \[ \] ⏳ Funktion: start\_polling\_thread\(interval=300\) \- startet Background\-Thread
- \[ \] ⏳ Loop: Check Gmail \-> neue Mails? \-> AI\-Analyse \-> DB insert
- \[ \] ⏳ Thread\-safe GUI\-Update \(Queue oder after\(\)\)
- \[ \] ⏳ Stopp\-Mechanismus \(beim App\-Close Thread sauber beenden\)
- \[ \] ⏳ Error Handling in Thread \(Exceptions dürfen App nicht crashen\)
- \[ \] ⏳ Logging \(welche Mails wann abgerufen\)
**Deliverables:**
- Vollständig autonome App die alle 5 Min\. nach neuen Mails sucht
- Logs in logs/ Ordner
- Neue Mails erscheinen automatisch in GUI
**Timeline:** 3\-5 Stunden
**Was wird gebaut?** Automatisierung \- aus "Manuell\-Tool" wird "Background\-Service"\.
**Warum jetzt?** GUI läuft, Backend läuft\. Jetzt kommt Automation\. Threading ist komplex und braucht Testing\.
**Tools/Libraries:**
- threading \(built\-in\)
- queue \(built\-in, für thread\-safe communication\)
- logging \(built\-in\)
**Wie wird getestet?** Polling\-Intervall auf 30 Sekunden setzen, Test\-Mail schicken, prüfen ob sie innerhalb 30 Sek\. in GUI erscheint\.
**Was danach?** Benachrichtigungen können implementiert werden, weil wir Event\-Detection haben \(neue Mail\)\.
## **PHASE 7: Benachrichtigungssystem ⏳**
**Status:** Abhängig von Phase 6
**Ziel:** Desktop\-Notifications bei neuen E\-Mails mit Interaktivität \(Spotlight\-Style\)
**Features:**
- Native OS\-Benachrichtigungen \(Windows/macOS/Linux\)
- Anklickbar \-> öffnet Detail in GUI oder Mini\-Popup
- Zeigt: Absender, Ein\-Satz\-Summary, Zeit
- Optional: Snooze/Dismiss
**Tasks:**
- \[ \] ⏳ Library recherchieren \(plyer, plyer10toast für Windows, pync für macOS\)
- \[ \] ⏳ notification\.py Modul erstellen
- \[ \] ⏳ Funktion: show\_notification\(sender, summary\) \- zeigt OS\-Notification
- \[ \] ⏳ Click\-Handler: Bei Klick \-> GUI\-Fenster in Vordergrund \+ E\-Mail selektieren
- \[ \] ⏳ Integration mit Polling: Neue Mail \-> Notification triggern
- \[ \] ⏳ Settings: Notifications on/off toggle in GUI
**Deliverables:**
- Funktionierende Desktop\-Benachrichtigungen
- Klick auf Notification öffnet E\-Mail in App
**Timeline:** Zu definieren \(plattformabhängig\)
**Was wird gebaut?** Aufmerksamkeits\-System \- User wird über neue Mails informiert\.
**Warum jetzt?** Polling läuft, Events \(neue Mails\) erkannt\. Notifications sind logischer nächster Schritt\.
**Tools/Libraries:**
- plyer oder plyer10toast \(Windows\)
- pync \(macOS\)
- Oder OS\-spezifische Lösung
**Wie wird getestet?** Test\-Mail senden, warten bis Polling sie erkennt, prüfen ob Notification erscheint und anklickbar ist\.
**Was danach?** Antwort\-Funktionalität, weil User jetzt Mails sehen und darauf reagieren wollen\.
## **PHASE 8: E\-Mail Antwort\-Funktionalität ⏳**
**Status:** Abhängig von Phase 7
**Ziel:** Antworten auf E\-Mails direkt aus der App heraus senden
**Features:**
- "Antworten"\-Button in Detail\-Ansicht
- Textfeld für manuelle Antwort
- Optional: Bulletpoints eingeben \-> AI schreibt Mail
- Senden via Gmail API
- Sent\-Status in DB tracken
**Tasks:**
- \[ \] ⏳ GUI erweitern: "Antworten"\-Button \+ Textfeld \(toggle\)
- \[ \] ⏳ Radio\-Buttons: "Manuell schreiben" vs "AI generieren lassen"
- \[ \] ⏳ AI\-Modus: Bulletpoints\-Input \-> Groq generiert formelle Antwort
- \[ \] ⏳ Gmail API: send\_email\(to, subject, body\) Funktion
- \[ \] ⏳ Threading\-ID beibehalten \(Reply in Thread, nicht neue Mail\)
- \[ \] ⏳ Error Handling: Send failed \-> User\-Feedback
- \[ \] ⏳ DB: Sent\-Status speichern \(reply\_sent, reply\_timestamp\)
**Deliverables:**
- Voll funktionaler Reply\-Workflow in GUI
- KI\-generierte Antworten
- Gesendete Mails tracken
**Timeline:** Zu definieren
**Was wird gebaut?** Interaktivität \- aus "Read\-Only" wird "Read\-Write"\.
**Warum jetzt?** User sieht Mails, bekommt Notifications\. Nächster logischer Schritt: Antworten\.
**Tools/Libraries:**
- Gmail API \(bereits vorhanden\)
- Groq API \(bereits vorhanden\)
**Wie wird getestet?** Test\-Mail an dich selbst schicken, App öffnet sie, Reply verfassen \(manuell \+ AI\), prüfen ob in Gmail als Antwort erscheint\.
**Was danach?** Erweiterte UI\-Features für bessere UX\.
## **PHASE 9: Erweiterte UI Features ⏳**
**Status:** Abhängig von Phase 8
**Ziel:** Benutzerfreundlichkeit und Produktivität erhöhen
**Features:**
- Such\-/Filterfunktion \(nach Absender, Datum, Inhalt\)
- Mark as Read/Unread
- Archivieren \(aus Hauptliste ausblenden\)
- Settings\-Panel \(Polling\-Intervall anpassen, API Keys, Notifications on/off\)
- Keyboard Shortcuts \(Enter = Open Detail, Delete = Archive\)
**Tasks:**
- \[ \] ⏳ Suchleiste implementieren \(filtert E\-Mail\-Liste\)
- \[ \] ⏳ Context\-Menu \(Rechtsklick\): Mark as Read, Archive, Delete
- \[ \] ⏳ Settings\-Dialog mit Tkinter
- \[ \] ⏳ Keyboard Bindings
- \[ \] ⏳ DB erweitern: is\_archived Feld
- \[ \] ⏳ GUI\-Theming \(optional: dunkler Modus\)
**Deliverables:**
- Produktionsreife GUI mit allen wichtigen Features
- Settings persistent gespeichert \(config\.json oder DB\)
**Timeline:** Zu definieren
**Was wird gebaut?** Polish \- App wird von "funktioniert" zu "angenehm zu nutzen"\.
**Warum jetzt?** Kern\-Features fertig, jetzt Feinschliff für täglichen Gebrauch\.
**Tools/Libraries:**
- Tkinter \(weiter ausbauen\)
**Wie wird getestet?** User\-Testing: 1 Woche tägliche Nutzung, Feedback sammeln, Bugs fixen\.
**Was danach?** Testing & Deployment\.
## **PHASE 10: Testing & Deployment ⏳**
**Status:** Abhängig von Phase 9
**Ziel:** Stabile, deploybare Version der App
**Features:**
- Unit Tests für kritische Funktionen
- Integration Tests
- Error Logging
- Executable erstellen \(PyInstaller\)
- Dokumentation
**Tasks:**
- \[ \] ⏳ tests/ Ordner erstellen
- \[ \] ⏳ Unit Tests für DB\-Funktionen
- \[ \] ⏳ Unit Tests für Gmail/Groq Clients \(Mocking\)
- \[ \] ⏳ Integration Test: Vollständiger Flow \(Gmail \-> AI \-> DB \-> GUI\)
- \[ \] ⏳ Logging überarbeiten \(levels: INFO, WARNING, ERROR\)
- \[ \] ⏳ PyInstaller Config schreiben
- \[ \] ⏳ Executable bauen und auf frischem System testen
- \[ \] ⏳ README\.md schreiben \(Installation, Setup, Usage\)
**Deliverables:**
- Test\-Suite mit >80% Coverage
- Standalone\-Executable \(\.exe für Windows, \.app für macOS\)
- Dokumentation
**Timeline:** Zu definieren
**Was wird gebaut?** Qualitätssicherung \- App wird verlässlich und verteilbar\.
**Warum jetzt?** App ist feature\-complete, jetzt Stabilität sichern\.
**Tools/Libraries:**
- pytest
- unittest\.mock
- PyInstaller
**Wie wird getestet?** CI/CD wäre Overkill, aber: Tests lokal laufen lassen, Executable auf frischem Windows/macOS installieren, kompletten Workflow durchgehen\.
**Was danach?** Projekt ist produktionsreif\. Optionale Erweiterungen: Multi\-Account Support, Kalender\-Integration, Mobile App\.