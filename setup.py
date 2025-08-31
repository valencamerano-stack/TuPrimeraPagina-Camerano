from setuptools import setup, find_packages

setup(
    name="TuPrimeraPaginaCamerano",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "django>=4.0",
    ],
    entry_points={
        "console_scripts": [
            "manage=manage:main",
        ],
    },
)
