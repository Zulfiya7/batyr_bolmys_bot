# Save the Batyr Bolmys chatbot code into a .py file for the user
code = """
import streamlit as st

# 🌐 Бет параметрлері
st.set_page_config(page_title="Batyr Bolmys Chatbot", page_icon="🎖", layout="centered")

# 👑 Тақырып
st.title("🎖 Batyr Bolmys Chatbot")
st.markdown("Тарихи-ағартушылық жоба туралы сұрақтарыңызға жауап береді")

# 🗣 Тіл таңдау
lang = st.selectbox(
    "Тілді таңдаңыз | Выберите язык | Select language",
    ["Қазақша", "Русский", "English"]
)

# 💬 Сұрақ енгізу
user_input = st.text_input({
    "Қазақша": "Сұрағыңызды жазыңыз:",
    "Русский": "Задайте вопрос:",
    "English": "Ask your question:"
}[lang])

# 🌟 Алдын ала жауаптар
responses = {
    "Қазақша": {
        "batyr bolmys деген не": "«Batyr Bolmys» – тарихи тұлғаларды, әсіресе Бауыржан Момышұлын кеңінен таныстыруға бағытталған рухани-ағартушылық жоба. Бұл жоба жастарға батырлық пен отансүйгіштік қасиеттерді насихаттауға арналған.",
        "не үшін қажет": "Мақсат – ұлы тұлғалардың ерлігін үлгі ете отырып, жастардың ұлттық рухын ояту, отансүйгіштікке тәрбиелеу.",
        "қашан басталды": "Жоба [дата] күні басталды. Қорытынды іс-шара [дата] күні жоспарланған.",
        "кімдерге арналған": "Жоба негізінен жастарға, студенттерге, мектеп оқушыларына бағытталған. Бірақ тарихқа қызығатын кез келген адам қатыса алады.",
        "бауыржан момышұлы кім": "Бауыржан Момышұлы – Ұлы Отан соғысының даңқты батыры, әскери қолбасшы, жазушы, Халық Қаһарманы.",
        "шығармалары": "Ең танымал еңбектері: «Ар-намыс», «Ұшқан ұя», «Соғыс психологиясы» және т.б.",
        "ерлік жасаған": "Мәскеу түбіндегі шайқаста қазақ жауынгерлерін басқарған және батырлық көрсеткен.",
        "қалай қатысуға болады": "Жобаға қатысу үшін тіркелу формасын толтырып, көрсетілген тапсырмаларды орындау қажет. Тіркелу сілтемесі: [сілтеме].",
        "іс-шаралар өтеді": "Онлайн викториналар, эссе байқауы, бейнежоба, пікірталастар, кездесулер мен марапаттау кеші өтеді.",
        "жүлде немесе сертификат": "Иә, қатысушыларға арнайы сертификаттар мен үздік қатысушыларға марапаттар беріледі.",
        "жоба авторларымен байланысу": "Сіз сұрағыңызды осы чат арқылы қалдыра аласыз немесе [эл. пошта/телефон/Instagram] арқылы хабарласа аласыз.",
        "қай жылы дүниеге": "Ол 1910 жылы Жамбыл облысында дүниеге келген.",
        "марапаттарға ие": "Ол «Халық Қаһарманы» атағына және бірнеше орден мен медальға ие болған.",
        "қабілеттер қажет": "Тарихқа қызығушылық, шығармашылық және патриоттық сезім жеткілікті.",
        "неге batyr bolmys": "Өйткені жоба батырлық болмысты дәріптеп, рухты оятуды мақсат етеді.",
        "материалдар ұсынылады": "Бейнематериалдар, мақалалар, сұхбаттар және онлайн тапсырмалар ұсынылады.",
        "цифрлық құралдар": "Streamlit чатботы, викториналар, онлайн формалары, Zoom кездесулері қолданылады.",
        "неліктен жастар қатысуы": "Өйткені бұл жоба олардың патриотизмін арттырып, тарихты құрметтеуге үйретеді."
    },
    "Русский": {
        "batyr bolmys что это": "«Batyr Bolmys» – духовно-просветительский проект, направленный на широкое знакомство с историческими личностями, в частности, с Бауыржаном Момышұлы. Проект призван воспитывать в молодежи героизм и патриотизм.",
        "зачем нужен": "Цель проекта — через пример подвига великих личностей пробудить национальный дух и воспитать патриотизм у молодежи.",
        "когда начался": "Проект начался [дата]. Заключительное мероприятие запланировано на [дата].",
        "для кого": "Проект в первую очередь адресован молодежи, студентам и школьникам. Однако участвовать может любой, кто интересуется историей.",
        "бауыржан момышұлы кто": "Бауыржан Момышұлы — славный герой Великой Отечественной войны, военный командир, писатель, Народный Герой.",
        "произведения": "Самые известные его произведения: «Ар-намыс», «Ұшқан ұя», «Психология войны» и т.д.",
        "какой подвиг": "Он командовал казахскими войсками в битве под Москвой и проявил героизм.",
        "как участвовать": "Чтобы участвовать в проекте, необходимо заполнить регистрационную форму и выполнить предложенные задания. Ссылка для регистрации: [link].",
        "какие мероприятия": "Онлайн-викторины, конкурс эссе, видео-проекты, дискуссии, встречи и церемония награждения.",
        "приз или сертификат": "Да, участникам выдаются сертификаты, а лучшим — награды.",
        "связаться с авторами": "Вы можете оставить вопрос через этот чат или связаться по электронной почте/телефону/Instagram.",
        "родился в": "Он родился в 1910 году в Жамбылской области.",
        "какие награды": "Он был удостоен звания «Народный Герой», а также нескольких орденов и медалей.",
        "какие навыки": "Интерес к истории, креативность и чувство патриотизма достаточны.",
        "почему batyr bolmys": "Потому что проект прославляет героизм и нацелен на пробуждение духа.",
        "какие материалы": "Видеоматериалы, статьи, интервью и онлайн-задания.",
        "какие цифровые": "Чат-бот на Streamlit, викторины, онлайн-формы, встречи в Zoom.",
        "почему молодежь": "Потому что проект укрепляет патриотизм и учит уважать историю."
    },
    "English": {
        "what is batyr bolmys": "“Batyr Bolmys” is a spiritual and educational project aimed at widely introducing historical figures, particularly Baurzhan Momyshuly. The project seeks to instill heroism and patriotism in young people.",
        "why needed": "The project's goal is to awaken the national spirit and foster patriotism among young people through the example of great individuals' heroic deeds.",
        "when started": "The project started on [date]. The final event is scheduled for [date].",
        "who for": "The project is primarily aimed at young people, students, and schoolchildren, but anyone interested in history can participate.",
        "who is baurzhan momyshuly": "Baurzhan Momyshuly was a renowned hero of the Great Patriotic War, a military commander, author, and People's Hero.",
        "works": "His most famous works include “Ar-namys”, “Ushkan uya”, “Psychology of War”, etc.",
        "what heroism": "He commanded Kazakh troops in the Battle of Moscow and demonstrated great heroism.",
        "how to join": "To participate, you need to fill out the registration form and complete the specified tasks. Registration link: [link].",
        "what events": "Online quizzes, essay contests, video projects, debates, meetings, and an awards ceremony.",
        "prize or certificate": "Yes, participants receive certificates, and top performers are awarded prizes.",
        "contact authors": "You can leave your question via this chat or contact us via email/phone/Instagram.",
        "born in": "He was born in 1910 in the Zhambyl region.",
        "awards": "He was awarded the title “People's Hero” and received several orders and medals.",
        "required skills": "Interest in history, creativity, and a sense of patriotism are sufficient.",
        "why named": "Because the project celebrates heroism and aims to awaken the spirit.",
        "what materials": "Video materials, articles, interviews, and online tasks are offered.",
        "what digital": "Streamlit chatbot, quizzes, online forms, and Zoom meetings are used.",
        "why youth": "Because the project strengthens patriotism and teaches respect for history."
    }
}

# 🔍 Жауап табу
if user_input:
    key = user_input.lower()
    answered = False
    for q, ans in responses[lang].items():
        if q in key:
            st.success(ans)
            answered = True
            break
    if not answered:
        st.warning({
            "Қазақша": "Кешіріңіз, сұрағыңызды түсінбедім.",
            "Русский": "Извините, я не понял ваш вопрос.",
            "English": "Sorry, I didn't understand your question."
        }[lang])
"""

file_path = "/mnt/data/batyr_bolmys_bot.py"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

file_path
