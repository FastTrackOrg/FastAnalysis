from setuptools import setup

setup(
    name="fastanalysis",
    version="0.0.1",
    author="Benjamin Gallois",
    author_email="benjamin.gallois@fasttrack.sh",
    description="A python library to open the tracking data from FastTrack the tracking software",
    url="https://github.com/FastTrackOrg/FastAnalysis",
    packages=['fastanalysis'],
    install_requires=['pandas', 'numpy', 'matplotlib', 'xlrd', 'openpyxl', 'seaborn'],
    license='MIT',
    python_requires='>=3.6',
    zip_safe=False
)
