from setuptools import setup, find_packages

classifiers = {
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
}

setup(
    name="postgresplus",
    version="0.0.4",
    description="Psycopg2 wrapper.",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="",
    author="Connor McHarg",
    author_email="",
    license="MIT",
    classifiers=classifiers,
    keywords="databases",
    packages=find_packages(),
    install_requires=["psycopg2"]
)