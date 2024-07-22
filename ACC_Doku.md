# Dokumentation ACC & Integration Lidar/Radar

Projektmodul
Projektleiter: Professor Krug, William Engel

Abgabe: 23.07.2024

Christopher Bautz
FAB7
christopher.bautz@hm.edu



# Einleitung


In diesem Projekt wird ein System entwickelt, das die Daten eines Lidarsensors mit Kamerabildern kombiniert, um die Erkennung und Verfolgung von Objekten in Echtzeit zu verbessern. Diese Fusion verschiedener Sensordaten ist besonders für autonome Fahrzeuge nützlich, da sie eine robustere und genauere Erkennung der Umgebung ermöglicht. Dies wird durch die Stärken der einzelnen Sensoren erreicht: Lidar liefert präzise Abstandsmessungen, während Kameras detaillierte visuelle Informationen liefern.

Das gesamte System wird in Python unter Verwendung des Robot Operating System (ROS) implementiert. ROS bietet eine flexible Kommunikationsinfrastruktur und ist in der Robotik weit verbreitet. Es ermöglicht eine effiziente Verteilung von Sensordaten und die Implementierung komplexer Algorithmen zur Sensorfusion und Entscheidungsfindung. In diesem Projekt wurden ROS-Knoten entwickelt, die unter anderem Lidardaten verarbeiten, Kamerabilder empfangen, Sensorfusion durchführen und die Ergebnisse zur weiteren Verarbeitung und Analyse bereitstellen.

Die Integration dieser Sensoren erfolgt durch eine Kombination von ROS-Nachrichten, Transformationsrahmen und Bildverarbeitungsalgorithmen. Besonderes Augenmerk wird auf die Echtzeitfähigkeit des Systems gelegt, um eine kontinuierliche und zuverlässige Objekterkennung und -verfolgung zu gewährleisten. Die Anwendung von Kalibrierungsmethoden und die kontinuierliche Überprüfung der Systemleistung stellen darüber hinaus eine hohe Genauigkeit der fusionierten Sensordaten sicher.

Diese Dokumentation beschreibt die Implementierung des Systems, die verwendeten Algorithmen zur Sensorfusion und die durchgeführten Tests zur Validierung der Ergebnisse. Ziel ist die Entwicklung eines zuverlässigen und effizienten Objekterkennungssystems für autonome Modellfahrzeuge.


# ACC / Integration Lidar / Fusion Lidar mit Kamera

Text

## Unterüberschrift 1

Text

## Unterüberschrift 1

Text

# Radar Test

Im Rahmen dieses Projektes wurde das Radar der Firma RadarIQ getestet und auf seine Eignung für unsere Anwendung geprüft. Das Radar bietet grundsätzlich vielversprechende Möglichkeiten zur Objekterkennung und -verfolgung. Allerdings traten bei der Integration in unser System erhebliche Probleme auf, die insbesondere auf die mangelnde Unterstützung durch den Hersteller zurückzuführen sind.

Das größte Problem, das während der Tests auftrat, war das Ende des Supports für alle Software und Informationen durch den Hersteller. Die offizielle Windows Standalone Software ist nicht mehr verfügbar und auch die Informationen zur Integration des Radars in das Robot Operating System (ROS) fehlen vollständig. Dies stellte uns vor die Herausforderung, das Radar ohne Unterstützung der vorgesehenen Tools in Betrieb zu nehmen.

Da die herstellereigene Software nicht mehr verfügbar war, blieb nur die Möglichkeit, das Radar über die Python-Schnittstelle zu nutzen. Diese bietet grundlegende Funktionen zur Steuerung und Auswertung der Radardaten. Trotz dieser Einschränkungen konnten wir das Radar erfolgreich testen und die gewonnenen Daten visualisieren. Dazu wurde ein 3D-Plot erstellt, der die vom Radar erfassten Punkte darstellt. Diese Visualisierung half uns, die Funktionsweise und die Erkennungsgenauigkeit des Radars besser zu verstehen.

![Radar Plot](https://raw.githubusercontent.com/TheFightAtom/Projektarbeit_ACC/master/Pictures/Radar_Plot.png)

Die Testergebnisse zeigten, dass das Radar in der Lage ist, Objekte in seiner Umgebung zu erkennen. Die fehlende Unterstützung durch den Hersteller wird jedoch die zukünftige Integration des Radars in unser System erheblich erschweren. Insbesondere die fehlende ROS-Integration stellt ein großes Hindernis dar, da wir dadurch keine nahtlose Kommunikation zwischen den verschiedenen Sensoren und Komponenten unseres Projektes gewährleisten können.

Zusammenfassend lässt sich sagen, dass das Radar zwar prinzipiell für unsere Anwendung geeignet wäre, aber die fehlende Unterstützung und die damit verbundenen technischen Herausforderungen eine vollständige Integration in unser System problematisch machen. Zukünftige Arbeiten sollten daher entweder auf eine Lösung zur Integration des Radars in ROS abzielen oder alternative Radarsysteme mit besserer Unterstützung und Dokumentation in Betracht ziehen.


# Fazit und Ausblick

In diesem Projekt wurde erfolgreich demonstriert, wie die Lidar-Technologie effektiv bei der Entwicklung autonomer Fahrzeuge eingesetzt werden kann. Lidar spielte eine zentrale Rolle bei der Erfassung und Verarbeitung von Umgebungsdaten, die für verschiedene Aspekte der Fahrzeugnavigation und -steuerung von entscheidender Bedeutung sind.

Durch die Integration von Lidar-Daten konnte der Abstand und die Geschwindigkeit des vorausfahrenden Fahrzeugs genau bestimmt werden. Dies ist für die adaptive Geschwindigkeitsregelung (ACC) unerlässlich, um ein sicheres und effizientes Fahren zu gewährleisten. Darüber hinaus wurden die Lidar-Daten verwendet, um den Abstand von Objekten, die durch die Objekterkennung identifiziert wurden, genau zu bestimmen, was die Genauigkeit und Zuverlässigkeit des Systems weiter erhöhte.

Ein weiterer wichtiger Aspekt in diesem Projekt war die Berücksichtigung von Streckenbegrenzungen. Das Lidar ermöglichte es, die Mittellinie der Fahrspur zu erkennen und zu verfolgen. Diese Informationen sind entscheidend, um das Fahrzeug sicher in der Spur zu halten und Kollisionen zu vermeiden.

Durch die Fusion von Lidar-Daten mit Kamerabildern konnte eine robustere und genauere Umgebungserkennung erreicht werden. Dies wurde durch den Einsatz von ROS und verschiedenen Bildverarbeitungsalgorithmen ermöglicht, die eine Echtzeitverarbeitung der Sensordaten sicherstellten. Darüber hinaus wurde das Lidar kalibriert, um die Genauigkeit der Messungen

Der entwickelte Code bietet eine solide Grundlage für die weitere Optimierung und Erweiterung des Systems. Ein Bereich, der noch verbessert werden kann, ist die Linienerkennung. Sobald eine verbesserte Linienerkennung implementiert ist, können weitere Schritte unternommen werden, um die erkannten Linien als seitliche Begrenzungen für das autonome Fahren zu nutzen. Diese Erweiterung würde die Navigation des Fahrzeugs in komplexeren Umgebungen weiter verbessern.

Insgesamt zeigt dieses Projekt, dass die Lidar-Technologie ein wesentlicher Bestandteil autonomer Fahrzeugsysteme ist. Durch die kontinuierliche Weiterentwicklung und Optimierung des Codes sowie die Integration zusätzlicher Sensoren und Algorithmen kann die Leistungsfähigkeit und Sicherheit autonomer Fahrzeuge weiter gesteigert werden.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExOTMwMDM3MCwyNTQwNjM2OTIsLTE4MD
QyMDY3MTIsLTI0NDY0MTc0MywtMTEzMzI2MTAwMV19
-->