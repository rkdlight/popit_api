# API Methods

Для аутентификации используется url страницы на которой запускается скрипт включая все GET параметры. Данный url необходимо передавать со всеми запросами в заголовке *HTTP-Referer*.

## POST api/v1/login/

Используется при заходе в приложение уже зарегистрированного пользователя

    {
        "vk_id":int # required
    }

*vk_id* - id пользователя ВК

**Response**

    {
        "vk_id": 1234,
        "friends": [
            {
                "vk_id": 1245,
                "full_name": "Jiji Jiji Jiji",
                "score": 0.0
            },
            {
                "vk_id": 123456,
                "full_name": "Jiji  friend",
                "score": 0.0
            }
        ],
        "referals_count": 2,
        "full_name": "Jiji Jiji",
        "coins_available": 169.793,
        "score": 169.793,
        "coins_by_sec": 0.001,
        "coins_by_click": 0.001,
        "buyed_updates": "[]",
        "buyed_toys": "[]",
        "active_toy": 1,
        "friend": []
    }
    
## POST api/v1/user/

Используется для регистрации нового пользователя
    
    {
        "vk_id": int #required
        "full_name": str #required
        "date_of_birth": "YYYY-MM-DD" #optional 
        "refer": int #optional vk_id of refer user
    }
    
**Response**

    {
        "vk_id": 43215,
        "full_name": "john smith",
        "date_of_birth": "2001-07-26",
        "coins_available": 1.0,
        "coins_by_sec": 0.001,
        "coins_by_click": 0.001,
        "active_toy": 1,
        "refer": 1234,
        "friend": []
    }
 
## GET api/v1/user/<vk_id>/
 
Используется для получения данных пользователя

**Response**

    {
        "vk_id": 1234,
        "friends": [
            {
                "vk_id": 1245,
                "full_name": "Jiji Jiji Jiji",
                "score": 0.0
            },
            {
                "vk_id": 123456,
                "full_name": "Jiji  friend",
                "score": 0.0
            }
        ],
        "referals_count": 2,
        "full_name": "Jiji Jiji",
        "coins_available": 169.793,
        "score": 169.793,
        "coins_by_sec": 0.001,
        "coins_by_click": 0.001,
        "buyed_updates": "[]",
        "buyed_toys": "[]",
        "active_toy": 1,
        "friend": []
    }    

## PUT api/v1/user/<vk_id>/update/

Обновление данных пользователя. Все данные являются необязательными.

    {
        "coins_available": float,
        "score": float,
        "coins_by_sec": float,
        "coins_by_click": float,
        "buyed_updates": array,#[
                               #     {"id": 1, "count":3, "current_price": 1.5}, # id of update
                               #     {"id": 4, "count":3, "current_price": 11.5},
                               #     {"id": 5, "count":6, "current_price": 110.5},
                               #]
        "buyed_toys": array,
        "active_toy": int, # id of active toy
        "friend": []
    }
    
**Response**

    {
        "coins_available": 3.0,
        "score": 0.0,
        "coins_by_sec": 0.001,
        "coins_by_click": 0.001,
        "buyed_updates": [],
        "buyed_toys": [],
        "active_toy": 1,
        "friend": []
    }
    
## GET api/v1/updates/

Получение списка улучшений

**Response**

    {
        "name" = str
        "description" = str
        "base_price" = float
        "image" = str #url of image
        "coins_by_sec" = float
    }
    
## GET api/v1/toys/

Получение списка игрушек

**Response**

    {
        "name" = str
        "flipings_before_ad" = int
        "base_price" = float
        "image" = str #url of image
        "coins_by_click" = float
        "referals_need" = int
    }

