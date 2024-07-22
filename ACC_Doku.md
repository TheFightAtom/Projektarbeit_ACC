# Dokumentation ACC & Integration Lidar/Radar

Projektmodul
Projektleiter: Professor Krug, William Engel

Abgabe: 23.07.2024

Christopher Bautz
FAB7
christopher.bautz@hm.edu



# 1. Einleitung


In diesem Projekt wird ein System entwickelt, das die Daten eines Lidarsensors mit Kamerabildern kombiniert, um die Erkennung und Verfolgung von Objekten in Echtzeit zu verbessern. Diese Fusion verschiedener Sensordaten ist besonders für autonome Fahrzeuge nützlich, da sie eine robustere und genauere Erkennung der Umgebung ermöglicht. Dies wird durch die Stärken der einzelnen Sensoren erreicht: Lidar liefert präzise Abstandsmessungen, während Kameras detaillierte visuelle Informationen liefern.

Das gesamte System wird in Python unter Verwendung des Robot Operating System (ROS) implementiert. ROS bietet eine flexible Kommunikationsinfrastruktur und ist in der Robotik weit verbreitet. Es ermöglicht eine effiziente Verteilung von Sensordaten und die Implementierung komplexer Algorithmen zur Sensorfusion und Entscheidungsfindung. In diesem Projekt wurden ROS-Knoten entwickelt, die unter anderem Lidardaten verarbeiten, Kamerabilder empfangen, Sensorfusion durchführen und die Ergebnisse zur weiteren Verarbeitung und Analyse bereitstellen.

Die Integration dieser Sensoren erfolgt durch eine Kombination von ROS-Nachrichten, Transformationsrahmen und Bildverarbeitungsalgorithmen. Besonderes Augenmerk wird auf die Echtzeitfähigkeit des Systems gelegt, um eine kontinuierliche und zuverlässige Objekterkennung und -verfolgung zu gewährleisten. Die Anwendung von Kalibrierungsmethoden und die kontinuierliche Überprüfung der Systemleistung stellen darüber hinaus eine hohe Genauigkeit der fusionierten Sensordaten sicher.

Diese Dokumentation beschreibt die Implementierung des Systems, die verwendeten Algorithmen zur Sensorfusion und die durchgeführten Tests zur Validierung der Ergebnisse. Ziel ist die Entwicklung eines zuverlässigen und effizienten Objekterkennungssystems für autonome Modellfahrzeuge.


# 2. ACC / Integration Lidar / Fusion Lidar mit Kamera

~~Dieses Kapitel beschreibt die verschiedenen Aspekte der Implementierung der ACC/Lidar/Kamera Funktionen für das autonome Modellfahrzeug. Es werden die einzelnen Komponenten des Systems detailliert erläutert, einschließlich ihrer Initialisierung, der Lidar-Punkt-Projektion, der Mittellinienerkennung, der Streckenbegrenzung, der Geschwindigkeitsberechnung, der Visualisierung, der Objekterkennung, der Kalibrierung und schließlich der Integration all dieser Komponenten im Gesamtsystem.~~

## 2.1 Initialisierungen

~~Dieses Unterkapitel behandelt die Initialisierung der ROS-Knoten, die Einrichtung der verschiedenen Abonnements und Veröffentlichungen sowie die Definition der Callback-Funktionen. Es wird beschrieben, wie die verschiedenen Sensoren (Lidar, Kamera, etc.) konfiguriert und eingebunden werden. Zudem wird erläutert, wie die Kamerainformationen periodisch veröffentlicht werden, um die Kalibrierung und Synchronisation zwischen den Sensoren zu unterstützen.~~

## 2.2 Lidar-Punkt-Projektion

~~Hier wird die Projektion der Lidar-Punkte auf die Bildebene der Kamera erläutert. Dieser Prozess umfasst die Transformation der Lidar-Daten in das Kamerakoordinatensystem und die Anwendung einer Kalibrierungsfunktion, um die Punkte korrekt zu skalieren und zu positionieren. Diese Projektion ist entscheidend für die Fusion der Sensordaten und die nachfolgende Verarbeitung.~~

## 2.3 Mittellinienerkennung

~~In diesem Abschnitt wird beschrieben, wie die Mittellinie der Fahrspur erkannt und verfolgt wird. Die Mittellinienerkennung nutzt die Lidar-Daten, um eine zuverlässige Spurführung zu ermöglichen. Es werden Algorithmen zur Erkennung und Verfolgung der Mittellinie vorgestellt sowie die Methoden zur Verarbeitung und Speicherung der erkannten Linienpunkte erläutert.~~

## 2.2 Lidar-Punkt-Projektion

~~Hier wird die Projektion der Lidar-Punkte auf die Bildebene der Kamera erläutert. Dieser Prozess umfasst die Transformation der Lidar-Daten in das Kamerakoordinatensystem und die Anwendung einer Kalibrierungsfunktion, um die Punkte korrekt zu skalieren und zu positionieren. Diese Projektion ist entscheidend für die Fusion der Sensordaten und die nachfolgende Verarbeitung.~~

## 2.4 Streckenbegrenzung

~~Dieses Unterkapitel beschreibt die Erkennung und Verfolgung der seitlichen Streckenbegrenzungen. Die Informationen über die Streckenbegrenzungen werden verwendet, um das Fahrzeug sicher auf der Fahrspur zu halten und mögliche Kollisionen zu vermeiden. Es wird erläutert, wie die Begrenzungslinien basierend auf den Lidar-Daten erkannt und extrapoliert werden.~~

## 2.5 Geschwindigkeitsberechnung

~~Hier wird die Berechnung der Geschwindigkeit des vorausfahrenden Fahrzeugs behandelt. Es wird erläutert, wie die Lidar-Daten verwendet werden, um die relative Geschwindigkeit zu berechnen und wie diese Information in die adaptive Geschwindigkeitsregelung (ACC) integriert wird. Zudem wird der Einsatz von Filtern zur Glättung der Geschwindigkeitsmessungen beschrieben.~~

## 2.6 Visualisierung

~~In diesem Abschnitt wird die Visualisierung der Sensordaten und der Ergebnisse der Datenverarbeitung erläutert. Es wird beschrieben, wie die Lidar-Punkte und die erkannten Objekte auf den Kamerabildern visualisiert werden, um eine anschauliche Darstellung der Umgebung zu ermöglichen. Diese Visualisierung unterstützt die Entwicklung und Fehlerbehebung des Systems.~~

## 2.7 Objekterkennung

~~Dieses Unterkapitel behandelt die Integration der Objekterkennung in das System. Es wird beschrieben, wie die von der Kamera erkannten Objekte mit den Lidar-Daten kombiniert werden, um genaue Positions- und Abstandsangaben zu erhalten. Die Objekterkennung spielt eine entscheidende Rolle bei der Navigation und Entscheidungsfindung des autonomen Fahrzeugs.~~

## 2.8 Kalibrierung

~~Hier wird der Kalibrierungsprozess des Systems erläutert. Es wird beschrieben, wie die Lidar-Daten kalibriert werden, um genaue Messungen zu gewährleisten, und wie die Kalibrierungsdaten gesammelt und verarbeitet werden. Die Kalibrierung ist entscheidend für die Genauigkeit und Zuverlässigkeit des gesamten Systems.~~


![Kalibrierung 1](https://raw.githubusercontent.com/TheFightAtom/Projektarbeit_ACC/master/Pictures/Kalibrierung_Fusion_Bild1.png)
![Kalibrierung 2](https://raw.githubusercontent.com/TheFightAtom/Projektarbeit_ACC/master/Pictures/Kalibrierung_Fusion_Bild2.png)

## 2.9 Gesamtumsetzung / main

~~Dieses Unterkapitel beschreibt die Integration aller zuvor erläuterten Komponenten in einem Gesamtprozess. Es wird detailliert erläutert, wie die verschiedenen Sensordaten zusammengeführt und verarbeitet werden, um eine zuverlässige und effiziente Navigation des autonomen Fahrzeugs zu gewährleisten. Hier wird auch der Ablauf der Hauptverarbeitungsroutine dargestellt, die die kontinuierliche Erfassung, Verarbeitung und Entscheidung ermöglicht.~~



# 3. Radar Test

Im Rahmen dieses Projektes wurde das Radar der Firma RadarIQ getestet und auf seine Eignung für unsere Anwendung geprüft. Das Radar bietet grundsätzlich vielversprechende Möglichkeiten zur Objekterkennung und -verfolgung. Allerdings traten bei der Integration in unser System erhebliche Probleme auf, die insbesondere auf die mangelnde Unterstützung durch den Hersteller zurückzuführen sind.

Das größte Problem, das während der Tests auftrat, war das Ende des Supports für alle Software und Informationen durch den Hersteller. Die offizielle Windows Standalone Software ist nicht mehr verfügbar und auch die Informationen zur Integration des Radars in das Robot Operating System (ROS) fehlen vollständig. Dies stellte uns vor die Herausforderung, das Radar ohne Unterstützung der vorgesehenen Tools in Betrieb zu nehmen.

Da die herstellereigene Software nicht mehr verfügbar war, blieb nur die Möglichkeit, das Radar über die Python-Schnittstelle zu nutzen. Diese bietet grundlegende Funktionen zur Steuerung und Auswertung der Radardaten. Trotz dieser Einschränkungen konnten wir das Radar erfolgreich testen und die gewonnenen Daten visualisieren. Dazu wurde ein 3D-Plot erstellt, der die vom Radar erfassten Punkte darstellt. Diese Visualisierung half uns, die Funktionsweise und die Erkennungsgenauigkeit des Radars besser zu verstehen.

![Radar Plot](https://raw.githubusercontent.com/TheFightAtom/Projektarbeit_ACC/master/Pictures/Radar_Plot.png)

Die Testergebnisse zeigten, dass das Radar in der Lage ist, Objekte in seiner Umgebung zu erkennen. Die fehlende Unterstützung durch den Hersteller wird jedoch die zukünftige Integration des Radars in unser System erheblich erschweren. Insbesondere die fehlende ROS-Integration stellt ein großes Hindernis dar, da wir dadurch keine nahtlose Kommunikation zwischen den verschiedenen Sensoren und Komponenten unseres Projektes gewährleisten können.

Zusammenfassend lässt sich sagen, dass das Radar zwar prinzipiell für unsere Anwendung geeignet wäre, aber die fehlende Unterstützung und die damit verbundenen technischen Herausforderungen eine vollständige Integration in unser System problematisch machen. Zukünftige Arbeiten sollten daher entweder auf eine Lösung zur Integration des Radars in ROS abzielen oder alternative Radarsysteme mit besserer Unterstützung und Dokumentation in Betracht ziehen.


# 4. Fazit und Ausblick

In diesem Projekt wurde erfolgreich demonstriert, wie die Lidar-Technologie effektiv bei der Entwicklung autonomer Fahrzeuge eingesetzt werden kann. Lidar spielte eine zentrale Rolle bei der Erfassung und Verarbeitung von Umgebungsdaten, die für verschiedene Aspekte der Fahrzeugnavigation und -steuerung von entscheidender Bedeutung sind.

Durch die Integration von Lidar-Daten konnten Abstand und Geschwindigkeit des vorausfahrenden Fahrzeugs genau bestimmt werden. Dies ist für die adaptive Geschwindigkeitsregelung (ACC) unerlässlich, um ein sicheres und effizientes Fahren zu gewährleisten. Darüber hinaus wurden die Lidar-Daten verwendet, um den Abstand von Objekten, die durch die Objekterkennung identifiziert wurden, genau zu bestimmen, was die Genauigkeit und Zuverlässigkeit des Systems weiter erhöht. Dies alles unter Berücksichtigung der Streckenbeschränkungen.

Durch die Fusion von Lidar-Daten mit Kamerabildern konnte eine robustere und genauere Umgebungserkennung erreicht werden. Dies wurde durch den Einsatz von ROS und verschiedenen Bildverarbeitungsalgorithmen ermöglicht, die eine Echtzeitverarbeitung der Sensordaten sicherstellten. Darüber hinaus wurde das Lidar kalibriert, um die Messgenauigkeit zu gewährleisten und zuverlässige Daten für die Entscheidungsfindung zu liefern.

Der entwickelte Code bietet eine solide Grundlage für die weitere Optimierung und Erweiterung des Systems. Ein Bereich, der noch verbessert werden kann, ist die Linienerkennung. Sobald eine verbesserte Linienerkennung implementiert ist, können weitere Schritte unternommen werden, um die erkannten Linien als seitliche Begrenzungen für das autonome Fahren zu nutzen. Diese Erweiterung würde die Navigation des Fahrzeugs in komplexeren Umgebungen weiter verbessern.

Insgesamt zeigt dieses Projekt, dass die Lidar-Technologie ein wesentlicher Bestandteil autonomer Fahrzeugsysteme ist. Durch die kontinuierliche Weiterentwicklung und Optimierung des Codes sowie die Integration zusätzlicher Sensoren und Algorithmen kann die Leistungsfähigkeit und Sicherheit autonomer Fahrzeuge weiter gesteigert werden.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY0Nzc1MTg4LC0xNDU2OTk4MTkxLDI1ND
A2MzY5MiwtMTgwNDIwNjcxMiwtMjQ0NjQxNzQzLC0xMTMzMjYx
MDAxXX0=
-->