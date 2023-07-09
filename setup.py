from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="geff",
    version="1.0.0",
    description="An api wrapper for Tenor and Giphy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="sleepbot-zapp",
    author_email="mullickneeladri@gmail.com",
    packages=find_packages(),
    url="https://github.com/sleepbot-zapp/GEFF",
    project_urls={
        "Issue tracker": "https://github.com/sleepbot-zapp/GEFF/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["httpx"],
    python_requires=">=3.10",
)