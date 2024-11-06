import requests as rq
import logging

# Настройка логов
logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('success')
success_handler = logging.FileHandler('success_responses.log')
success_logger.addHandler(success_handler)

bad_logger = logging.getLogger('bad')
bad_handler = logging.FileHandler('bad_responses.log')
bad_logger.addHandler(bad_handler)

blocked_logger = logging.getLogger('blocked')
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_logger.addHandler(blocked_handler)

# Список сайтов для проверки
sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for url in sites:
    try:
        response = rq.get(url, timeout=5)  # Устанавливаем таймаут для ускорения обработки
        if response.status_code == 200:
            success_logger.info(f"Success: {url}")
        else:
            bad_logger.warning(f"Bad response ({response.status_code}): {url}")
    except rq.RequestException as e:
        blocked_logger.error(f"Blocked: {url} - {str(e)}")
