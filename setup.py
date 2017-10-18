from setuptools import setup

setup(name='watarus_funniest',
      version='0.2',
      description='The funniest joke in the world',
      url='https://github.com/watarus-nt/watarus_funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['watarus_funniest'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)