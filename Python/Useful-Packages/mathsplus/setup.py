from setuptools import setup, find_packages

classifiers = {
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
}

setup(
    name="mathsplus",
    version="0.1.1",
    description="Extra maths functions.",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="",
    author="Connor McHarg, Thomas Copland",
    author_email="",
    license="MIT",
    classifiers=classifiers,
    keywords="maths",
    packages=find_packages(),
    install_requires=[""]
)