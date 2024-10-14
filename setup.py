import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Prkaritt"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL= "prakrituprety0@gmail.com"
__version__ = "0.0.0"


setuptools.setup(
    name =SRC_REPO,
    version = __version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for NLP app",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"" : "src"},
    packages = setuptools.find_packages(where="src")
                                                
)
