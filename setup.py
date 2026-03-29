from setuptools import setup, find_packages

setup(
    name='pid_aimbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pid_aimbot = pid_aimbot.__init__:main',
        ],
    },
)
