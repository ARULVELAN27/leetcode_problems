"""
LeetCode Organizer
Author: Arulvelan

Entry point of the application.
"""

from organizer import Organizer


def main():
    print("=" * 50)
    print("🚀 LeetCode Organizer Started")
    print("=" * 50)

    organizer = Organizer()
    organizer.run()

    print("=" * 50)
    print("✅ Organizer Finished")
    print("=" * 50)


if __name__ == "__main__":
    main()