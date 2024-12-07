import datetime
import json
import logging

# Логика учета атак


class AttackCounter:
    def __init__(self, filename="attack_count.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {
                "total_attacks": 0,
                "daily_attacks": {},
                "attack_durations": [],
            }
        else:
            if "attack_durations" not in self.data:
                self.data["attack_durations"] = []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def record_attack_start(self):
        self.attack_start_time = datetime.datetime.now()

    def record_attack_end(self):
        if not hasattr(self, "attack_start_time"):
            logging.error("Начало атаки не было записано!")
            return

        attack_end_time = datetime.datetime.now()
        duration = (attack_end_time - self.attack_start_time).total_seconds()
        self.data["attack_durations"].append(duration)
        self.data["total_attacks"] += 1

        today = datetime.date.today().isoformat()
        if today not in self.data["daily_attacks"]:
            self.data["daily_attacks"][today] = 0

        self.data["daily_attacks"][today] += 1

        logging.info("Записал окончание атаки с длительностью: %.2f секунд" % duration)

        self.save_data()

    def get_total_attacks(self):
        return self.data["total_attacks"]

    def get_daily_attacks(self, date=None):
        if date is None:
            date = datetime.date.today().isoformat()
        return self.data["daily_attacks"].get(date, 0)

    def get_avg_attack_duration(self):
        if not self.data["attack_durations"]:
            return 0

        return sum(self.data["attack_durations"]) / len(self.data["attack_durations"])


if __name__ == "__main__":
    counter = AttackCounter()
    counter.record_attack_start()
    import time

    time.sleep(2)
    counter.record_attack_end()
