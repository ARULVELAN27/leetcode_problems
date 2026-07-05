import json


class PriorityEngine:

    def __init__(self):

        with open("../config/topic_priority.json", "r") as f:
            self.priority = json.load(f)

    def get_primary_topic(self, tags):

        if not tags:
            return "Uncategorized"

        best_topic = None
        best_score = -1

        for tag in tags:

            score = self.priority.get(tag, 0)

            if score > best_score:
                best_score = score
                best_topic = tag

        return best_topic
if __name__ == "__main__":

    engine = PriorityEngine()

    print(engine.get_primary_topic([
        "Array",
        "Hash Table",
        "Sliding Window"
    ]))

    print(engine.get_primary_topic([
        "Array",
        "Binary Search"
    ]))

    print(engine.get_primary_topic([
        "String",
        "Dynamic Programming",
        "Two Pointers"
    ]))