from setuptools import setup, find_packages
import os

setup(
    name='tts-watson',
    version='1.0.0',
    packages=['tts_watson'],
    url='https://github.com/HomeHabbit/tts-watson',
    license='MIT',
    author='Arthur Halet',
    author_email='arthurh.halet@gmail.com',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    description='Text to speech using watson',
    keywords='text-to-speech watson',
    classifiers=['Topic :: Multimedia :: Sound/Audio :: Speech',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: MIT License'],
    platforms='ALL',
    install_requires=[
        'Flask',
        'requests',
        'pyaudio>=0.2.9',
        'pyyaml>=3.08',
        'anyconfig',
        'bunch>=1.0.1'
    ],
    entry_points={
        'console_scripts': [
            'tts-watson=tts_watson.__main__:main',
        ],
    },
)
