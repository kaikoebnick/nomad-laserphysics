import json
import os


class NomadCounter:
    def __init__(self, data_dir="./.volumes/fs/staging", counter_file="counter.json"):
        # Verzeichnis, in dem die NOMAD-Daten gespeichert werden
        self.data_dir = data_dir
        # Datei zur Speicherung des Zählers
        self.counter_file = os.path.join(data_dir, counter_file)
        self.counter = self._load_counter()

    def _load_counter(self):
        """Lädt den gespeicherten Zähler aus der Datei oder initialisiert ihn."""
        if os.path.exists(self.counter_file):
            with open(self.counter_file) as f:
                return json.load(f).get("count", 0)
        return 0

    def _save_counter(self):
        """Speichert den aktuellen Zählerstand in die Datei."""
        with open(self.counter_file, "w") as f:
            json.dump({"count": self.counter}, f)

    def count_entries(self):
        """Zählt die vorhandenen Einträge im Datenverzeichnis."""
        entries = -1
        try:
            entries = [
                entry
                for entry in os.listdir(self.data_dir)
                if os.path.isdir(os.path.join(self.data_dir, entry))
            ]
        except Exception as e:
            print(f"Fehler beim Zählen der Einträge: {e}")
        return entries

    def update_counter(self):
        """Vergleicht gezählte Einträge mit gespeichertem Zähler, aktualisiert ihn."""
        current_count = self.count_entries()
        if current_count > self.counter:
            self.counter = current_count
            self._save_counter()
        return self.counter

    def get_counter(self):
        """Gibt den aktuellen Wert des Zählers zurück."""
        return self.counter

# Beispielnutzung
if __name__ == "__main__":
    nomad_path = "/pfad/zu/nomad/daten"  # Diesen Pfad anpassen
    counter = NomadCounter(nomad_path)
    counter.update_counter()
    print(f"Aktuelle Anzahl der Einträge: {counter.get_counter()}")
