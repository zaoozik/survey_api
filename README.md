## DEPLOY REFERENCE
`docker-compose up -d` - запустит приложение на порту 8000

В Бд создан Админ, логин admin, пароль 1234

## ADMIN API REFERENCE
### 1. Описание объектов
#### Объект Poll (Опрос)
Служит для хранения опросов

Свойства объекта:
+ `id <Int>` - уникальный идентификатор опроса
+ `name <String>` - название опроса
+ `datetime_start <Datetime>` - время начала опроса, в формате ISO 8601
+ `datetime_start <Datetime>` - время начала опроса, в формате ISO 8601
+ `info <String>` - описание опроса

#### Объект Question (Вопрос)
Служит для хранения вопросов

Свойства объекта:
+ `id <Int>` - уникальный идентификатор вопроса
+ `poll <Int>` - идентификатор опроса, в котором участвует вопрос 
+ `type <String>` - тип вопроса, принимает следующие значения:
    + `text` - ответ на вопрос ожидается текстом в свободной форме
    + `select_one` - выбор одного из вариантов ответа
    + `select_many` - выбор нескольких вариантов ответа
+ `text <String>` - содержание вопроса

#### Объект Choice (Вариант ответа)
Служит для хранения вариантов ответа вопросов

Свойства объекта:
+ `id <Int>` - уникальный идентификатор варианта ответа
+ `question <Int>` - идентификатор вопроса, для которого создан вариант ответа
+ `text <String>` - содержание варианта ответа

### Авторизация
Для авторизации запросов используется Http Basic Auth

### Запросы API
Api реализовано по стандарту REST

Адрес API - `/api/admin`

Поддерживается получение (GET), создание (POST), обновление (PUT) и удаление (DELETE) перечисленных объектов

Опросы:

`GET /api/admin/polls` 

Вопросы: 

`GET /api/admin/questions`

Варианты ответов:

`GET /api/admin/choices`

Операции добавления, обновления, создания полностью соответствуют стандарту REST

## USER API REFERENCE
### 1. Описание объектов
#### Объект Poll (Опрос)
Служит для получения опросов

Свойства объекта:
+ `id <Int>` - уникальный идентификатор опроса
+ `name <String>` - название опроса
+ `datetime_start <Datetime>` - время начала опроса, в формате ISO 8601
+ `datetime_start <Datetime>` - время начала опроса, в формате ISO 8601
+ `info <String>` - описание опроса

#### Объект Question (Вопрос)
Служит для получения вопросов

Свойства объекта:
+ `id <Int>` - уникальный идентификатор вопроса
+ `text <String>` - содержание вопроса
+ `type <String>` - тип вопроса, принимает следующие значения:
    + `text` - ответ на вопрос ожидается текстом в свободной форме
    + `select_one` - выбор одного из вариантов ответа
    + `select_many` - выбор нескольких вариантов ответа
+ `choices <Object>` - содержит варианты ответа на вопрос. Структура объекта:
    + `id <Int>` - идентификатор варианта ответа
    + `text <String>` - содержание варианта ответа
    
#### Массив Answers (Ответы)
Содержит список пройденных опросов пользователя и детализацию по ответам

Массив содержит объекты следующей структуры:

+ `id <Int>` - уникальный идентификатор опроса
+ `name <String>` - название опроса
+ `questions <Array>` - список вопросов. Структура элемента массива:
    + `id <Int>` - идентификатор вопроса
    + `text <String>` - содержание вопроса
    + `answer <String>` - ответ пользователя
    
### Авторизация
Авторизация запросов отсуствует

### Запросы API
Адрес API - `/api/user`

#### Получение списка опросов
`GET /api/user/polls`

#### Получение списка вопросов опроса
`GET /api/user/polls/<poll_id>/questions`  

где `poll_id` - идентификатор опроса

#### Размещение ответа на вопрос
`POST /api/user/polls/<poll_id>/questions/<question_id>/`  

где `poll_id` - идентификатор опроса

`question_id` - идентификатор вопроса

В качестве ответа передается объект следующего вида:
```json
{
  "user_id": <Int>,
  "text": <String>,
  "choice": <Int>
}
```

`user_id` - идентификатор пользователя. По нему можно будет получить пройденные опросы

`text` - ответ на вопрос, если у вопроса `type == 'text'`

`choice` - идентификатор варианта ответа, если `type != 'text'`

#### Получение информации о пройденных опросах
`GET /api/user/polls/answers/<user_id>`  

где `user_id` - идентификатор пользователя, использовавшийся при ответах на вопросы
