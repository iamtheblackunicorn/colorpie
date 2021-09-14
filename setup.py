import pathlib
from setuptools import setup
from setuptools import find_packages
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
setup(
    name='colorpie',
    version='1.0.0',
    description='Make the snake discover the rainbow',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iamtheblackunicorn/colorpie',
    author='The Black Unicorn',
    author_email='drkuncrn@protonmail.ch',
    package_dir={'': '.'},
    packages=find_packages(),
    python_requires='>=3.6, <4',
    project_urls={
        'Bug Reports': 'https://github.com/iamtheblackunicorn/colorpie/issues',
        'Source': 'https://github.com/iamtheblackunicorn/colorpie/'
    },
)
