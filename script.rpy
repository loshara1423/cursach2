define b = Character('Борис', color="#d5d5d5")
define a = Character('Акси', color="#d5d5d5")
define k = Character('Кокос', color="#d5d5d5")
define r = Character('Рядовой кот', color="#d5d5d5")


image  Kokos:
    "kokos"
    zoom 0.7

image  Zloikokos:
    "zloikokos"
    zoom 0.7

image Zadboris:
    "zadboris"
    zoom 0.7

image Boris:
    "boris"
    zoom 0.7

image Borisrot:
    "borisrot"
    zoom 0.7

image Ulboris:
    "ulboris"
    zoom 0.7

image Ulborisrot:
    "ulborisrot"
    zoom 0.7

image Pobaksi:
    "pobaksi"
    zoom 0.7

image Pobaksirot:
    "pobaksirot"
    zoom 0.7

image Aksi:
    "aksi"
    zoom 0.7

image Aksirot:
    "aksirot"
    zoom 0.7

image Lageraksi:
    "lageraksi"
    zoom 1.4

image Lager:
    "lager"
    zoom 1.4





label start:

    scene black 

    r "Командир, какие дальнейший указания?"
    b "Пока придерживаемся обычного распорядка дня и готовимся к наступлению!"
    "Тяжелый и сложный вопрос стоял перед Генералом Борисом. Вопрос, от которого зависело будущее его страны."
    
    #scene ...  
    show Zadboris:
        xalign 0.5
    with fade
    b "Что же дальше"
    b "Что же делать...."
    hide Zadboris
    with fade
    
    scene black
    "Давно длящийся и никак не заканчивающийся конфликт между двумя котогосударствами настиг своего пика."
    "В напряженной обстановке командир Борис пытался продумать план для грядущего наступления, но ничего не приходило в голову."
    "Как вдруг...."
    "За пределом его штаба раздались громкие звуки голосов и толпы."
    "Он поспешно вышел на улицу чтобы разузнать в чем дело."

    scene Lageraksi
    with fade
    "Причиной сбора всех стала Акси. Кошка разведчица."
    "Все думала, что она погибла на задании, но она сумела вернулась спустя долгое время."
    "Увидев Бориса, она поспешила к нему."
    
    scene Lager
    show Boris:
        xalign 0.7
    show Pobaksirot:
        xalign 0.3 yalign 0.9
    with fade
    a "Приветствую вас, у нас состоится долгий разговор."
    hide Pobaksirot
    show Pobaksi:
        xalign 0.3 yalign 0.9

    show Ulborisrot:
        xalign 0.7
    b "Здравствуй Акси, мы уж стали думать, что ты не вернёшься."
    

    scene black
    "Глядя на Акси, Борис поспешил налить воды и достать банку консерв для неё."

    show Boris:
        xalign 0.7
    show Pobaksirot:
        xalign 0.3 yalign 0.9
    a "Не стоит, это подождет. Сейчас важнее другое."
    hide Pobaksirot
    show Pobaksi:
        xalign 0.3 yalign 0.9

    show Borisrot:
        xalign 0.7
    b "Ты уверенна? Выглядишь совсем худо. Что с тобой было? "
    hide Borisrot
    show Boris:
        xalign 0.7

    show Pobaksirot:
        xalign 0.3 yalign 0.9
    a "Меня поймали на четвертый день разведки и взяли в плен. "
    a "Пока я была в плену я узнала много ценной для нас информации. "
    hide Pobaksirot
    show Pobaksi:
        xalign 0.3 yalign 0.9

    show Borisrot:
        xalign 0.7
    b "Я знал, что ты лучшая в своем деле."
    b "Скорее поведай мне что тебе удалось узнать."

    scene black
    with fade

    "Время спустя, выслушав Акси, Борис поспешил отправить ее к врачу."

    #scene ...
    "Борис расхаживал их одного угла в другой бормоча себе под нос."
    
    show Zadboris:
        xalign 0.5
    b "Если застать их ночью?"
    b "Нет. Это не то, что нам нужно…"
    "Всё же ему удалось принять решение и на утро он решил обсудить это с Акси."

    scene black

    #scene ...
    show Aksi:
        xalign 0.3 yalign 0.9
    show Borisrot:
        xalign 0.7
    with fade
    b "Доброго утра, Акси, как ты себя чувствуешь?"
    hide Borisrot
    show Boris:
        xalign 0.7

    show Aksirot:
        xalign 0.3 yalign 0.9
    a "Приветствую. Уже намного лучше."
    hide Aksirot
    show Aksi:
        xalign 0.3 yalign 0.9

    "Борис попросил удалиться всех посторонних."

    show Borisrot:
        xalign 0.7
    b "Я решил, что если так все и продолжится, то эта война никогда не закончится."
    b "Я хочу встречи с Кокосом, а если точнее подписать мирный договор."
    hide Borisrot
    show Boris:
        xalign 0.7
    
    show Aksirot:
        xalign 0.3 yalign 0.9
    a "Я думаю, что это мудрое решение."
    a "Но сомневаюсь, что Кокос согласиться с вами."
    a "Он очень жесток. Единственная цель, которую он преследует – это власть."
    hide Aksirot
    show Aksi:
        xalign 0.3 yalign 0.9

    show Borisrot:
        xalign 0.7
    b "Да, он ужасен... С тех пор как он пришёл к власти многое изменилось...."
    b "Я и представить не мог, что первым делом он решит махать мечом!"
    b "Всё же я думаю, он примет правильное решение и поймёт, что этой войной он ничего не добьётся."
    
    scene black
    show Zadboris:
        xalign 0.5
    with fade 

    menu:
        "что делать?"
        "Отправить Акси":
            jump ploxo
        "Отправить рядового":
            jump xoposho

    return





label ploxo:

    #scene ...
    scene black
    with fade
    show Aksi:
        xalign 0.3 yalign 0.9
    show Borisrot:
        xalign 0.7
    b "Я хочу, чтобы ты снова отправилась туда снова и поговорила с Кокосом о встрече."
    hide Boris
    show Boris:
        xalign 0.7

    show Aksirot:
        xalign 0.3 yalign 0.9
    a "Принято, будет сделано!"
    hide Aksirot
    hide Boris

    scene black
    with fade
    "Прошло много времени, но Акси так и не вернулась…"
    return





label xoposho:

    scene black
    show Aksi:
        xalign 0.3 yalign 0.9
    show Boris:
        xalign 0.7
    b "Я сегодня же отправлю рядового чтобы он договорился о встречи!"
    
    scene black
    "После нескольких ночей рядовой кот вернулся с новостью. Кокос дал добро!"
    "Борис в неспокойной обстановке стал ожидать гостя."

    scene black
    show Boris:
        xalign 0.7
    show Kokos:
        xalign 0.3 yalign 0.9
    k "Ну здравствуй Борис!"
    k "Не ожидал что мы встретимся в таких обстоятельствах."
    k "Что же ты хочешь от меня?"

    show Borisrot:
        xalign 0.7
    b "Приветствую, Кокос, прошу к столу."
    hide Borisrot
    show Boris:
        xalign 0.7
        
    "Кокос уселся напротив Бориса и принялся 'внимательно' его слушать, усмехаясь и почавкивая сухим кормом."

    show Boris
    b "Знаю, что ты хочешь показать всему миру свою власть и могущество, но это может длиться вечно. "
    b "Я предлагаю покончить с этим."

    return