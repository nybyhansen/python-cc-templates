import os
import sys

from git import Repo


def install_poetry() -> bool:
    try:
        os.system("poetry install")
        return True

    except Exception:
        return False


def clone_remote_repo() -> bool:
    remote_repo_url = "{{ cookiecutter.remote_repo_url }}"
    if not remote_repo_url:
        return False
    try:
        Repo.clone_from(
            url=remote_repo_url,
            to_path="./",
        )
        return True

    except Exception:
        return False


def connect_pre_commit_to_git() -> bool:
    try:
        os.system("poetry run pre-commit install")
        return True
    except Exception:
        return False


if __name__ == "__main__":
    # install_poetry_response = install_poetry()
    # if not install_poetry_response:
    #    sys.exit(1)

    clone_repo_response = clone_remote_repo()
    if not clone_repo_response:
        sys.exit(1)

    # connect_pre_commit_to_git_response = connect_pre_commit_to_git()
    # if not connect_pre_commit_to_git_response:
    #    sys.exit(1)
