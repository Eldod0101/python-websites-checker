# Website Monitor Bot

## الغرض من الاسكريبت
اسكربت Python هذا يتيح لك مراقبة حالة المواقع بشكل دوري باستخدام **Telegram Bot** لإرسال تنبيهات في حال حدوث أي خطأ في الموقع (مثل انقطاع الاتصال أو أخطاء الخادم). 
يتم التحقق من حالة الموقع بشكل دوري، وإذا كان هناك مشكلة في الاتصال أو الرد من الخادم، سيتم إرسال تنبيه إلى قناة Telegram أو إلى المستخدم عبر البوت.

## المتطلبات
- **Python 3.6 أو أحدث**
- **مكتبة requests**: لتحميل المواقع والتحقق من استجابتها.
- **مكتبة python-telegram-bot**: لإرسال التنبيهات عبر Telegram.

### تثبيت المكتبات المطلوبة:
تأكد من أنك قمت بتثبيت المكتبات التالية باستخدام `pip`:

```bash
pip install requests python-telegram-bot

### خطوات التثبيت
1. الحصول على توكن البوت:

    قم بإنشاء Telegram Bot من خلال BotFather للحصول على التوكن.
    بعد الحصول على التوكن، احتفظ به في مكان آمن لأنه ستحتاجه لاستخدام البوت.

2. الحصول على معرف الدردشة (Chat ID):

    قم بإرسال أي رسالة إلى البوت الخاص بك.

    استخدم السكربت التالي بشكل منفرد لاسترداد chat_id:

import requests

token = 'YOUR_BOT_TOKEN'
url = f"https://api.telegram.org/bot{token}/getUpdates"
response = requests.get(url)
print(response.json())
بعد تشغيل السكربت، ستتمكن من العثور على chat_id في الاستجابة.

. إعداد السكربت:

    قم بنسخ السكربت إلى جهازك.
    افتح السكربت وأدخل BOT_TOKEN و CHAT_ID في الأماكن المحددة:

    BOT_TOKEN = 'YOUR_BOT_TOKEN'  # استبدل بهذا التوكن الخاص بك
    CHAT_ID = 'YOUR_CHAT_ID'  # استبدل بهذا معرف الدردشة الخاص بك

4. تشغيل السكربت:

    بعد تعديل السكربت، يمكنك تشغيله باستخدام الأمر التالي:

    python script_name.py

5. مراقبة المواقع:

    يمكنك تحديد قائمة المواقع التي ترغب في مراقبتها. كل موقع يتم التحقق من حالته بشكل دوري، وإذا حدثت مشكلة، سيتم إرسال تنبيه عبر Telegram Bot.
    لإضافة مواقع جديدة للمراقبة، قم بإضافتها إلى قائمة websites في السكربت:

    websites = [
        "https://www.example.com",
        "https://www.anotherwebsite.com"
    ]

كيف يعمل السكربت؟

    التحقق من حالة المواقع:
        يقوم السكربت بمحاولة الوصول إلى المواقع باستخدام HEAD request لتجنب تحميل المحتوى بالكامل، فقط للتحقق من حالة الموقع.
        إذا كانت الاستجابة غير صحيحة أو إذا حدث خطأ في الاتصال، يتم إرسال تنبيه عبر Telegram Bot.

    إرسال التنبيهات عبر Telegram:
        في حال حدوث أي مشكلة مع أحد المواقع، يقوم السكربت بإرسال رسالة إلى chat_id المحدد.
        الرسائل تتضمن معلومات الموقع، نوع الخطأ، والوقت الذي حدث فيه الخطأ.

ملاحظات:
    يعمل السكربت بشكل دوري ويكرر العملية بناءً على الفاصل الزمني الذي تحدده (افتراضيًا 600 ثانية).
    يتم التعامل مع الأخطاء مثل ConnectionError و Timeout و TooManyRedirects وإرسال تنبيهات مفصلة حول السبب.

دعم
إذا واجهت أي مشاكل أو كانت لديك أسئلة، يمكنك فتح Issue هنا على GitHub أو الاتصال بي مباشرة عبر البريد الإلكتروني abdelrhman0mahmoud1@gmail.com.

المساهمة
إذا كنت ترغب في المساهمة في تطوير السكربت، يمكنك عمل Fork لهذا المستودع، ثم تقديم Pull Request مع التعديلات التي ترغب في إضافتها.

