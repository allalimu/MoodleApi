from setuptools import setup,find_packages

setup(
    name='My Script',
    version='0.1.0',
    py_modules=['mainscript'],
    packages=find_packages(),
    install_requires=[
        'click','python_dotenv','requests'
    ],
    entry_points={
        'console_scripts': [
            'mainscript = mainscript:main'
        ],
    },
)