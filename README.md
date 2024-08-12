# Tezer Platform | TezerPaymentSystem

### Financial opportunities available to everyone.

![TezerPlatformLogo](https://i.postimg.cc/L8d88Yx3/photo-2024-07-06-10-07-44.jpg)

## Page navigation :triangular_flag_on_post:

+ [Website Tezer Platform](https://tezerplatform.github.io/Tezer/ "Information site") :ballot_box_with_check:

___

+ [Russian language](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#russian-language)
  + [О прокте](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#о-прокте-heavy_check_mark)
  + [Выгода сторон](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#выгода-сторон-heavy_dollar_sign)
  + [Оплата в 3 действия](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#оплата-в-3-действия-three)
  + [Подключение системы оплаты в проект. Код](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#подключение-системы-оплаты-в-проект-код)
  + [Безопастность](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#безопастность-beginner)
  + [Важно](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#важно-warning)
  + [О контрактах](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#о-контрактах-bank)
  + [Контакты](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#контакты-speech_balloon)
+ [English language](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#english-language)

# Russian language
## О прокте :heavy_check_mark:

Наш проект представлен, на данный момент, на языке программирования Python. Работаем над тем, чтобы в будущем можно  будет использовать не только код на python, но и на других популярных языках программирования. 

*Если у Вас есть начинающий проект, вы можете подключить быструю и безопасную систему оплаты, с использованием нашей бесплатной платформы Tezer и о вашем проекте узнают заинтересованные люди. Наша задача - предоставить Вам возможность проявить успех начинающего или уже работающего проекта, с выходом на стабильный доход.*

Доход Вы получаете от того, что в вашем проекте оплачивают продукт, плюс Вы можете зарабатывать не зависимо от своего проекта на нашей платформе: [создать контракт](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#о-контрактах-bank) для оплаты и брать комиссию  за переводы или наоборот больше привлекать людей и условием будет - быть подписанным на Ваш канал. Возможностей и идей куча, нужно только реализовать.

> *[..о вашем проекте узнают заинтересованные люди..](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#Выгода-сторон)*

При подключении системы оплаты, мы рассказываем во всех социальных сетях о вашем проекте, и наша аудитория может заинтересоваться вашим проектом и купить продукт. *Если возникут вопросы при подключении системы оплаты, свяжитесь с [Менеджером проекта](https://t.me/majmanager).*

Оплата происходит в [3 действия](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#Оплата-в-3-действия):
+ Сначало пользователь создаёт ссылку для оплаты, где в ссылке нужно указать: 
  + Адрес получателя токенов (Продавец) 
  + Количество токенов 
  + Информационное поле (В нём можно указывать login пользователя, который получит продукт/программу за которую он оплачивал) 
  + И выбрать [контракт](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#О-контрактах) для передачи токенов TZR

+ Вторым этапом пользователь переходит по ссылке в Telegram бота, проверяет данные, оплачивает или отменяет. *Пример оплаты через контракт [TezerX](https://telegra.ph/Kontrakt-TezerX-06-28 "telegra.ph"):*

![PayContractTezerX](https://i.postimg.cc/fL4TkN22/stepanpoprosil-07-06-20-57-25.jpg "Пример оплаты через контракт TezerX")

+ Копируем `CodeCheck` и вставляем в поле в проекте для приёма чека и подтверждаем оплату. Если чек действителен и не повреждён, то пользователь получает продукт. 

## Выгода сторон :heavy_dollar_sign:

Каждая сторона становится популярнее. Как? При подключении каких-либо проектов в систему оплаты Tezer мы рекламируем Ваш проект в наших социальных сетях. Аудитория Tezer Platform узнаёт о Вашем проекте, а ваша аудитория проекта узнаёт о нашей системе оплаты.
По вопросам обращаться к [Менеджеру проекта](https://t.me/majmanager "Официальный менеджер проекта Tezer Platform")

## Оплата в 3 действия :three:

+ Создаётся ссылка для перехода в [Telegram бота](https://t.me/TezerPlatformBot)
  
+ Пользователь переходит по ней, оплачивает и копирует чек
  
+ Вставлет чек в поле и подтверждает, что оплатил

![Tezer-Payments-System.jpg](https://i.postimg.cc/x8F5zR0Z/Tezer-Payments-System.jpg "Пример проекта с оплатой")



## Подключение системы оплаты в проект. Код
**1.**
  1. Установки через `git` в главной папке проекта, в терминале:

  ```
  git clone https://github.com/TezerPlatform/TezerPaymentSystem.git
  ```


  2. Установка через `.zip`
    
      + Скачайте в Github этот репозиторий в `.zip` файл, переместите файл в главную папку проекта и распакуйте его. После чего `.zip` можно удалить. У Вас скачается папка с названием `TezerPaymentSystem-main.zip` - **пожалуйста, переименуюте в `TezerPaymentSystem.zip`**

  Должна получиться следующая структура, *посмотрите, чтобы папка `TezerPaymentSystem` была в одной директории с папкой где используется эта система*:

  ![ПримерПапкиПроекта](https://i.postimg.cc/rFyf9pPk/image.png "ПримерПапкиПроекта")

  Где `Roxer` - папка всего вашего проекта

  `main.py` - главный/запускающий файл вашего проекта

  `TezerPaymentSystem` - папка с контрактами платформы, которые Вы хотите по желанию подключить.

  + TezerPaymentSystem
    + tezerx
      + public.key
      
      + signature_verification.py
    + createlink.py
    + installsettings.exe
    + settings.json

**2.**
### Встраивание кода в проект

Создание ссылки и фиксирование времени оплаты:

`amount_rox` - количество токенов, которое пользователь должен оплатить. *В моём случае это количество пользователь сам выбирает. Указывается выше 100.0 до 1,000,000.0 TZR*

`use_contract` - Название контракта строчными буквами. Доступные контракты смотрите тут. По мере обновления мы оповещаем в Telegram канале и здесь происходят обновления.

`information_login` - Информация, которая будет проверяться при обработке чека, если `checking_information` = True. **Также количество символов должно быть до или равно 18. Нельзя использовать спецефические символы и русские буквы.**

`my_address`:
1. Перейдите по ссылке https://t.me/TezerPlatformBot
2. Нажмите на кнопку меню слева и выберите /wallet
3. Скопируйте адрес *(TprimeRaDreSs)* и вставьте его в переменную `my_address`

`create_link_payments()` - возвращает ссылку для оплаты и время создании ссылки. *(Используется в `verify_signature`)*

```python
from TezerPaymentSystem.createlink import create_link_payments

use_contract = "tezerx"
information_login = "DonateRox"
checking_information = True
my_address = "TpSACeH9ZsBEvBJSMRG3n"

link_to_pay, time_create_link = create_link_payments(amount_rox, information_login, use_contract, my_address)
```

**3.**

После этого кода, открывается поле в окне проекта для ввода код-чека (`CodeCheck`)

После того как пользователь ввёл код-чек и нажал кнопку подтвердить чек, выполняем код снизу. *(У каждого контракта своя структура. Мы расматриваем встраивание контракта **TezerX**)*

```python
from TezerPaymentSystem.tezerx.signature_verification import verify_signature

result_pay = verify_signature(check_input, # Введённый чек
                              time_create_link, 
                              amount_rox, 
                              information_login, 
                              use_contract, 
                              my_address, 
                              checking_information)

if result_pay is True:
    print("Спасибо за донат!")
    # ... код, где вы отдаёте продукт пользователю, так как он оплатил.

elif result_pay == "The signature is not authentic":
    print('Подпись неисправна. Просим перезапустить программу, чтобы заново оплатить.')

elif result_pay == "CodeCheck is not relevant":
    print('Время оплаты неправильное.')

elif result_pay == "The payment contract does not match":
    print('Контракт оплаты не соответствует требованному.')

elif result_pay == "The number of tokens does not match":
    print('Количество токенов не правильно указано.')

elif result_pay == "The seller's address does not match":
    print('Адрес получателя указан не верно.')

elif result_pay == "The information does not match":
    print('Указанная информация не соответствует нужной. Info поле заполнено неправильно.')
```

## Безопастность :beginner:

Данные о пользователе, такие как:

+ Telegram ID
+ First name telegram
+ Second name telegram
+ Address TezerPlatform
+ Количество токенов на вашем кошельке
+ Оборот токенов в день/за всё время
  
cохраняются в базе данных, которая находится на нашем личном сервере. Сервер защищён криптографическим алгоритмом RSA. Доступ к нему осущевстляется по токену. - Поэтому выше перечисленные данные 3-им лицам не предоставляется.

### Важно :warning:

+ **Данные, такие как история платежей, номера карт, пароли и другие конфеденциальные данные мы не просим вводить и не сохраняем. Если возникли проблемы с оплатой или попались на мошенника - сообщите [менеджеру](https://t.me/majmanager "Официальный менеджер проекта Tezer Platform")**

+ **Всегда проверяйте данные перед передачей токенов другому человеку.**

+ **Выбирайте безопастный контракт, которому доверяете.**

## О контрактах :bank:

Контракты нужны для того, чтобы пользователь мог сам решать как ему удобнее и выгоднее переводить токены.

Существует 2 типа контрактов:

+ `T` - Конракт без информационного поля. Можно использовать для обычных переводов с Tezer адреса на Tezer адрес
+ `XT` - Контракт с информационным полем. С открытым исходным кодом. Используется для внедрения в проекты.

Первый контракт на Tezer Platform типа `T` - **[OneType](https://telegra.ph/Kontrakt-OneType-06-25 "telegra.ph")**

И паралельно первый контракт типа `XT` - **[TezerX](https://telegra.ph/Kontrakt-TezerX-06-28 "telegra.ph")**

У каждого контракта есть свои условия, свои комиссии (Их устанавливает создатель контракта), чтобы перевест токены TZR.

Создать контракт может каждый желающий имеющий базу программирования. Подробнее про создание контрактов обратитесь к **[Менеджеру](https://t.me/majmanager)**
  

## Контакты :speech_balloon:

+ **Telegram Tezer:** [t.me/TezerNet](https://t.me/TezerNet)
+ **VK CIO:** [vk.com/stepanbelopolsky](https://vk.com/majworker)
+ **Discord server:** [discord.gg/ZAe35YVzhe](https://discord.gg/ZAe35YVzhe)
+ **Website TezerPlatform:** [tezerplatform.github.io](https://tezerplatform.github.io/Tezer/)


# English language
