from pathlib import Path

from setuptools import setup

ROOT_PATH = Path(__file__).parent


GITHUB_USERNAME = "gabrielbazan"
GITHUB_PROJECT_NAME = "indexed_priority_queue"
GIT_REPOSITORY = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_PROJECT_NAME}"

PACKAGE_NAME = "indexed_priority_queue"
PYPI_PACKAGE_NAME = "indexed_priority_queue"
REQUIREMENTS_FILE = "requirements.txt"


README_FILENAME = "README.md"


DESCRIPTION = "A Python implementation of an Indexed Priority Queue (IPQ)."


def get_requirements():
    with open(REQUIREMENTS_FILE) as file:
        return file.readlines()


def get_long_description():
    return (ROOT_PATH / README_FILENAME).read_text(encoding="utf8")


setup(
    name=PYPI_PACKAGE_NAME,
    description=DESCRIPTION,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    # keywords="", TODO
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        # "Development Status :: 5 - Production/Stable", TODO
        "Operating System :: OS Independent",
    ],
    url=GIT_REPOSITORY,
    author="Gabriel Bazan",
    author_email="gbazan@outlook.com",
    license="MIT",
    packages=[PACKAGE_NAME],
    zip_safe=False,
    python_requires=">=3.6.2",
    install_requires=get_requirements(),
)
