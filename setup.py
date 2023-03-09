from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='0.0.1',
      autor='Makeiev Yehor',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts':['clean = clean_folder.clean_folder.clean:main']}
      )

