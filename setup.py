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
        "pandas>=2.0.0",
        "numpy>=1.24.0",
    ],
    python_requires="==3.10.*",
    author="Ogokmen",
    description="A Streamlit-based AI assistant for travel, events, news, and sports information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.10",
    ],
) 