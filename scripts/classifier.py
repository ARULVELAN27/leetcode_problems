import json
import os


class Classifier:

    def __init__(self):

        file_path = os.path.join(
            "..",
            "config",
            "topics.json"
        )

        with open(file_path, "r") as f:
            self.topics = json.load(f)

    def get_topic(self, problem_id):

        return self.topics.get(
            str(problem_id),
            "Uncategorized"
        )