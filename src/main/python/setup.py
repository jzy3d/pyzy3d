from setuptools import setup

setup(name='pyzy3d',
      version='1.0.1.rc2',
      description='3d charts for Python',
      url='https://github.com/jzy3d/pyzy3d',
      author='Martin Pernollet',
      author_email='martin@jzy3d.org',
      license='MIT',
      packages=['pyzy3d'],
      install_requires=[
          'py4j','time','random'
      ],
      data_files=[('target/', ['pyzy3d/bin/pyzy3d-1.0.1-SNAPSHOT.jar'])],
      zip_safe=False)
