mapping = {
    ' NEZNANO': 'unknown',
    'Afganistan': 'afg',
    'Alandski otoki': 'ala',
    'Albanija': 'alb',
    'Aruba': 'abw',
    'Avstralija': 'aus',
    'Avstrija': 'aut',
    'Azerbajdžan': 'aze',
    'Belgija': 'bel',
    'Bocvana': 'bwa',
    'Bolgarija': 'bgr',
    'Bosna in Hercegovina': 'bih',
    'Ciper': 'cyp',
    'Češka': 'cze',
    'Črna Gora': 'mne',
    'Danska': 'dnk',
    'Džibuti': 'jib',
    'Dominikanska republika': 'dom',
    'Egipt': 'egy',
    'Ekvatorialna Gvineja': 'gnq',
    'Estonija': 'est',
    'Finska': 'fin',
    'Francija': 'fra',
    'Gambija': 'gmb',
    'Grčija': 'grc',
    'Hrvaška': 'hrv',
    'Iran': 'irn',
    'Irska': 'irl',
    'Italija': 'ita',
    'Izrael': 'isr',
    'Južna afrika': 'jar',
    'Katar': 'qat',
    'Kazahstan': 'kaz',
    'Kirgizistan (Kirgizija)': 'kgz',
    'Kosovo': 'xkx',
    'Kuba': 'cub',
    'Latvija': 'lva',
    'Luksemburg': 'lux',
    'Madžarska': 'hum',
    'Makedonija': 'mkd',
    'Maldivi': 'mdv',
    'NAM': 'nam',
    'Namibija': 'nam',
    'Nepal': 'npl',
    'Nizozemska': 'nld',
    'Norveška': 'nor',
    'Mali': 'mli',
    'Malta': 'mlt',
    'Maroko': 'mar',
    'Mauricius (Moris)': 'mus',
    'Mehika': 'mex',
    'Mikronezija': 'fsm',
    'Nemčija': 'deu',
    'Otočje Valis in Futuna': 'wlf',
    'Pakistan': 'pak',
    'Poljska': 'pol',
    'Portugalska': 'prt',
    'Romunija': 'rou',
    'Ruanda': 'rwa',
    'Ruska federacija': 'rus',
    'Slovaška': 'svk',
    'Slovenija': 'svn',
    'Surinam': 'sur',
    'Španija': 'esp',
    'Srbija': 'srb',
    'Švedska': 'swe',
    'Švica': 'che',
    'Tanzanija': 'tza',
    'Tunizija': 'tun',
    'Turčija': 'tur',
    'Ukrajina': 'ukr',
    'Uzbekistan': 'uzb',
    'Združeno kraljestvo': 'gbr',
    'Združeno kraljestvo Velike Britanije in Severne Irske': 'gbr',
    'Združene države Amerike': 'usa',
    'Združeni Arabski Emirati': 'are',
}


def get_county_code(country_name: str):
    return mapping[country_name]
