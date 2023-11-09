from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import urllib.parse

options=Options()
# options.add_experimental_option('detach', True) #브라우저 바로꺼짐 방지

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://twitter.com/i/flow/login')
driver.implicitly_wait(10) # 사이트가 뜰때까지 기다려주는 명령어

# 아이디 입력
driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe').send_keys('saessag64830')
time.sleep(1)

# 다음 버튼 클릭
divcls = 'css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu'
divcls = divcls.replace(' ', '.')
driver.find_element(By.CSS_SELECTOR, f'div.{divcls}').click()
time.sleep(2)

# 패스워드 입력
pwcls = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"
pwcls = pwcls.replace(' ', '.')
driver.find_element(By.CSS_SELECTOR, f'input.{pwcls}').send_keys('pass123word')
time.sleep(1)

# 로그인 버튼 클릭
logincls = 'css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr'
logincls = logincls.replace(' ', '.')
driver.find_element(By.CSS_SELECTOR, f'div.{logincls}').click()
time.sleep(2)


# 헤더 완성
cookie_text = ''
csrf = ''

for cookie in driver.get_cookies() :
    cookie_text += f"{cookie['name']}={cookie['value']};"
    if cookie['name'] == 'ct0' :
        csrf = cookie['value']

headers = {
  'Accept':'*/*',
  # 'Accept-Encoding':'gzip, deflate, br',
  'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
  'Authorization':  'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
  'Content-Type':  'application/json',
  'Cookie':  cookie_text,
  'Referer':  'https://twitter.com/search?q=%EC%A7%80%EB%93%9C%EB%9E%98%EA%B3%A4&src=typed_query&f=live',
  'Sec-Ch-Ua':  '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'Sec-Ch-Ua-Mobile':  '?0',
  'Sec-Ch-Ua-Platform':  '"Windows"',
  'Sec-Fetch-Dest':  'empty',
  'Sec-Fetch-Mode':  'cors',
  'Sec-Fetch-Site':  'same-origin',
  'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
  'X-Client-Transaction-Id':  'Pg3fjCddmFiiyNdafUCCvw7bgsDn6EA/sRbXHRNqVxOm4HfOZSjQu0jguLlKk9dOvnpcxD7hVmGi4fKpvAhCfhCsYQ30Pw',
  'X-Client-Uuid':  '01eb23d8-1521-4600-8a30-de0f7813e644',
  'X-Csrf-Token': csrf,
  'X-Twitter-Active-User':  'yes',
  'X-Twitter-Auth-Type':  'OAuth2Session',
  'X-Twitter-Client-Language':'ko'
  }
time.sleep(5)

print(headers)

query = '지드래곤'

variables = '{"rawQuery":"' + query + '","count":20,"cursor":"DAADDAABCgABF-eBJjmawXEKAAIX53DLhVbggwAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUX54IiDMAnEAoABhfngiIMv9jwAAA","querySource":"typed_query","product":"Latest"}'
features = '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_home_pinned_timelines_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}'

params = {'variables' : urllib.parse.quote(variables),
          'features' : urllib.parse.quote(features)}


while True :
  url = 'https://twitter.com/i/api/graphql/lZ0GCEojmtQfiUQa5oJSEw/SearchTimeline'
  res = requests.get(url, headers=headers)

  for tweet in res.json()['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]['entries'] :
    try :
      print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'].replace('\n', ''))
    except :
      pass

  cursor = res.json()['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']

