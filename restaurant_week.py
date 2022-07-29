from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from nltk.metrics.distance import jaccard_distance

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# restaurant_week_names = []
# for page_num in range(1, 29):
#     driver.get(f"https://www.nycgo.com/restaurant-week?page={page_num}")
#     cards = driver.find_elements(By.CLASS_NAME, 'card-title')
#     restaurant_week_names += [c.accessible_name for c in cards[4:-1]]
#     pass

# with open('restaurant_week.txt', 'w') as f:
#     for name in restaurant_week_names:
#         f.write(name + '\n')


# michelin_names = []
# for page_num in range(1, 26):
#     print(f'on page {page_num}')
#     driver.get(f'https://guide.michelin.com/us/en/new-york-state/new-york/restaurants/page/{page_num}')
#     name_cards = driver.find_elements(By.CLASS_NAME, 'card__menu-content--title')
#     rating_cards = driver.find_elements(By.CLASS_NAME, 'card__menu-content--rating')

#     error = True
#     while error:
#         try:
#             while name_cards[0].text == '':
#                 name_cards = driver.find_elements(By.CLASS_NAME, 'card__menu-content--title')
#                 rating_cards = driver.find_elements(By.CLASS_NAME, 'card__menu-content--rating')

#             error = False
#         except Exception:
#             name_cards = driver.find_elements(By.CLASS_NAME, 'card__menu-content--title')
#             rating_cards = driver.find_elements(By.CLASS_NAME, 'card__menu-content--rating')
#             error = True
            


#     for name_card, rating_card in zip(name_cards, rating_cards):
#         restaurant_name = name_card.text
#         restaurant_rating = rating_card.text
#         rating = ''
#         if '=' in restaurant_rating:
#             rating += ':P'
#         rating += ' ' + '*' * restaurant_rating.count('m')
#         michelin_names.append(f'{restaurant_name}\t{rating}')

# with open('michelin_nyc.txt', 'w') as f:
#     for name in michelin_names:
#         f.write(name + '\n')


restaurant_names = None
michelin_names = None

with open('michelin_nyc.txt', 'r') as f:
    michelin_names = f.readlines()

with open('restaurant_week.txt', 'r') as f:
    restaurant_names = f.readlines()

s = set()
for m_name in michelin_names:
    m_name = m_name[:-1]
    m_name, m_rating = m_name.split('\t')
    m_set = set(ch for ch in m_name)
    for r_name in restaurant_names:
        r_name = r_name[:-1]
        r_set = set(ch for ch in r_name)
        if jaccard_distance(m_set, r_set) < .2:
            print(f'{m_name} : {r_name}')
            s.add(f'{m_name} {m_rating}')
            # f.write(f'{r_name} : {m_name}\n')

print(len(s))

# with open('michelin_restaurant_week.txt', 'w') as f:
#     for name in s:
#         f.write(name + '\n')
