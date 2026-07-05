import json
import os
import sys

from leetcode_api import LeetCodeAPI
from priority_engine import PriorityEngine

sys.path.append("..")

from models.problem import Problem
from helpers import (
    is_problem_folder,
    extract_problem_id,
    extract_slug,
)

ROOT = ".."


def load_problem_index():
    with open("../config/problem_index.json", "r") as f:
        return json.load(f)


def load_primary_topics():
    with open("../config/primary_topics.json", "r") as f:
        return json.load(f)


def main():

    print("=" * 70)
    print("Building Metadata Database")
    print("=" * 70)

    api = LeetCodeAPI()
    priority_engine = PriorityEngine()

    problem_index = load_problem_index()
    topic_map = load_primary_topics()

    metadata = {}

    total = 0
    success = 0
    failed = 0

    folders = sorted(os.listdir(ROOT))

    for folder in folders:

        path = os.path.join(ROOT, folder)

        # Skip anything that is not a problem folder
        if not os.path.isdir(path):
            continue

        if not is_problem_folder(folder):
            continue

        total += 1

        problem_id = extract_problem_id(folder)

        # --------------------------------------------------
        # Get slug
        # --------------------------------------------------

        if problem_id in problem_index:

            slug = problem_index[problem_id]["slug"]

        else:

            slug = extract_slug(folder)

            print(
                f"⚠ Problem {problem_id} not found in problem_index.json"
            )
            print(f"   Using folder slug : {slug}")

        print(f"Fetching {problem_id} -> {slug}")

        # --------------------------------------------------
        # Fetch metadata
        # --------------------------------------------------

        try:

            data = api.get_problem(slug)

        except Exception as e:

            print(f"❌ API Error : {e}")

            failed += 1

            continue

        if (
            data is None
            or "data" not in data
            or data["data"] is None
            or data["data"]["question"] is None
        ):

            print(f"❌ Failed : {slug}")

            failed += 1

            continue

        question = data["data"]["question"]

        tags = [
            tag["name"]
            for tag in question["topicTags"]
        ]

        primary_tag = priority_engine.get_primary_topic(tags)

        primary_topic = topic_map.get(
            primary_tag,
            primary_tag
        )

        problem = Problem(

            id=int(problem_id),

            title=question["title"],

            slug=slug,

            difficulty=question["difficulty"],

            primary_topic=primary_topic,

            leetcode_tags=tags,

            folder_name=f"{int(problem_id):04d} - {question['title']}"

        )

        metadata[problem_id] = problem.to_dict()

        success += 1

    # --------------------------------------------------
    # Save metadata
    # --------------------------------------------------

    with open("../config/metadata.json", "w") as f:

        json.dump(
            metadata,
            f,
            indent=4,
            ensure_ascii=False
        )

    print()

    print("=" * 70)
    print("Metadata Build Complete")
    print("=" * 70)
    print(f"Problem Folders Found : {total}")
    print(f"Success               : {success}")
    print(f"Failed                : {failed}")
    print("=" * 70)


if __name__ == "__main__":
    main()