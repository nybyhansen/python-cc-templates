import os
import sys


def install_poetry() -> bool:
    try:
        os.system("poetry install")
        return True

    except Exception:
        return False


def clone_remote_repo() -> bool:
    remote_repo_url = "{{ cookiecutter.remote_repo_url }}"

    try:
        os.system("git init")
        if remote_repo_url:
            os.system(f"git remote add origin {remote_repo_url}")
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
    clone_repo_response = clone_remote_repo()
    if not clone_repo_response:
        sys.exit(1)

    install_poetry_response = install_poetry()
    if not install_poetry_response:
        sys.exit(1)

    connect_pre_commit_to_git_response = connect_pre_commit_to_git()
    if not connect_pre_commit_to_git_response:
        sys.exit(1)
