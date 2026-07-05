import json
import os
import sys

sys.path.append("..")

from helpers import is_problem_folder, extract_problem_id
from models.move_plan import MovePlan


ROOT = ".."


class MovePlanner:

    def __init__(self):

        with open("../config/metadata.json", "r") as f:
            self.metadata = json.load(f)

        self.moves = []

    def build(self):

        folders = sorted(os.listdir(ROOT))

        for folder in folders:

            if not is_problem_folder(folder):
                continue

            problem_id = extract_problem_id(folder)

            if problem_id not in self.metadata:
                print(f"Skipping {folder}")
                continue

            info = self.metadata[problem_id]

            destination = os.path.join(
                info["primary_topic"],
                info["difficulty"],
                info["folder_name"]
            )

            move = MovePlan(
                problem_id=int(problem_id),
                source=folder,
                destination=destination
            )

            self.moves.append(move)

    def save(self):

        data = {
            "generated_moves": len(self.moves),
            "moves": [
                move.to_dict()
                for move in self.moves
            ]
        }

        with open("../logs/move_plan.json", "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )

        print(f"\n✅ Move plan created successfully!")
        print(f"Total Moves : {len(self.moves)}")

    def preview(self, count=20):

        print("\n========== MOVE PREVIEW ==========\n")

        for move in self.moves[:count]:

            print(move.source)

            print("   ↓")

            print(move.destination)

            print()

        print(f"Showing first {count} moves.")

    def run(self):

        self.build()

        self.preview()

        self.save()


if __name__ == "__main__":

    planner = MovePlanner()

    planner.run()