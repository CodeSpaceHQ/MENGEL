from setuptools import find_packages, setup

# Further documentation on this topic
# https://packaging.python.org/distributing/
setup(name="MENGEL",
      version="0.1",
      description="Automated machine learning framework in Python.",
      author="Code_Space",
      author_email="alexander.clines@ttu.edu",
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Data Scientists',
          'Topic :: Data Science :: Analysis Tools',
          'Programming Language :: Python :: 2.7'
      ]
)
