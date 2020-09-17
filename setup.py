import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
  name='kijiji-bot',
  version='1.0.0',
  description='Repost Kijiji ads programmatically',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/george-lim/kijiji-bot',
  author='George Lim',
  author_email='lim.george@me.com',
  license='MIT',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  keywords='python bs4 pyyaml requests web automation kijiji bot',
  packages=setuptools.find_packages(include=['kijiji_bot']),
  install_requires=['bs4', 'pyyaml', 'requests'],
  python_requires='>=3.6'
)
