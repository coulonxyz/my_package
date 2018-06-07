from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='my_funniest',
      version='0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      license='coulon.xyz',
      packages=['my_funniest'],
      test_suite='nose.collector',
      entry_points={
          'console_scripts': ['funniest-joke=funniest.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)