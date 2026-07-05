import re


class Metadata:

    @staticmethod
    def extract(folder_name):
        """
        Extract problem number and title from folder name.

        Example:
        0001-two-sum
        ↓
        {
            "id": 1,
            "title": "Two Sum"
        }
        """

        pattern = r"(\d+)-(.*)"
        match = re.match(pattern, folder_name)

        if not match:
            return None

        problem_id = int(match.group(1))

        title = match.group(2)
        title = title.replace("-", " ").title()

        return {
            "id": problem_id,
            "title": title
        }