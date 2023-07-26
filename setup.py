import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gauth_python',
    version='0.1.2',
    description='Python sdk from Gauth.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/GSM-MSG/GAuth-SDK-Python",
    packages=setuptools.find_packages(),
    classifiers = [        
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.7',
    author_email="dev.yohan05@gmail.com",
    author='Noh Gaseong',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner','requests'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)

