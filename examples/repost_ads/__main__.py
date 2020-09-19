import os
import sys
import yaml

_CONFIG_FILE = 'config.yaml'
_ADS_FOLDER = './ads'
_USERNAME = ''
_PASSWORD = ''

from kijiji_bot import KijijiBot

if os.path.isfile(_CONFIG_FILE):
  print('Logging in with existing cookies...')

  with open(_CONFIG_FILE, 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    bot = KijijiBot(config['cookies'])
else:
  print('Logging in with account credentials...')

  bot = KijijiBot()
  config = {}
  config['is_using_alternate_ads'] = False
  config['cookies'] = bot.login(_USERNAME, _PASSWORD)

print('Successfully logged into Kijiji!')

print('Reposting ads...')
config['cookies'] = bot.repost_ads(_ADS_FOLDER, is_using_alternate_ads=config['is_using_alternate_ads'])
config['is_using_alternate_ads'] = not config['is_using_alternate_ads']
print('Successfully posted ads!')

print(f'Updating {_CONFIG_FILE}...')
with open(_CONFIG_FILE, 'w') as file:
  file.write(yaml.dump(config))
print(f'Successfully updated {_CONFIG_FILE}!')
