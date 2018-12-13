from setuptools import setup


setup(name='calculator',
      version='0.0.1',
      packages=['calculator'],
      entry_points={
        'console_scripts': [
            'calculator = calculator.__main__:main'
        ]
      })
