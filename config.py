import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5180625091:AAEzv9cKk0y305paqqKQ_MlTHA8m8CfhgSw')
API_ID =  os.environ.get('api_id','9520699')
API_HASH = os.environ.get('api_hash','353e5b6ef2c174d0e8d7fb62e277840d')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','quejestoniuyol').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KIDDKDYJJKJJGDYDJKGJGJYGIHIERKDGLGDELI'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
