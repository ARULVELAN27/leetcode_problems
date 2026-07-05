import requests


class LeetCodeAPI:

    URL = "https://leetcode.com/graphql"

    def __init__(self):
        pass

    def get_problem(self, slug):
        """
        Fetch metadata for a LeetCode problem.
        """

        query = """
        query getQuestion($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            title
            difficulty
            topicTags {
              name
            }
          }
        }
        """

        variables = {
            "titleSlug": slug
        }

        response = requests.post(
            self.URL,
            json={
                "query": query,
                "variables": variables
            }
        )

        return response.json()
if __name__ == "__main__":

    api = LeetCodeAPI()

    data = api.get_problem("two-sum")

    print(data)