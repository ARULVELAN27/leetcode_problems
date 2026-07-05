import os


def is_problem_folder(folder_name: str) -> bool:
    """
    Returns True only if the folder starts
    with a numeric LeetCode problem ID.
    """

    if folder_name.startswith("."):
        return False

    first = folder_name.split("-")[0]

    return first.isdigit()


def extract_problem_id(folder_name: str) -> str:
    """
    Example:

    0001-two-sum
            ↓
    1
    """

    first = folder_name.split("-")[0]

    problem_id = first.lstrip("0")

    if problem_id == "":
        return "0"

    return problem_id


def extract_slug(folder_name: str) -> str:
    """
    Example:

    0001-two-sum
            ↓
    two-sum
    """

    return folder_name.split("-", 1)[1]


def project_root():
    return ".."


def config_path(filename: str):

    return os.path.join(
        project_root(),
        "config",
        filename
    )


def logs_path(filename: str):

    return os.path.join(
        project_root(),
        "logs",
        filename
    )