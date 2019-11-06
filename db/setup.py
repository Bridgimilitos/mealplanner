from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'pyodbc',
    'sqlalchemy'
]

setup(
    name='mealplanner_db',
    version='0.0',
    description='db interface to sql server',
    author='James Bridges',
    author_email='jbridges@f2s.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)