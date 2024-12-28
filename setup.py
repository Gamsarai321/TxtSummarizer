import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
    
    
__version__ ="0.0.0"

REPO_NAME = "TxtSummarizer"
AUTHOR_USER_NAME = "Gamsarai321"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "garaib97@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP apps.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"", "src"},
    packages=setuptools.find_packages(where="src")
    
) 