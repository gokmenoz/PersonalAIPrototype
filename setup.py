from setuptools import setup, find_packages

setup(
    name="personal-ai-assistant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.32.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "boto3>=1.34.0",
        "botocore>=1.34.0",
    ],
) 