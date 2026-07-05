from dataclasses import dataclass


@dataclass
class Problem:

    id: int

    title: str

    slug: str

    difficulty: str

    primary_topic: str

    leetcode_tags: list

    folder_name: str

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "difficulty": self.difficulty,
            "primary_topic": self.primary_topic,
            "leetcode_tags": self.leetcode_tags,
            "folder_name": self.folder_name
        }