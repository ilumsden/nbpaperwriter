from setuptools import setup

setup(name="nbpaperwriter",
      version="0.1.0a",
      description="A tool to write interactive scientific papers as Jupyter notebooks and convert them to LaTeX files",
      url="https://github.com/ilumsden/nbpaperwriter",
      author="Ian Lumsden",
      author_email="lumsden.ian@gmail.com",
      license="MIT",
      install_requires=[
          "pyinstaller",
      ],)
