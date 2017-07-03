from setuptools import setup

setup(name='GoogleSheetClient',
      version='0.1',
      description='a simple wrapper of gspread for batch up/downloading of google sheet materials',
      url='https://github.com/yang0339/GoogleSheetClient',
      author='Fred Yang',
      author_email='fredyang0507@gmail.com',
      license='MIT',
      packages=['GoogleSheetClient'],
      zip_safe=False,
      include_package_data=True,
      install_requires = [
                'gspread',
                'pandas',
                'oauth2client',
              ],
)
