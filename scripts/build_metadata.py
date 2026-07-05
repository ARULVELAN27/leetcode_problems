import json
import os

from leetcode_api import LeetCodeAPI

ROOT = ".."


def load_problem_index():
    with open("../config/problem_index.json", "r") as f:
        return json.load(f)


def load_primary_topics():
    with open("../config/primary_topics.json", "r") as f:
        return json.load(f)


def main():

    api = LeetCodeAPI()

    problem_index = load_problem_index()

    topic_map = load_primary_topics()

    metadata = {}

    folders = sorted(os.listdir(ROOT))

    for folder in folders:

        path = os.path.join(ROOT, folder)

        if not os.path.isdir(path):
            continue

        if folder.startswith("."):
            continue

        if folder in ["scripts", "config", "logs"]:
            continue

        # Extract problem number
        problem_id = folder.split("-")[0].lstrip("0")

        if problem_id == "":
            problem_id = "0"

        if problem_id not in problem_index:
            print(f"Skipping {folder}")
            continue

        slug = problem_index[problem_id]["slug"]

        print(f"Fetching {problem_id} -> {slug}")

        data = api.get_problem(slug)

        question = data["data"]["question"]

        if question is None:
            print(f"Failed : {slug}")
            continue

        tags = [x["name"] for x in question["topicTags"]]

        primary = "Uncategorized"

        if tags:
            primary = topic_map.get(tags[0], tags[0])

        metadata[problem_id] = {
            "title": question["title"],
            "difficulty": question["difficulty"],
            "primary_topic": primary,
            "all_topics": tags,
            "slug": slug
        }

    with open("../config/metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print("\nMetadata Created Successfully")


if __name__ == "__main__":
    main()