from setuptools import setup, find_packages

setup(
    name="FoodieBot",
    version="1.0.0",
    description="FoodieBot - Intelligent Database-Driven Conversational Fast Food Recommendation AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Anussha001/Foodie_Bot",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        "sqlite3",
        "requests",
        "groq",
        "streamlit",
        "dataclasses; python_version<'3.7'",
    ],
    entry_points={
        "console_scripts": [
            "foodiebot-cli=conversational_ai:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
