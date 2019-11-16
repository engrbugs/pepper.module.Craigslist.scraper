import configparser

def WriteIni(Data):

    config = configparser.ConfigParser()
    config.read("settings.ini")


    if not config.has_section('main'):
        config.add_section('main')

    config.set('main', 'lastseenUrl1', Data[0])
    config.set('main', 'lastseenUrl2', Data[1])
    config.set('main', 'lastseenUrl3', Data[2])
    config.set('main', 'lastseenUrl4', Data[3])
    config.set('main', 'lastseenUrl5', Data[4])

    with open("settings.ini", 'w') as configfile:
        config.write(configfile)

def readini():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    data = []
    try:
        data.append(config.get('main', 'lastseenUrl1'))
        data.append(config.get('main', 'lastseenUrl2'))
        data.append(config.get('main', 'lastseenUrl3'))
        data.append(config.get('main', 'lastseenUrl4'))
        data.append(config.get('main', 'lastseenUrl5'))
    except:
        data = -1  
    return data;

    