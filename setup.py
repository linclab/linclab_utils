import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setuptools.setup(
    name="linclab-utils",
    version="0.0.1",
    author="LincLab",
    author_email="blake.richards@mcgill.ca",
    description="Package with basic LiNCLab coding utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linclab/linclab-utils",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
