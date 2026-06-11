import sys
sys.path.append("src")
from ai_analyzer import analyze_email

email_body = """
Hallo zusammen,

ich möchte kurz ein Update zum Projekt "Phoenix" geben und gleichzeitig einige offene Punkte ansprechen, da wir uns mittlerweile dem ursprünglich geplanten Go-Live am 15.07.2026 nähern.

Zunächst die gute Nachricht: Das Entwicklungsteam hat die Implementierung des neuen Authentifizierungsmoduls gestern Abend gegen 21:30 Uhr erfolgreich abgeschlossen. Die internen Tests verliefen weitgehend positiv. Allerdings wurden bei den letzten Lasttests auf dem Staging-System sporadische Antwortzeiten von über 4,5 Sekunden gemessen, insbesondere bei gleichzeitigen Anfragen von mehr als 2.000 Nutzern.

In diesem Zusammenhang bitte ich Thomas Müller und Sarah Chen darum, bis spätestens kommenden Dienstag eine Einschätzung abzugeben, ob die aktuelle Infrastruktur ausreichend dimensioniert ist oder ob zusätzliche Cloud-Ressourcen erforderlich werden. Bitte berücksichtigt dabei sowohl die europäischen als auch die asiatischen Nutzergruppen.

Ein weiterer Punkt betrifft das Budget. Nach aktueller Hochrechnung liegen wir bei Gesamtkosten von etwa 482.700 EUR und damit rund 12,4 % über der ursprünglichen Planung. Der Hauptgrund hierfür sind zusätzliche Lizenzkosten sowie die kurzfristige Beauftragung externer Berater im April und Mai.

Zur besseren Übersicht hier die wichtigsten Zahlen:

* Ursprüngliches Budget: 429.500 EUR
* Aktuelle Prognose: 482.700 EUR
* Erwartete Mehrausgaben: 53.200 EUR
* Bereits freigegeben: 470.000 EUR

Ich bin nicht sicher, ob wir diese Überschreitung intern noch auffangen können oder ob eine zusätzliche Genehmigung durch das Management erforderlich ist. Ehrlich gesagt wäre mir Variante A deutlich lieber, aber vielleicht sehe ich die Lage auch zu pessimistisch.

Außerdem gab es gestern ein Gespräch mit unserem Kunden in Singapur. Dort wurde erneut der Wunsch geäußert, bestimmte KI-Funktionen früher bereitzustellen. Offiziell wurde keine Frist genannt, zwischen den Zeilen klang jedoch ein Termin Ende August durch. Bitte behandelt diese Information vorerst als vertraulich.

Organisatorisch noch zwei Hinweise:

1. Das Meeting am Freitag findet nicht um 09:00 Uhr statt, sondern voraussichtlich um 08:30 Uhr. Die endgültige Bestätigung folgt noch.
2. Die Reise nach München wurde vorläufig genehmigt, allerdings fehlen noch die Hotelbuchungen.

Anbei sollten folgende Dokumente enthalten sein:

* Budget_Report_v3.xlsx
* Infrastructure_Assessment.pdf
* Meeting_Notes_Singapore.docx

Falls die Dateien fehlen, informiert mich bitte zeitnah. Beim letzten Versand gab es offenbar Probleme mit dem Mailserver.

Persönlich glaube ich weiterhin, dass wir den Termin halten können. Andererseits habe ich vor drei Monaten auch gesagt, dass wir definitiv im Budget bleiben werden – man sieht also, dass Prognosen manchmal mit Vorsicht zu genießen sind.

Für Rückfragen bin ich heute bis etwa 17:00 Uhr telefonisch erreichbar. Danach befinde ich mich voraussichtlich im Zug zwischen Chemnitz und München und habe nur eingeschränkten Empfang.

Viele Grüße

Max Mustermann
Projektleiter Digital Solutions
TechVision Europe GmbH

Mobil: +49 171 1234567
E-Mail: [max.mustermann@example.com](mailto:max.mustermann@example.com)
Personalnummer: TVE-2026-18473
"""

result = analyze_email(email_body)
print("Summary:")
for point in result["summary"]:
    print(f"- {point}")
print(f"\n Ein-Satz-Zusammenfassung: {result['one_sentence']}")