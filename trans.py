WORD = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж':'ZH',
        'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': 'I', 'Ы': 'Y', 'Ь': 'I', 'Э': 'E', 'Ю': 'YU',
        'Я': 'YA',' ': ' '}
EXC = {'Ю': 'YU','ЬЯ': 'IA','ИЙ':'Y','ИЯ': 'IA','КС': 'X','Я':'YA','Х':'H','АЛЕКСАНДР':'ALEXANDER','ИЛЬЯ':'ILYA','ВИТАЛИЙ':'VITALIY','АЯ':'AYA','ЬЁ':'YE','ЬЕ':'YE'}

GL = ['А', 'Е', 'Ё', 'И', 'Й', 'О', 'У', 'Ы','Э','Ю', 'Я']

SOGL = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н',
        'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']

names ={'АЛЕКСАНДР':'ALEXANDER','ИЛЬЯ':'ILYA','ВИКТОРИЯ':'VICTORIA', 'ВИКТОР':'VICTOR','БОЙКО': 'BOYKO','ОКСАНА':'OKSANA',
        'ВЫРУЧАЕВ':'VIRUCHAEV','ТЮТЕВА':'TYUTYEVA','ГОРОДЕЦКИЙ':'GORODETSKIY','ВИТАЛИЙ':'VITALIY','ВЯЧЕСЛАВ':'VIACHESLAV',
        'ДОВГАЛЮК':'DOVGALUK','ЛЮБИМЦЕВ':'LYBIMTSEV','ЛАВРЕНТЬЕВА':'LAVRENTJEVA','БОЙКО':'BOIKO','ШТОХ':'SHTOH',
        'АЛЦЫБЕЕВ':'ALTSIBEEV','АРКАДИЙ':'ARKADIY','ПЧЕЛИНЦЕВ':'PCHELINCEV','САЙГИНА':'SAIGINA','СУХОРУКОВ':'SUHORUKHOV',
        'АГУРЬЯНОВ':'AGURYANOV','ЛЮБОВЬ':'LUBOV','ХАМИДУЛЛИНА':'HAMIDULLINA','ВАСИЛЬЕВ':'VASILIEV'}

def trans(name):
    name = name.upper()
    list_name = list(name)
    newname = ''
    i = 0
    while i < len(name):
        if name in names:
            newname += names[name]
            break
        elif i != len(name)-1 and name[i] == 'Ь' and name[i+1] == 'Ё':
            newi = str(EXC['ЬЁ'])
            newname += newi
            i += 2
        elif i != len(name)-1 and name[i] == 'Ь' and name[i+1] == 'Е':
            newi = str(EXC['ЬЕ'])
            newname += newi
            i += 2
        elif i == len(name)-2 and name[-2] == 'А' and name[-1] == 'Я':
            newi = str(EXC['АЯ'])
            newname += newi
            i += 2
        elif name[i] == 'Ю' and name[i-1] in SOGL and name[i+1] in SOGL:
            newi = str(EXC['Ю'])
            newname +=newi
            i += 1
        elif name[i] == 'Ь' and i == len(name)-1:
            i += 1
        elif i == 0 and name[0] == 'Я':
            newi =str(EXC['Я'])
            newname +=newi
            i += 1
        elif name[i] == 'К' and i != len(name)-1 and name[i+1] == 'С' and i != 0 and name[i-1]:
            newi = str(EXC['КС'])
            newname += newi
            i += 2
        elif name[i] == 'И' and i != len(name)-1 and name[i+1] == 'Я':
            newi = str(EXC['ИЯ'])
            newname +=newi
            i += 2
        elif name[i] == 'Ь' and i != len(name)-1 and name[i+1] == 'Я':
            newi = str(EXC['ЬЯ'])
            newname +=newi
            i += 2
        elif name[i] == 'И' and i != len(name)-1 and name[i+1] == 'Й':
            newi = str(EXC['ИЙ'])
            newname +=newi
            i += 2
        elif name[i] == 'Ь' and name[i-1] in SOGL and i != len(name)-1 and name[i+1] in SOGL:
            i += 1
        else:
            newi = str(WORD[name[i]])
            newname +=newi
            i += 1
    return newname.title()



"""
Удалил 1.2.3 коменты
"""
"""
