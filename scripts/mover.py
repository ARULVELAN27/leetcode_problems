import json
import os
import shutil


class Mover:

    def __init__(self):

        with open("../logs/move_plan.json", "r") as f:
            self.move_plan = json.load(f)["moves"]

        self.success = 0
        self.failed = 0
        self.skipped = 0

    def move_all(self):

        total = len(self.move_plan)

        print("=" * 70)
        print(f"Moving {total} problem folders")
        print("=" * 70)

        answer = input("\nProceed? (y/n): ")

        if answer.lower() != "y":
            print("\nOperation cancelled.")
            return

        for index, move in enumerate(self.move_plan, start=1):

            source = os.path.join("..", move["source"])

            destination = os.path.join("..", move["destination"])

            destination_parent = os.path.dirname(destination)

            print(f"[{index}/{total}] {move['source']}")

            if not os.path.exists(source):
                print("   ⏭ Source not found. Skipping.")
                self.skipped += 1
                continue

            os.makedirs(destination_parent, exist_ok=True)

            try:

                shutil.move(source, destination)

                print("   ✅ Moved")

                self.success += 1

            except Exception as e:

                print(f"   ❌ Failed : {e}")

                self.failed += 1

        print("\n" + "=" * 70)
        print("Migration Completed")
        print("=" * 70)
        print(f"Moved   : {self.success}")
        print(f"Skipped : {self.skipped}")
        print(f"Failed  : {self.failed}")
        print("=" * 70)

    def run(self):

        self.move_all()


if __name__ == "__main__":

    mover = Mover()

    mover.run()