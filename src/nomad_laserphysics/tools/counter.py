import json
import os
import threading

LOCK = threading.Lock()


class NomadCounter:
    def __init__(self, data_dir="/app/.volumes/counter", counter_file="counter.json"):
        self.data_dir = data_dir
        self.counter_file = os.path.join(data_dir, counter_file)
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f:
                json.dump({"counter": 1, "id": "a"}, f)


    def get_counter_and_update(self, entry_id):
        """Reads counter-value, increments it and returns the pre-increment value"""
        with LOCK:
            if not os.path.exists(self.counter_file):
                data = {"counter": 1, "ids": [entry_id]}
            else:
                with open(self.counter_file) as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = {"counter": 1, "ids": [entry_id]}

            if entry_id in data.get("ids", []):
                return str(data["counter"]).zfill(5)

            data["counter"] += 1
            data.setdefault("ids", []).append(entry_id)

            with open(self.counter_file, "w") as f:
                json.dump(data, f)

            return str(data["counter"]).zfill(5)

