=======
ProSi-3D: Robust and reliable process monitoring for Laser Powder Bed Fusion
=======

Dieses Repository beinhaltet den im Forschungsprojekt erarbeiteten Code sowie die Konfigurationsdateien, um diesen in einem Docker Container laufen zu lassen. Dies dient dazu, um die Paketabhängigkeiten für jede Plattform aufzulösen und auf dem Client keine Konflikte mit bestehenden Python-Installationen zu erzeugen.

Im Hauptverzeichnis befindet sich das Dockerfile, das die Konfiguration des Containers beschreibt. Die Basis ist eine Anaconda Installation mit Python 3. Die Abhängigkeiten sind in env/environment.yml zu finden. Sind weitere gewünscht, können diese hier einfach ergänzt werden.

Um den Container (einmalig) lokal zu erstellen, muss folgender Befehl im Hauptverzeichnis dieses Repositories in einem Terminal (Linux / OS X) oder der PowerShell ausgeführt werden:

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.0.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
