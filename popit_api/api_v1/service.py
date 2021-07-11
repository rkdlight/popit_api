from base64 import b64encode
from hashlib import sha256
from hmac import HMAC
from urllib.parse import urlencode 

def is_request_valid(query: dict, secret: str) -> bool:
    """

    Check VK Apps signature

    :param dict query: Словарь с параметрами запуска
    :param str secret: Секретный ключ приложения ("Защищённый ключ")
    :returns: Результат проверки подписи
    :rtype: bool

    """
      
    if not query.get("sign"):
        return False
    
    vk_subset = sorted(
        filter(
            lambda key: key.startswith("vk_"), 
            query
        )
    )

    if not vk_subset:
        return False

    ordered = {k: query[k] for k in vk_subset}

    hash_code = b64encode(
        HMAC(
            secret.encode(), 
            urlencode(ordered, doseq=True).encode(), 
            sha256
        ).digest()
    ).decode("utf-8")

    if hash_code[-1] == "=":
        hash_code = hash_code[:-1]

    fixed_hash = hash_code.replace('+', '-').replace('/', '_')
    return query.get("sign") == fixed_hash

