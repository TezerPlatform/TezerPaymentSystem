# Tezer Platform | TezerPaymentSystem "TPS"

### Financial opportunities available to everyone.

![TezerPlatformLogo](https://i.postimg.cc/L8d88Yx3/photo-2024-07-06-10-07-44.jpg)

## Page navigation :triangular_flag_on_post:

+ [Website Tezer Platform](https://tezerplatform.github.io/Tezer/ "Information site") :ballot_box_with_check:

___

+ [Russian language](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#russian-language)
  + [О проекте](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#о-проекте-heavy_check_mark)
  + [Выгода сторон](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#выгода-сторон-heavy_dollar_sign)
  + [Оплата в 3 действия](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#оплата-в-3-действия-three)
  + [Подключение системы оплаты в проект. Код](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#подключение-системы-оплаты-в-проект-код)
  + [Безопастность](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#безопастность-beginner)
  + [О контрактах](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#о-контрактах-bank)
  + [Контакты](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#контакты-speech_balloon)


# Russian language
## О проекте :heavy_check_mark:

Наш проект представлен, на данный момент, на языке программирования Python. Работаем над тем, чтобы в будущем можно  будет использовать не только код на python, но и на других популярных языках программирования. 

*Если у Вас есть начинающий проект, вы можете подключить быструю и безопасную систему оплаты, с использованием нашей бесплатной платформы Tezer и о вашем проекте узнают заинтересованные люди. Наша задача - предоставить Вам возможность проявить успех начинающего или уже работающего проекта, с выходом на стабильный доход.*

Доход Вы получаете от того, что в вашем проекте оплачивают продукт, плюс Вы можете зарабатывать не зависимо от своего проекта на нашей платформе: [создать контракт](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#О-контрактах) для оплаты и брать комиссию  за переводы или наоборот больше привлекать людей и условием будет - быть подписанным на Ваш канал. Возможностей и идей куча, нужно только реализовать.

> *[..о вашем проекте узнают заинтересованные люди..](https://github.com/TezerPlatform/TezerPaymentSystem?tab=readme-ov-file#Выгода-сторон)*

При подключении системы оплаты, мы рассказываем во всех социальных сетях о вашем проекте, и наша аудитория может заинтересоваться вашим проектом и купить продукт. *Если возникут вопросы при подключении системы оплаты, свяжитесь с [Менеджером проекта](https://t.me/tezermoder).*

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
По вопросам обращаться к [Менеджеру проекта](https://t.me/tezermoder "Официальный менеджер проекта Tezer Platform")

## Оплата в 3 действия :three:

+ Создаётся ссылка для перехода в [Telegram бота](https://t.me/TezerPlatformBot)
  
+ Пользователь переходит по ней, оплачивает и копирует чек
  
+ Вставлет чек в поле и подтверждает, что оплатил

![Tezer-Payments-System.jpg](https://i.postimg.cc/x8F5zR0Z/Tezer-Payments-System.jpg "Пример проекта с оплатой")



## Подключение системы оплаты в проект. Код

1. Установки через `git` в главной папке проекта, в терминале:

```
git clone https://github.com/TezerPlatform/TezerPaymentSystem.git
```


2. Установка через `.zip`
   
     + Скачайте в Github этот репозиторий в `.zip` файл, переместите файл в главную папку проекта и распакуйте его. После чего `.zip` можно удалить.

Должна получиться следующая структура:

![ПримерПапкиПроекта](https://i.postimg.cc/W4psbLRb/image.png "ПримерПапкиПроекта")

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

#### Настройка `settings.json`

Просто запустите консольное приложение `installsettings.exe` и следуйте указаниям.

### Встраивание кода в проект

Создание ссылки и фиксирование времени оплаты:

```python
from TezerPaymentSystem import createlink

# Create link and fix time to TezerPlatform:
# the create_link_payments function accepts: 
# 1. The number of tokens to send
# 2. information (login)
# 3. the name of the contract

link_to_pay, time_create_link = createlink.create_link_payments(amount_rox, "DonateRox", "tezerx")
```

После этого кода, открывается поле в окне проекта для ввода код-чека (`CodeCheck`)

После того как пользователь ввёл код-чек и нажал кнопку подтвердить чек, выполняем  код снизу. *(У каждого контракта своя структура. Мы расматриваем встраивание контракта TezerX)*

```python
from TezerPaymentSystem.tezerx.signature_verification import verify_signature

result_pay = verify_signature(chek, time_create_link, amount_rox, "DonateRox")

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

+ **Данные, такие как история платежей, номера карт, пароли и другие конфеденциальные данные мы не просим вводить и не сохраняем. Если возникли проблемы с оплатой или попались на мошенника - сообщите [менеджеру](https://t.me/tezermoder "Официальный менеджер проекта Tezer Platform")**

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

Создать контракт может каждый желающий имеющий базу программирования. Подробнее про создание контрактов обратитесь к **[Менеджеру](https://t.me/tezermoder)**
  

## Контакты :speech_balloon:

+ **Telegram Tezer:** [t.me/TezerNet](https://t.me/TezerNet)
