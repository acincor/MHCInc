import setuptools

with open("README.md", "r",encoding = "UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MHCInc",
    version="0.3.0",
    author="Mhc-inc",
    author_email="Wf6350177@163.com",
    description="改进：seven ate nine. PHYSICAL_CONDITION_APPLET解决了os导入的问题",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/MHCInc/",
    project_urls={
        "Bug Tracker": "https://github.com/Mhc-inc/MHCInc/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['lxml',
                  'requests','bs4','pygame'],
    package_dir={"": "MHCInc"},
    packages=setuptools.find_packages(where="MHCInc"),
    python_requires=">=3.9",
)
