from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'c_project_initializer',
    version = '0.0.3',
    author = 'Jian Zcar Esteban',
    author_email = 'pub.esteban.jianzcar@outlook.com',
    license = 'MIT License',
    description = 'C project initializer',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/JianZcar/c_project_initializer',
    py_modules = ['index', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.11',
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        c-initializer=index:cli
    '''
)