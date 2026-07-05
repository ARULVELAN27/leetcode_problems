import requests
import json


URL = "https://leetcode.com/api/problems/all/"


def main():

    print("Fetching LeetCode problem index...")

    response = requests.get(URL)

    if response.status_code != 200:
        print("Failed to fetch data")
        return

    data = response.json()

    problems = {}

    for item in data["stat_status_pairs"]:

        stat = item["stat"]

        problem_id = str(stat["frontend_question_id"])

        problems[problem_id] = {
            "title": stat["question__title"],
            "slug": stat["question__title_slug"]
        }

    with open("../config/problem_index.json", "w") as f:
        json.dump(problems, f, indent=4)

    print(f"\nSaved {len(problems)} problems")
    print("File created: config/problem_index.json")


if __name__ == "__main__":
    main()

URL = "https://leetcode.com/api/problems/all/"


def main():
    print("Fetching LeetCode problem index...")

    response = requests.get(URL)

    if response.status_code != 200:
        print("Failed to fetch data")
        return

    data = response.json()

    print(f"Total Problems Found: {len(data['stat_status_pairs'])}")


if __name__ == "__main__":
    main()