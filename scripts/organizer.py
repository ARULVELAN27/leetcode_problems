import json
import os


class Organizer:

    def __init__(self):
        print("Organizer Initialized")

        with open("../config/metadata.json", "r") as f:
            self.metadata = json.load(f)

    def create_structure(self):
        topics = set()

        for _, info in self.metadata.items():
            topics.add(info["primary_topic"])

        for topic in sorted(topics):
            for difficulty in ["Easy", "Medium", "Hard"]:
                os.makedirs(os.path.join("..", topic, difficulty), exist_ok=True)

        print(f"\n✅ Created {len(topics)} topic folders.")

    def dry_run(self):

        print("\n========== DRY RUN ==========\n")

        count = 0

        for problem_id, info in self.metadata.items():

            folder_name = f"{int(problem_id):04d}-{info['slug']}"

            destination = os.path.join(
                info["primary_topic"],
                info["difficulty"],
                f"{int(problem_id):04d} - {info['title']}"
            )

            print(f"{folder_name}")
            print(f"   ↓")
            print(f"{destination}\n")

            count += 1

            if count == 20:
                break

        print("Showing first 20 problems only.")

    def run(self):

        print(f"\nLoaded {len(self.metadata)} problems")

        self.create_structure()

        self.dry_run()