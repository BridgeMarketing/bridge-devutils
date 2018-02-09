from setuptools import setup, find_packages

setup(name='bridge-devutils',
      version='0.1',
      description='Bridge development utilities',
      url='https://github.com/BridgeMarketing/bridge-devutils',
      author='Bridge',
      author_email='info@bridgecorp.com',
      license='GPL',
      # packages=['workfront', 'workfront.wf', 'workfront.wf.objects'],
      long_description=open('README.md').read(),
      packages=find_packages(exclude=('tests')),
      install_requires=[
             'celery==4.1.0',
             'Flask==0.12.2'],
      tests_require=['mock', 'nose', 'requests-mock'],
      zip_safe=False)
