import base64
import os
import pickle
import time
import yaml
import kijiji_bot.kijiji_api as api

class KijijiBot(api.KijijiApi):
  def __init__(self, cookies_str=None):
    super().__init__()

    if cookies_str is not None:
      self._set_cookies(cookies_str)

  def _get_cookies(self):
    cookies_pickled = pickle.dumps(self.session.cookies)
    cookies_base64 = base64.b64encode(cookies_pickled)
    cookies_str = str(cookies_base64, 'utf-8')
    return cookies_str

  def _set_cookies(self, cookies_str):
    cookies_base64 = bytes(cookies_str, 'utf-8')
    cookies_pickled = base64.b64decode(cookies_base64)
    cookies = pickle.loads(cookies_pickled)
    self.session.cookies.update(cookies)

    if not self.is_logged_in():
      raise api.KijijiApiException('Detected invalid or expired cookies')

  def login(self, username, password):
    super().login(username, password)
    return self._get_cookies()

  def repost_ads(self, ads_path, is_using_alternate_ads=False):
    [self.delete_ad(ad['id']) for ad in self.get_all_ads()]
    print('Deleted all active ads.')

    for dirname, _, filenames in os.walk(ads_path):
      for filename in filenames:
        if filename.endswith('.yml') or filename.endswith('.yaml'):
          ad_file = os.path.join(dirname, filename)

          with open(ad_file, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            image_files = [open(os.path.join(os.path.dirname(ad_file), picture), 'rb').read() for picture in data['image_paths']]
            del data['image_paths']

            if is_using_alternate_ads:
              data['postAdForm.title'] = data.get('postAdForm.alternateTitle', data['postAdForm.title']).strip()
              data['postAdForm.city'] = data.get('postAdForm.alternateCity', data['postAdForm.city'])
              data['postAdForm.addressCity'] = data.get('postAdForm.alternateAddressCity', data['postAdForm.addressCity'])
              data['postAdForm.description'] = data.get('postAdForm.alternateDescription', data['postAdForm.description'])
            else:
              data['postAdForm.title'] = data['postAdForm.title'].strip()

          try:
            print(f'Found ad: {data["postAdForm.title"]}')
            self.post_ad_using_data(data, image_files)
            time.sleep(30)

            all_ads = self.get_all_ads()
            is_active_ad = [ad['title'] for ad in all_ads if ad['title'] == data['postAdForm.title']]

            if not is_active_ad:
              raise api.KijijiApiException('Duplicate ad removed by Kijiji')

            print(f'Posted ad: {data["postAdForm.title"]}')
          except Exception as exception:
            print(exception)

    return self._get_cookies()
