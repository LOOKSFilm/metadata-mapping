def usergroups(value):
    if value != None:
        if value == "Progress":
            value = "PROGRESS"
    else:
        value = ""
    return value

def collections(value):
    if value != None:
        if value == "DEFA Movie" or value == "DEFA Documentary" or value == "DEFA Animation" or value == "DEFA-Film" or value == "Auftragsproduktionen der DEFA" or value == "Filme mit Unterstützung der DEFA-Stiftung" or value == "Geförderte Projekte / Stipendien DEFA-Stiftung" or value == "Ministerium für Auswärtige Angelegenheiten (MfAA)" or value == "Nachlass Bill Meyers" or value == "Sanssouci Film-Archiv" or value == "Wende-Film":
            value = "East German Film Archives (DEFA)"
        if value == "DEFA Newsreel":
            value = 'East German Newsreel "Der Augenzeuge"'
        if value == "Zeitzeugen-Archiv" or value == "Zeitzeugenarchiv Thomas Grimm":
            value = "Thomas Grimm History Archive"
        if value == "LOOKSfilm":
            value = "LOOKSfilm Productions"
        if value == "Blick in die Welt":
            value = 'West German Newsreel "Blick in die Welt"'
        if value == "Catholic Newsreel":
            value = "German Catholic Newsreel"
        if value == "Wollenberg-Archiv":
            value = "Wollenberg Archive"
        if value == "Vietnam Archive":
            value = "Vietnam Archives"
        if value == "LOOKS München '72":
            value = "LOOKSfilm München '72"
        if value == "LOOKS Chernobyl":
            value = "LOOKSfilm Chernobyl"
        if value == "Blickpunkt-Archiv":
            value = "Blickpunkt"
        if value == "Cintec-Archiv":
            value = "Cintec"
        if value == "Eigenproduktionen DEFA-Stiftung":
            value = "DEFA Interviews"
        if value == "Wydoks-Archiv":
            value = "Wydoks"
    else:
        value = ""
    return value

def format(input):
    if input != None:
        output = []
        values = input.split(",")
        for value in values:
            if value == "DV Cam" or value == "DVCam":
                value = "DVCAM"
            if value == "HD Cam" or value == "HDCAM":
                value = "HDCAM"
            if value == "Umatic" or value == "U-Matic":
                value = "U-matic"
            if value == "XD Cam":
                value = "XDCAM"
            if value == "16 mm":
                value = "16mm"
            if value == "35 mm":
                value = "35mm"
            if value == "70 mm":
                value = "70mm"
            if value == "Betacam":
                value = "Betacam"
            if value == "Betacam SP":
                value = "Betacam SP"
            if value == "Blu-ray":
                value = "Blu-ray"
            if value == "Digital Betacam":
                value = "DigiBeta"
            if value == "DVCPro":
                value = "DVCPRO"
            if value == "DVD":
                value = "DVD"
            if value == "Festplatte" or value == "File (mp4)" or value == "File (ProRes)":
                value = "File"
            if value == "Mini-DV":
                value = "Mini DV"
            if value == "S-VHS":
                value = "S-VHS"
            if value == "S-VHS-C":
                value = "S-VHS-C"
            if value == "Tonband":
                value = "Tonband"
            if value == "VHS":
                value = "VHS"            
            output.append(value)
    else:
        output = ""
    return output

def decade(input):
    if input != None:
        values = input.split(",")
        decades = []
        for value in values:
            decades.append(value)
    else:
        decades = ""
    return decades
    
def genre(input):
    engenres = []
    degenres = []
    frgenres = []
    status = []
    if input != None:
        values = input.split(",")
        for value in values:
            if value == "Advertisement":
                engenres.append("Advertisement")
                degenres.append("Werbung")
                frgenres.append("Publicité")
            if value == "Amateur":
                engenres.append("Amateur")
                degenres.append("Amateurfilm ")
                frgenres.append("Film amateur")
            if value == "Animation":
                engenres.append("Animation")
                degenres.append("Animationsfilm")
                frgenres.append("Film d'animation")
            if value == "Docu" or value == "Documentary":
                engenres.append("Documentary")
                degenres.append("Dokumentarfilm")
                frgenres.append("Documentaire")
            if value == "Docu" or value == "Documentary":
                engenres.append("Documentary")
                degenres.append("Dokumentarfilm")
                frgenres.append("Documentaire")
            if value == "Education and Training" or value == "Educational":
                engenres.append("Education and Training")
                degenres.append("Bildung und Training")
                frgenres.append("Éducation et formation")
            if value == "Fiction":
                engenres.append("Movie and Fiction")
                degenres.append("Spielfilm und Fiktion")
                frgenres.append("Film de fiction")
            if value == "Interview":
                engenres.append(value)
                degenres.append(value)
                frgenres.append(value)
            if value == "News":
                engenres.append(value)
                degenres.append(value)
                frgenres.append("Actualités")
            if value == "Newsreel":
                engenres.append(value)
                degenres.append("Wochenschau")
                frgenres.append("Film d'actualité")
            if value == "Rushes / B-Roll":
                engenres.append("B-Roll")
                degenres.append("B-Roll")
                frgenres.append("B-Roll")
            if value == "Stock Footage":
                engenres.append("Stock Footage")
                degenres.append("Stock Footage")
                frgenres.append("Stock Footage")
            if value == "Trailer":
                engenres.append("Trailer")
                degenres.append("Trailer")
                frgenres.append("Stock Footage")
            if value == "TV Show":
                engenres.append("TV Show")
                degenres.append("TV Show")
                frgenres.append("Émission télévisé")
            if value == "Fine cut":
                status.append("Fine Cut")
            if value == "Picture Lock":
                status.append(value)
            if value == "Rough cut":
                status.append("Rough Cut")
    return engenres, degenres, frgenres, status

def accid(source):
    if source != None:
        if source == "DEFA":
            rid = "93044"
        if source == "Probono":
            rid = "96618"
        if source == "Vietnam Film Institute":
            rid = "96561"
        if source == "Katholisches Filmwerk":
            rid = "96661"
        if source == "Cinecentrum":
            rid = "96844"
        if source == "Deutsche Welle":
            rid = "96845"
        if source == "Historiathek":
            rid = "96058"
        if source == "LOOKSfilm":
            rid = "80005"
        if source == "rbb Media":
            rid = "95724"
        else:
            rid = ""
        return rid 

def tags(input):
    if input != None:
        commas = input.count(",")
        semi = input.count(";")
        #print(commas, semi)
        if commas > semi:
            values = input.split(",")
        else:
            values = input.split(";")
        tags = []
        for value in values:
            tags.append(value)
        tags = list(dict.fromkeys(tags))
    else:
        tags = ""
    return tags

def countries(cop):
    encops = []
    enroas = []
    decops = []
    deroas = []
    frcops = []
    frroas = []
    cops = cop.split(",")
    for cop in cops:
        if cop == "Afghanistan":
            encops.append("Afghanistan")
            decops.append("Afghanistan")
            frcops.append("Afghanistan")
        if cop == "Africa" or cop == "Afrika":
            enroas.append("Africa")
            deroas.append("Afrika")
            frroas.append("Afrique")
        if cop == "Aland Islands":
            encops.append("Finland")
            decops.append("Finnland")
            frcops.append("Finlande")
            enroas.append("Aland Islands")
            frroas.append("Aland(les Îles)")#
            deroas.append("Alandinseln")#
        if cop == "Albania" or cop == "Albanien":
            encops.append("Albania")
            decops.append("Albanien")
            frcops.append("Albanie")
        if cop == "Algeria" or cop == "Algerien":
            encops.append("Algeria")
            decops.append("Algerien")
            frcops.append("Algérie")
        if cop == "American Samoa":
            encops.append("United States of America (USA)")
            decops.append("Vereinigte Staaten von Amerika (USA)")
            frcops.append("États-Unis d'Amérique (USA)")
            enroas.append("American Samoa")
            frroas.append("Samoa américaines")#
            deroas.append("Amerikanisch-Samoa")#
        if cop == "Andorra":
            encops.append("Andorra")
            decops.append("Andorra")
            frcops.append("Andorre")
        if cop == "Angola":
            encops.append("Angola")
            decops.append("Angola")
            frcops.append("Angola")
        if cop == "Anguilla":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Anguilla")
            deroas.append("Anguilla")
            frroas.append("Anguilla")
        if cop == "Antarctis" or cop == "Antarktis":
            encops.append("Antarctica")
            decops.append("Antarktis")
            frcops.append("Antarctique")
        if cop == "Antarctica" or cop == "Antarktis":
            encops.append("Antarctica")
            decops.append("Antarktis")
            frcops.append("Antarctique")
        if cop == "Antigua and Barbuda":
            encops.append("Antigua and Barbuda")
            decops.append("Antigua und Barbuda")
            frcops.append("Antigua-et-Barbuda")
        if cop == "Arctic" or cop == "Arktis":
            enroas.append("Artic")
            deroas.append("Arktis")
            frroas.append("Arctique")
        if cop == "Argentina" or cop == "Argentinien":
            encops.append("Argentina")
            decops.append("Argentinien")
            frcops.append("Argentine")
        if cop == "Armenia" or cop == "Armenien":
            encops.append("Armenia")
            decops.append("Armenien")
            frcops.append("Arménie")
        if cop == "Aruba":
            encops.append("Netherlands")
            decops.append("Niederlande")
            frcops.append("Pays-Bas")
            enroas.append("Aruba")
            deroas.append("Aruba")#
            frroas.append("Aruba")#
        if cop == "Asia" or cop == "Asien":
            enroas.append("Asia")
            deroas.append("Asien")
            frroas.append("Asie")
        if cop == "Australia" or cop == "Australien":
            encops.append("Australia")
            decops.append("Australien")
            frcops.append("Australie")
        if cop == "Austria" or cop == "Österreich":
            encops.append("Austria")
            decops.append("Österreich")
            frcops.append("Autriche")
        if cop == "Austria-Hungary" or cop == "Österreich-Ungarn":
            encops.append("Austria-Hungary")
            decops.append("Österreich-Ungarn")
            frcops.append("Autriche-Hongrie")
        if cop == "Azerbaijan" or cop == "Aserbaidschan":
            encops.append("Azerbaijan")
            decops.append("Aserbaidschan")
            frcops.append("Azerbaïdjan")
        if cop == "Bahamas":
            encops.append("Bahamas")
            decops.append("Bahamas")
            frcops.append("Bahamas")
        if cop == "Bahrain":
            encops.append("Bahrain")
            decops.append("Bahrain")
            frcops.append("Bahreïn")
        if cop == "Bangladesh":
            encops.append("Bangladesh")
            decops.append("Bangladesch")
            frcops.append("Bangladesh")
        if cop == "Barbados":
            encops.append("Barbados")
            decops.append("Barbados")
            frcops.append("Barbade")
        if cop == "Belarus":
            encops.append("Belarus")
            decops.append("Belarus")
            frcops.append("Bélarus")
        if cop == "Belgium" or cop == "Belgien":
            encops.append("Belgium")
            decops.append("Belgien")
            frcops.append("Belgique")
        if cop == "Belize":
            encops.append("Belize")
            decops.append("Belize")
            frcops.append("Belize")        
        if cop == "Benin":
            encops.append("Benin (Dahomey)")
            decops.append("Benin (Dahomey)")
            frcops.append("Bénin (Dahomey)")
        if cop == "Bhutan":
            encops.append("Bhutan")
            decops.append("Bhutan")
            frcops.append("Bhoutan") 
        if cop == "Bolivia" or cop == "Bolivie":
            encops.append("Bolivia")
            decops.append("Bolivien")
            frcops.append("Bolivie")
        if cop == "Bosnia and Herzegovina" or cop == "Bosnien und Herzegowina":
            encops.append("Bosnia and Herzegovina")
            decops.append("Bosnien und Herzegowina")
            frcops.append("Bosnie-Herzégovine")  
        if cop == "Botswana":
            encops.append("Botswana")    
            decops.append("Botswana")
            frcops.append("Botswana")
        if cop == "Bermuda":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Bermuda")
            deroas.append("Bermuda")
            frroas.append("Bermudes")
        if cop == "Bouvet Island":
            encops.append("Norway")
            decops.append("Norwegen")
            frcops.append("Norvège")
            enroas.append("Bouvet Island")
            deroas.append("Bouvetinsel")#
            frroas.append("Bouvet (l'Île)")#
        if cop == "Brazil" or cop == "Brasilien":
            encops.append("Brazil")
            decops.append("Brasilien")
            frcops.append("Brésil")
        if cop == "British Indian Ocean Territory":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("British Indian Ocean Territory")
            deroas.append("Britisches Territorium im Indischen Ozean")#
            frroas.append("Indien (le Territoire britannique de l'océan)")#
        if cop == "British Mandate (Palestine)" or cop == "Britisches Mandat (Palästina)":
            encops.append("Palestine (British Mandate)")
            decops.append("Palästina (Britisches Mandat)")
            frcops.append("Palestine (Mandat britannique)")
        if cop == "Brunei Darussalam":
            encops.append("Brunei Darussalam")
            decops.append("Brunei Darussalam")
            frcops.append("Brunéi Darussalam")
        if cop == "Bulgaria" or cop == "Bulgarien":
            encops.append("Bulgaria")
            decops.append("Bulgarien")
            frcops.append("Bulgarie")
        if cop == "Burkina Faso":
            encops.append("Burkina Faso (Upper Volta)")
            decops.append("Burkina Faso (Obervolta)")
            frcops.append("Burkina Faso (Haute-Volta)")
        if cop == "Burma" or cop == "Birma":
            encops.append("Myanmar (Burma)")
            decops.append("Myanmar (Burma)")
            frcops.append("Myanmar (Birmanie)")
        if cop == "Burundi":
            encops.append("Burundi")
            decops.append("Burundi")
            frcops.append("Burundi")
        if cop == "Cambodia" or cop == "Kambodscha":
            encops.append("Cambodia")
            decops.append("Kambodscha")
            frcops.append("Cambodge")
        if cop == "Cameroon" or cop == "Kamerun":
            encops.append("Cameroon")
            decops.append("Kamerun")
            frcops.append("Cameroun")
        if cop == "Canada" or cop == "Kanada":
            encops.append("Canada")
            decops.append("Kanada")
            frcops.append("Canada")
        if cop == "Cape Verde":
            encops.append("Cabo Verde")
            decops.append("Cabo Verde")
            frcops.append("Cabo Verde")
        if cop == "Cayman Islands":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Cayman Islands")
            deroas.append("Kaimaninseln")#
            frroas.append("Caïmans (les Îles)")#
        if cop == "Central African Republic" or cop == "Zentralafrikanische Republik":
            encops.append("Central African Republic")
            decops.append("Zentralafrikanische Republik")
            frcops.append("République centrafricaine")
        if cop == "Ceylon":
            encops.append("Sri Lanka (Ceylon)")
            decops.append("Sri Lanka (Ceylon)")
            frcops.append("Sri Lanka (Ceylon)")
        if cop == "Chad" or cop == "Tschad":
            encops.append("Chad")
            decops.append("Tschad")
            frcops.append("Tchad")
        if cop == "Chechen Republic" or cop == "Tschechische Republik":
            enroas.append("Chechnya")
            deroas.append("Tschetschenien")
            frroas.append("Tchétchénie")#
        if cop == "Chechnya" or cop == "Tschechische Republik":
            enroas.append("Chechnya")
            deroas.append("Tschetschenien")
            frroas.append("Tchétchénie")#
        if cop == "Chile":
            encops.append("Chile")
            decops.append("Chile")
            frcops.append("Chili")
        if cop == "China" or cop == "Republik China":
            encops.append("China")
            decops.append("China")
            frcops.append("Chine")
        if cop == "Christmas Island":
            encops.append("Australia")
            decops.append("Australien")
            frcops.append("Australie")
            enroas.append("Christmas Island")
            deroas.append("Weihnachtsinsel")#
            frroas.append("Christmas (l'Île)")#
        if cop == "Cocos (Keeling) Islands":
            encops.append("Australia")
            decops.append("Australien")
            frcops.append("Australie")
            enroas.append("Cocos (Keeling) Islands")
            deroas.append("Kokosinseln (Keelinginseln)")#
            frroas.append("Cocos (Keeling) (les Îles)")#
        if cop == "Colombia" or cop == "Kolumbien":
            encops.append("Colombia")
            decops.append("Kolumbien")
            frcops.append("Colombie")
        if cop == "Comoros" or cop == "Komoren":
            encops.append("Comoros")
            decops.append("Komoren")
            frcops.append("Comores")
        if cop == "Congo" or cop == "Kongo":
            encops.append("Congo")
            decops.append("Kongo")
            frcops.append("Congo")
        if cop == "Congo, The Democratic Republic of":
            encops.append("Congo (Democratic Republic of the) (Zaire)")
            decops.append("Kongo (Demokratische Republik) (Zaire)")
            frcops.append("Congo (République démocratique du) (Zaïre)")
        if cop == "Cook Islands":
            encops.append("New Zealand")
            decops.append("Neuseeland")
            frcops.append("Nouvelle-Zélande")
            enroas.append("Cook Islands")
            deroas.append("Cookinseln")#
            frroas.append("Cook (les Îles)")#
        if cop == "Costa Rica":
            encops.append("Costa Rica")
            decops.append("Costa Rica")
            frcops.append("Costa Rica")
        if cop == "Cote d'Ivoire" or cop == "Côted’Ivoire":
            encops.append("Côte d'Ivoire")
            decops.append("Côte d'Ivoire (Elfenbeinküste)")
            frcops.append("Côte d'Ivoire")
        if cop == "Côte d'Ivoire" or cop == "Côte d’Ivoire ":
            encops.append("Côte d'Ivoire")
            decops.append("Côte d'Ivoire (Elfenbeinküste)")
            frcops.append("Côte d'Ivoire")
        if cop == "Croatia" or cop == "Kroatien":
            encops.append("Croatia")
            decops.append("Kroatien")
            frcops.append("Croatie")
        if cop == "Cuba" or cop == "Kuba":
            encops.append("Cuba")
            decops.append("Kuba")
            frcops.append("Cuba")
        if cop == "Curacao":
            encops.append("Netherlands")
            decops.append("Niederlande")
            frcops.append("Pays-Bas")
            enroas.append("Curaçao")
            deroas.append("Curaçao")#
            frroas.append("Curaçao")#
        if cop == "Cyprus" or cop == "Zypern":
            encops.append("Cyprus")
            decops.append("Zypern")
            frcops.append("Chypre")
        if cop == "Czech Republic" or cop == "Tschechische Republik":
            encops.append("Czech Republic")
            decops.append("Tschechische Republik")
            frcops.append("Tchéquie")
        if cop == "Czechoslovakia" or cop == "Tschechoslowakei":
            encops.append("Czechoslovakia")
            decops.append("Tschechoslowakei")
            frcops.append("Tchécoslovaquie")
        if cop == "Denmark" or cop == "Dänemark":
            encops.append("Denmark")
            decops.append("Dänemark")
            frcops.append("Danemark")
        if cop == "Deutsche Demokratische Republik (DDR)":
            encops.append("Germany (East)")
            decops.append("Deutsche Demokratische Republik (DDR)")
            frcops.append("Allemagne (Est)")
        if cop == "Djibouti" or cop == "Dschibuti":
            encops.append("Djibouti (French Somaliland)")
            decops.append("Dschibuti (Französische Somaliküste)")
            frcops.append("Djibouti (Côte française des Somalis)")
        if cop == "Dominica":
            encops.append("Dominica")
            decops.append("Dominica")
            frcops.append("Dominique")
        if cop == "Dominican Republic" or cop == "Dominikanische Republik":
            encops.append("Dominican Republic")
            decops.append("Dominikanische Republik")
            frcops.append("République dominicaine")
        if cop == "East Timor":
            encops.append("Timor-Leste")
            decops.append("Osttimor (Timor-Leste)")
            frcops.append("Timor-Leste")
        if cop == "Ecuador":
            encops.append("Ecuador")
            decops.append("Ecuador")
            frcops.append("Équateur")
        if cop == "Egypt" or cop == "Ägypten":
            encops.append("Egypt")
            decops.append("Ägypten")
            frcops.append("Égypte")
        if cop == "El Salvador":
            encops.append("El Salvador")
            decops.append("El Salvador")
            frcops.append("El Salvador")
        if cop == "Equatorial Guinea" or cop == "Äquatorialguinea":
            encops.append("Equatorial Guinea")
            decops.append("Äquatorialguinea")
            frcops.append("Guinée équatoriale")
        if cop == "Eritrea":
            encops.append("Eritrea")
            decops.append("Eritrea")
            frcops.append("Érythrée")
        if cop == "Estonia" or cop == "Estland":
            encops.append("Estonia")
            decops.append("Estland")
            frcops.append("Estonie")
        if cop == "Ethiopia" or cop == "Äthiopien":
            encops.append("Ethiopia")
            decops.append("Äthiopien")
            frcops.append("Éthiopie")
        if cop == "Europe" or cop == "Europa":
            enroas.append("Europe")
            deroas.append("Europa")
            frroas.append("Europe")#
        if cop == "Falkland Islands" or cop == "Falklandinseln":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Falkland Islands (Malvinas)")
            deroas.append("Falklandinseln (Malwinen)")#
            frroas.append("Falkland (Malouines) (les Îles)")#
        if cop == "Faroe Islands" or cop == "Färöer Inseln":
            encops.append("Denmark")
            decops.append("Dänemark")
            frcops.append("Danemark")
            enroas.append("Faroe Islands")
            deroas.append("Färöer Inseln")#
            frroas.append("Féroé (les Îles)")#
        if cop == "Federation of Malaya" or cop == "Föderation Malaya":
            encops.append("Malaysia")
            decops.append("Malaysia")
            frcops.append("Malaisie")
        if cop == "Fiji" or cop == "Fidschi":
            encops.append("Fiji")
            decops.append("Fidschi")
            frcops.append("Fidji")
        if cop == "Finland" or cop == "Finnland":
            encops.append("Finland")
            decops.append("Finnland")
            frcops.append("Finlande")
        if cop == "Formosa":
            encops.append("Taiwan (Formosa)")
            decops.append("Taiwan (Formosa)")
            frcops.append("Taïwan (Formose)")
        if cop == "France" or cop == "Frankreich":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
        if cop == "French Guiana" or cop == "Französisch-Guayana":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("French Guiana")
            deroas.append("Französisch-Guayana")#
            frroas.append("Guyane française")#
        if cop == "French Polynesia":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("French Polynesia")
            deroas.append("Französisch-Polynesien")
            frroas.append("Polynésie française") 
        if cop == "French Southern Territories":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("French Southern Territories")
            deroas.append("Französische Süd- und Antarktisgebiete")#
            frroas.append("Terres australes françaises")#
        if cop == "Gabon" or cop == "Gabun":
            encops.append("Gabon")
            decops.append("Gabun")
            frcops.append("Gabon")
        if cop == "Gambia":
            encops.append("Gambia")
            decops.append("Gambia")
            frcops.append("Gambie")
        if cop == "Georgia" or cop == "Georgien":
            encops.append("Georgia")
            decops.append("Georgien")
            frcops.append("Géorgie")
        if cop == "German Democratic Republic (GDR)" or cop == "Deutsche Demokratische Republik (DDR)":
            encops.append("Germany (East)")
            decops.append("Deutsche Demokratische Republik (DDR)")
            frcops.append("Allemagne (Est)")
        if cop == "Germany" or cop == "Deutschland":
            encops.append("Germany")
            decops.append("Deutschland")
            frcops.append("Allemagne")
        if cop == "Germany (East)":
            encops.append("Germany (East)")
            decops.append("Deutsche Demokratische Republik (DDR)")
            frcops.append("Allemagne (Est)")
        if cop == "Germany (Soviet Zone)" or cop == "Deutschland (Sowjetische Zone)":
            encops.append("Germany (East)")
            decops.append("Deutschland (Sowjetische Zone)")
            frcops.append("Allemagne (Est)")
            enroas.append("Germany (Soviet Zone)")
            frroas.append("Allemagne (zone soviétique)")#
        if cop == "Germany (West)" or cop == "Bundesrepublik Deutschland (BRD)":
            encops.append("Germany")
            decops.append("Deutschland")
            frcops.append("Allemagne")
        if cop == "Germany (Western Allied Zone)" or cop == "Deutschland (Westalliierte Zone)":
            encops.append("Germany")
            decops.append("Deutschland")
            frcops.append("Allemagne")
            enroas.append("Germany (Western Allied Zone)")
            deroas.append("Deutschland (Westalliierte Zone)")#
            frroas.append("Allemagne (zone alliée occidentale) (Trizone)")#
        if cop == "Ghana":
            encops.append("Ghana")
            decops.append("Ghana")
            frcops.append("Ghana")
        if cop == "Gibraltar":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Gibraltar")
            deroas.append("Gibraltar")
            frroas.append("Gibraltar")
        if cop == "Great Britain" or cop == "Großbritannien":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
        if cop == "Greece" or cop == "Griechenland":
            encops.append("Greece")
            decops.append("Griechenland")
            frcops.append("Grèce")
        if cop == "Greenland" or cop == "Grönland":
            encops.append("Greenland")
            decops.append("Grönland")
            frcops.append("Groenland")
        if cop == "Grenada":
            encops.append("Grenada")
            decops.append("Grenada")
            frcops.append("Grenade")
        if cop == "Guadeloupe":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("Guadeloupe")
            deroas.append("Guadeloupe")#
            frroas.append("Guadeloupe")#
        if cop == "Guam":
            encops.append("United States of America (USA)")
            decops.append("Vereinigte Staaten von Amerika (USA)")
            frcops.append("États-Unis d'Amérique (USA)")
            enroas.append("Guam")
            deroas.append("Guam")#
            frroas.append("Guam")#
        if cop == "Guatemala":
            encops.append("Guatemala")
            decops.append("Guatemala")
            frcops.append("Guatemala")
        if cop == "Guinea":
            encops.append("Guinea (French Guinea)")
            decops.append("Guinea (Französisch-Guinea)")
            frcops.append("Guinée (Guinée française)")
        if cop == "Guinea-Bissau":
            encops.append("Guinea-Bissau (Portuguese Guinea)")
            decops.append("Guinea-Bissau (Portugiesisch-Guinea)")
            frcops.append("Guinée-Bissau (Guinée portugaise)")
        if cop == "Guyana":
            encops.append("Guyana")
            decops.append("Guyana")
            frcops.append("Guyana")
        if cop == "Haiti":
            encops.append("Haiti")
            decops.append("Haiti")
            frcops.append("Haïti")
        if cop == "Heard and Mc Donald Islands":
            encops.append("Australia")
            decops.append("Australien")
            frcops.append("Australie")
            enroas.append("Heard and McDonald Islands")
            deroas.append("Heard und McDonaldinseln")#
            frroas.append("Heard-et-Îles MacDonald")#
        if cop == "Holy See (Vatican City State)" or cop == "Vatikan":
            encops.append("Vatican City")
            decops.append("Vatikanstadt")
            frcops.append("Vatican (État de la Cité du)")
        if cop == "Honduras":
            encops.append("Honduras")
            decops.append("Honduras")
            frcops.append("Honduras")
        if cop == "Hong Kong" or cop == "Hongkong":
            encops.append("Hong Kong")
            decops.append("Hongkong")
            frcops.append("Hong Kong")
        if cop == "Hungary" or cop == "Ungarn":
            encops.append("Hungary")
            decops.append("Ungarn")
            frcops.append("Hongrie")
        if cop == "Iceland" or cop == "Island":
            encops.append("Iceland")
            decops.append("Island")
            frcops.append("Islande")
        if cop == "India" or cop == "Indien":
            encops.append("India")
            decops.append("Indien")
            frcops.append("Inde")
        if cop == "Indochina":
            encops.append("Indochina")
            decops.append("Indochina")
            frcops.append("Indochine")
        if cop == "Indonesia" or cop == "Indonesien":
            encops.append("Indonesia")
            decops.append("Indonesien")
            frcops.append("Indonésie")
        if cop == "Iran":
            encops.append("Iran")
            decops.append("Iran")
            frcops.append("Iran")
        if cop == "Iran, Islamic Republic of":
            encops.append("Iran")
            decops.append("Iran")
            frcops.append("Iran")
        if cop == "Iraq" or cop == "Irak":
            encops.append("Iraq")
            decops.append("Irak")
            frcops.append("Iraq")
        if cop == "Ireland" or cop == "Irland":
            encops.append("Ireland")
            decops.append("Irland")
            frcops.append("Irlande")
        if cop == "Israel":
            encops.append("Israel")
            decops.append("Israel")
            frcops.append("Israel")
        if cop == "Italy" or cop == "Italien":
            encops.append("Italy")
            decops.append("Italien")
            frcops.append("Italie")
        if cop == "Ivory Coast" or cop == "Elfenbeinküste":
            encops.append("Côte d'Ivoire")
            decops.append("Côte d'Ivoire (Elfenbeinküste)")
            frcops.append("Côte d'Ivoire")
        if cop == "Jamaica" or cop == "Jamaika":
            encops.append("Jamaica")
            decops.append("Jamaika")
            frcops.append("Jamaïque")
        if cop == "Japan":
            encops.append("Japan")
            decops.append("Japan")
            frcops.append("Japon")
        if cop == "Jordan" or cop == "Jordanien":
            encops.append("Jordan")
            decops.append("Jordanien")
            frcops.append("Jordanie")
        if cop == "Kazakstan" or cop == "Kasachstan":
            encops.append("Kazakhstan")
            decops.append("Kasachstan")
            frcops.append("Kazakhstan")
        if cop == "Kenya" or cop == "Kenia":
            encops.append("Kenya")
            decops.append("Kenia")
            frcops.append("Kenya")
        if cop == "Kiribati":
            encops.append("Kiribati")
            decops.append("Kiribati")
            frcops.append("Kiribati")
        if cop == "Kongo":
            encops.append("Congo")
            decops.append("Kongo")
            frcops.append("Congo")
        if cop == "Korea":
            encops.append("Korea")
            decops.append("Korea")
            frcops.append("Corée")
        if cop == "Korea, Democratic People's Republic of":
            encops.append("Korea (South)")
            decops.append("Korea (Süd)")
            frcops.append("Corée (Sud)")
        if cop == "Korea, Republic of":
            encops.append("Korea (North)")
            decops.append("Korea (Nord)")
            frcops.append("Corée (Nord)")
        if cop == "Kuwait":
            encops.append("Kuwait")
            decops.append("Kuwait")
            frcops.append("Koweït")
        if cop == "Kyrgyzstan" or cop == "Kirgisistan":
            encops.append("Kyrgyzstan")
            decops.append("Kirgistan (Kirgisistan)")
            frcops.append("Kirghizistan")
        if cop == "Lao People's Democratic Republic":
            encops.append("Laos")
            decops.append("Laos")
            frcops.append("Laos")
        if cop == "Laos" or cop == "Laos":
            encops.append("Laos")
            decops.append("Laos")
            frcops.append("Laos")
        if cop == "Latvia" or cop == "Lettland":
            encops.append("Latvia")
            decops.append("Lettland")
            frcops.append("Lettonie")
        if cop == "Lebanon" or cop == "Libanon":
            encops.append("Lebanon")
            decops.append("Libanon")
            frcops.append("Liban")
        if cop == "Lesotho":
            encops.append("Lesotho (Basutoland)")
            decops.append("Lesotho (Basutoland)")
            frcops.append("Lesotho (Basutoland)")
        if cop == "Liberia":
            encops.append("Liberia")
            decops.append("Liberia")
            frcops.append("Libéria")
        if cop == "Libya" or cop == "Libyen":
            encops.append("Libya")
            decops.append("Libyen")
            frcops.append("Libye")
        if cop == "Libyan Arab Jamahiriya" or cop == "Libysch-Arabische Dschamahirija":
            encops.append("Libyan Arab Jamahiriya")
            decops.append("Libysch-Arabische Dschamahirija")
            frcops.append("Jamahiriya arabe libyenne")
        if cop == "Lichtenstein":
            encops.append("Liechtenstein")
            decops.append("Liechtenstein")
            frcops.append("Liechtenstein")
        if cop == "Liechtenstein":
            encops.append("Liechtenstein")
            decops.append("Liechtenstein")
            frcops.append("Liechtenstein")
        if cop == "Lithuania" or cop == "Litauen":
            encops.append("Lithuania")
            decops.append("Litauen")
            frcops.append("Lituanie")
        if cop == "Luxembourg" or cop == "Luxemburg":
            encops.append("Luxembourg")
            decops.append("Luxemburg")
            frcops.append("Luxembourg")
        if cop == "Lybia" or cop == "Libyen":
            encops.append("Libya")
            decops.append("Libyen")
            frcops.append("Libye")
        if cop == "Macao":
            encops.append("China")
            decops.append("China")
            frcops.append("Chine")
            enroas.append("Macao")
            deroas.append("Macao")#
            frroas.append("Macao")#
        if cop == "Macedonia, The Former Yugoslav Republic Of":
            encops.append("Macedonia (North)")
            decops.append("Mazedonien (Nord)")
            frcops.append("Macédoine (Nord)")
        if cop == "Madagascar" or cop == "Madagaskar":
            encops.append("Madagascar")
            decops.append("Madagaskar")
            frcops.append("Madagascar")
        if cop == "Malawi":
            encops.append("Malawi")
            decops.append("Malawi")
            frcops.append("Malawi")
        if cop == "Malaysia":
            encops.append("Malaysia")
            decops.append("Malaysia")
            frcops.append("Malaisie")
        if cop == "Malaysian Federation" or cop == "Föderation Malaya":
            encops.append("Malaysia")
            decops.append("Malaysia")
            frcops.append("Malaisie")
        if cop == "Malaysian Union" or cop == "Malaiische Union":
            encops.append("Malaysia")
            decops.append("Malaysia")
            frcops.append("Malaisie")
        if cop == "Maldives" or cop == "Malediven":
            encops.append("Maldives")
            decops.append("Malediven")
            frcops.append("Maldives")
        if cop == "Mali":
            encops.append("Mali (French Sudan)")
            decops.append("Mali (Französisch-Sudan)")
            frcops.append("Mali (Soudan français)")
        if cop == "Malta":
            encops.append("Malta")
            decops.append("Malta")
            frcops.append("Malte")
        if cop == "Marshall Islands" or cop == "Marshallinseln" or cop == "Marshall-Inseln":
            encops.append("Marshall Islands")
            decops.append("Marshallinseln")
            frcops.append("Marshall (les Îles)")
        if cop == "Marinique":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("Martinique")
            deroas.append("Martinique")#
            frroas.append("Martinique")#
        if cop == "Mauritania" or cop == "Mauretanien":
            encops.append("Mauritania")
            decops.append("Mauretanien")
            frcops.append("Mauritanie")
        if cop == "Mauritius":
            encops.append("Mauritius")
            decops.append("Mauritius")
            frcops.append("Maurice")
        if cop == "Mayotte":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("Mayotte")
            deroas.append("Mayotte")#
            frroas.append("Mayotte")#
        if cop == "Mexico" or cop == "Mexiko":
            encops.append("Mexico")
            decops.append("Mexiko")
            frcops.append("Mexique")
        if cop == "Micronesia, Federated States of":
            encops.append("Micronesia")
            decops.append("Mikronesien")
            frcops.append("Micronésie")
        if cop == "Moldova, Republic of":
            encops.append("Moldova")
            decops.append("Moldau (Moldawien)")
            frcops.append("Moldova")
        if cop == "Monaco":
            encops.append("Monaco")
            decops.append("Monaco")
            frcops.append("Monaco")
        if cop == "Mongolia" or cop == "Mongolei":
            encops.append("Mongolia")
            decops.append("Mongolei")
            frcops.append("Mongolie")
        if cop == "Montenegro":
            encops.append("Montenegro")
            decops.append("Montenegro")
            frcops.append("Monténégro")
        if cop == "Montserrat":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Montserrat")
            deroas.append("Montserrat")#
            frroas.append("Montserrat")#
        if cop == "Morocco" or cop == "Marokko":
            encops.append("Morocco")
            decops.append("Marokko")
            frcops.append("Maroc")
        if cop == "Mozambique" or cop == "Mosambik":
            encops.append("Mozambique")
            decops.append("Mosambik")
            frcops.append("Mozambique")
        if cop == "Myanmar":
            encops.append("Myanmar (Burma)")
            decops.append("Myanmar (Burma)")
            frcops.append("Myanmar (Birmanie)")
        if cop == "Namibia":
            encops.append("Namibia")
            decops.append("Namibia")
            frcops.append("Namibie")
        if cop == "Nauru":
            encops.append("Nauru")
            decops.append("Nauru")
            frcops.append("Nauru")
        if cop == "Nepal":
            encops.append("Nepal")
            decops.append("Nepal")
            frcops.append("Népal")
        if cop == "Netherlands" or cop == "Niederlande":
            encops.append("Netherlands")
            decops.append("Niederlande")
            frcops.append("Pays-Bas")
        if cop == "Netherlands Antilles":
            encops.append("Nehterlands")
            decops.append("Niederlande")
            frcops.append("Pays-Bas")
            enroas.append("Netherlands Antilles")
            deroas.append("Niederländische Antillen")#
            frroas.append("Antilles néerlandaises")#
        if cop == "New Caledonia":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("New Caledonia")
            deroas.append("Neukaledonien")#
            frroas.append("Nouvelle-Calédonie")#
        if cop == "New Guinea" or cop == "Neuguinea":
            enroas.append("New Guinea")
            deroas.append("Neuguinea")
            frroas.append("Nouvelle-Guinée")
        if cop == "New Zealand" or cop == "Neuseeland":
            encops.append("New Zealand")
            decops.append("Neuseeland")
            frcops.append("Nouvelle-Zélande")
        if cop == "Nicaragua":
            encops.append("Nicaragua")
            decops.append("Nicaragua")
            frcops.append("Nicaragua")
        if cop == "Niger":
            encops.append("Niger")
            decops.append("Niger")
            frcops.append("Niger")
        if cop == "Nigeria":
            encops.append("Nigeria")
            decops.append("Nigeria")
            frcops.append("Nigéria")
        if cop == "Niue":
            encops.append("Niue")
            decops.append("Niue")
            frcops.append("Niue")
        if cop == "Norfolk Island":
            encops.append("Australia")
            decops.append("Australien")
            frcops.append("Australie")
            enroas.append("Norfolk Island")
            deroas.append("Norfolkinsel")
            frroas.append("Norfolk (l'Île)") 
        if cop == "Northern Mariana Islands":
            encops.append("United States of America (USA)")
            decops.append("Vereinigte Staaten von Amerika (USA)")
            frcops.append("États-Unis d'Amérique (USA)")
            enroas.append("Northern Mariana Islands")
            deroas.append("Nördliche Marianen")
            frroas.append("Mariannes du Nord (les Îles)")
        if cop == "Norway" or cop == "Norwegen":
            encops.append("Norway")
            decops.append("Norwegen")
            frcops.append("Norvège")
        if cop == "Oceania" or cop == "Ozeanien":
            enroas.append("Oceania")
            deroas.append("Ozeanien")
            frroas.append("Océanie")
        if cop == "Oceans":
            enroas.append("Oceans")
            deroas.append("Ozeane")#
            frroas.append("Océans")#
        if cop == "Oman":
            encops.append("Oman")
            decops.append("Oman")
            frcops.append("Oman")
        if cop == "Outer Space" or cop == "Weltraum":
            enroas.append("Outer Space")
            deroas.append("Weltraum")#
            frroas.append("Espace")#
        if cop == "Pakistan":
            encops.append("Pakistan")
            decops.append("Pakistan")
            frcops.append("Pakistan")
        if cop == "Palau":
            encops.append("Palau")
            decops.append("Palau")
            frcops.append("Palaos")
        if cop == "Palestine" or cop == "Palästina":
            encops.append("Palestine (State of)")
            decops.append("Palästina (Staat)")
            frcops.append("Palestine (État de)")
        if cop == "Panama":
            encops.append("Panama")
            decops.append("Panama")
            frcops.append("Panama")
        if cop == "Papua New Guinea" or cop == "Papua-Neuguinea":
            encops.append("Papua New Guinea")
            decops.append("Papua-Neuguinea")
            frcops.append("Papouasie-Nouvelle-Guinée")
        if cop == "Paraguay":
            encops.append("Paraguay")
            decops.append("Paraguay")
            frcops.append("Paraguay")
        if cop == "Peru":
            encops.append("Peru")
            decops.append("Peru")
            frcops.append("Pérou")
        if cop == "Philippines" or cop == "Philippinen":
            encops.append("Philippines")
            decops.append("Philippinen")
            frcops.append("Philippines")
        if cop == "Pitcairn":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Pitcairn")
            deroas.append("Pitcairn")#
            frroas.append("Pitcairn")#
        if cop == "Poland" or cop == "Polen":
            encops.append("Poland")
            decops.append("Polen")
            frcops.append("Pologne")
        if cop == "Polynesia" or cop == "Polynesien":
            enroas.append("Polynesia")
            deroas.append("Polynesien")#
            frroas.append("Polynésie")#
        if cop == "Portugal":
            encops.append("Portugal")
            decops.append("Portugal")
            frcops.append("Portugal")
        if cop == "Province of China":
            encops.append("China")
            decops.append("China")
            frcops.append("Chine")
        if cop == "Puerto Rico":
            encops.append("Puerto Rico")
            decops.append("Porto Rico")
            frcops.append("Puerto Rico")
        if cop == "Qatar" or cop == "Katar":
            encops.append("Qatar")
            decops.append("Katar")
            frcops.append("Qatar")
        if cop == "Reunion":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("Réunion")
            deroas.append("Réunion")#
            frroas.append("Réunion")#
        if cop == "Rhodesia" or cop == "Rhodesien":
            encops.append("Zimbabwe (Rhodesia)")
            decops.append("Simbabwe (Rhodesien)")
            frcops.append("Zimbabwe (Rhodésie)")
        if cop == "Romania" or cop == "Rumänien":
            encops.append("Romania")
            decops.append("Rumänien")
            frcops.append("Roumanie")
        if cop == "Russia" or cop == "Russland":
            encops.append("Russia")
            decops.append("Russland")
            frcops.append("Russie")
        if cop == "Rwanda" or cop == "Ruanda":
            encops.append("Rwanda")
            decops.append("Ruanda")
            frcops.append("Rwanda")
        if cop == "Saar area" or cop == "Saargebiet":
            encops.append("Germany")
            decops.append("Deutschland")
            frcops.append("Allemagne")
            enroas.append("Saar area")
            deroas.append("Saargebiet")#
            frroas.append("Région de la Sarre")#
        if cop == "Saarland":
            decops.append("Deutschland")
            deroas.append("Saarland")
        if cop == "Saint Helana":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Saint Helena (Ascension and Tristan da Cunha)")
            deroas.append("St. Helena (Ascension und Tristan da Cunha)")
            frroas.append("Sainte-Hélène (Ascension et Tristan da Cunha)")
        if cop == "Saint Kitts & Nevis":
            encops.append("Saint Kitts and Nevis")
            decops.append("St. Kitts und Nevis")
            frcops.append("Saint-Kitts-et-Nevis")
        if cop == "Saint Lucia":
            encops.append("Saint Lucia")
            decops.append("St. Lucia")
            frcops.append("Sainte-Lucie")
        if cop == "Saint Pierre and Miquelon":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("Saint Pierre and Miquelon")
            deroas.append("St. Pierre und Miquelon")#
            frroas.append("Saint-Pierre-et-Miquelon")#
        if cop == "Saint Vincent and the Grenadines":
            encops.append("Saint Vincent and the Grenadines")
            decops.append("St. Vincent und die Grenadinen")
            frcops.append("Saint-Vincent-et-Grenadines")
        if cop == "Samoa":
            encops.append("Samoa")
            decops.append("Samoa")
            frcops.append("Samoa")
        if cop == "San Marino":
            encops.append("San Marino")
            decops.append("San Marino")
            frcops.append("Saint-Marin")
        if cop == "Sao Tome and Principe":
            encops.append("São Tomé and Príncipe")
            decops.append("São Tomé und Príncipe")
            frcops.append("Sao Tomé-et-Principe")
        if cop == "Saudi Arabia" or cop == "Saudi-Arabien":
            encops.append("Saudi Arabia")
            decops.append("Saudi-Arabien")
            frcops.append("Arabie Saoudite")
        if cop == "Scotland" or cop == "Schottland":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Scotland")
            deroas.append("Schottland")
            frroas.append("Écosse")
        if cop == "Senegal":
            encops.append("Senegal")
            decops.append("Senegal")
            frcops.append("Sénégal")
        if cop == "Serbia" or cop == "Serbien":
            encops.append("Serbia")
            decops.append("Serbien")
            frcops.append("Serbie")
        if cop == "Serbia and Montenegro":
            encops.append("Serbia")
            decops.append("Serbien")
            frcops.append("Serbie")
        if cop == "Seychelles" or cop == "Seychellen":
            encops.append("Seychelles")
            decops.append("Seychellen")
            frcops.append("Seychelles")
        if cop == "Sierra Leone":
            encops.append("Sierra Leone (British Sierra Leone)")
            decops.append("Sierra Leone")
            frcops.append("Sierra Leone")
        if cop == "Singapore" or cop == "Singapur":
            encops.append("Singapore")
            decops.append("Singapur")
            frcops.append("Singapour")
        if cop == "Slovakia" or cop == "Slowakei":
            encops.append("Slovakia")
            decops.append("Slowakei")
            frcops.append("Slovaquie")
        if cop == "Slovenia" or cop == "Slowenien":
            encops.append("Slovenia")
            decops.append("Slowenien")
            frcops.append("Slovénie")
        if cop == "Solomon Islands" or cop == "Salomonen":
            encops.append("Solomon Islands")
            decops.append("Salomonen")
            frcops.append("Salomon (les Îles)")
        if cop == "Somalia":
            encops.append("Somalia")
            decops.append("Somalia")
            frcops.append("Somalie")
        if cop == "South Africa" or cop == "Südafrika":
            encops.append("South Africa")
            decops.append("Südafrika")
            frcops.append("Afrique du Sud")
        if cop == "South America" or cop == "Südamerika":
            enroas.append("South America")
            deroas.append("Südamerika")
            frroas.append("Amérique du Sud")
        if cop == "South Arabian Federation" or cop == "Südarabische Föderation":
            encops.append("Yemen")
            decops.append("Jemen")
            frcops.append("Yémen")
        if cop == "South Georgia & The South Sandwich Islands":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("South Georgia and The South Sandwich Islands")
            deroas.append("Südgeorgien und die Südlichen Sandwichinseln")
            frroas.append("Géorgie du Sud-et-les Îles Sandwich du Sud")
        if cop == "South Korea" or cop == "Südkorea":
            encops.append("Korea (South)")
            decops.append("Korea (Süd)")
            frcops.append("Corée (Sud) ")
        if cop == "South Vietnam" or cop == "Südvietnam":
            encops.append("Vietnam (South)")
            decops.append("Vietnam (Süd)")
            frcops.append("Viêtnam (Sud)")
        if cop == "Soviet Union" or cop == "Sowjetunion (SU)":
            encops.append("Soviet Union (USSR)")
            decops.append("Sowjetunion (SU)")
            frcops.append("Union soviétique (URSS)")
        if cop == "Spain" or cop == "Spanien":
            encops.append("Spain")
            decops.append("Spanien")
            frcops.append("Espagne")
        if cop == "Spitzbergen":
            encops.append("Norway")
            decops.append("Norwegen")
            frcops.append("Norvège")
            enroas.append("Spitzbergen")
            deroas.append("Spitsbergen (Svalbard)")#
            frroas.append("Spitsbergen (Svalbard)")#
        if cop == "Sri Lanka":
            encops.append("Sri Lanka (Ceylon)")
            decops.append("Sri Lanka (Ceylon)")
            frcops.append("Sri Lanka (Ceylon)")
        if cop == "Sudan":
            encops.append("Sudan")
            decops.append("Sudan")
            frcops.append("Soudan")
        if cop == "Suriname":
            encops.append("Suriname")
            decops.append("Suriname")
            frcops.append("Suriname")
        if cop == "Svalbard and Jan Mayen":
            encops.append("Norway")
            decops.append("Norwegen")
            frcops.append("Norvège")
            enroas.append("Svalbard and Jan Mayen")
            deroas.append("Svalbard und Jan Mayen")#
            frroas.append("Svalbard et Jan Mayen")#
        if cop == "Swaziland":
            encops.append("Eswatini (Swasiland)")
            decops.append("Eswatini (Swaziland)")
            frcops.append("Eswatini (Swaziland)")
        if cop == "Sweden" or cop == "Schweden":
            encops.append("Sweden")
            decops.append("Schweden")
            frcops.append("Suède")
        if cop == "Switzerland" or cop == "Schweiz":
            encops.append("Switzerland")
            decops.append("Schweiz")
            frcops.append("Suisse")
        if cop == "Syria" or cop == "Syrien":
            encops.append("Syria")
            decops.append("Syrien")
            frcops.append("Syrie")
        if cop == "Syrian Arab Republic":
            encops.append("Syria")
            decops.append("Syrien")
            frcops.append("Syrie")
        if cop == "Taiwan":
            encops.append("Taiwan (Formosa)")
            decops.append("Taiwan (Formosa)")
            frcops.append("Taïwan (Formose)")
        if cop == "Tajikistan" or cop == "Tadschikistan":
            encops.append("Tajikistan")
            decops.append("Tadschikistan")
            frcops.append("Tadjikistan")
        if cop == "Tansania":
            encops.append("Tanzania (Zanzibar)")
            decops.append("Tansania (Sansibar)")
            frcops.append("Tanzanie (Zanzibar)")
        if cop == "Tanzania":
            encops.append("Tanzania (Zanzibar)")
            decops.append("Tansania (Sansibar)")
            frcops.append("Tanzanie (Zanzibar)")
        if cop == "Thailand":
            encops.append("Thailand")
            decops.append("Thailand")
            frcops.append("Thaïlande")
        if cop == "Tibet":
            encops.append("China")
            decops.append("China")
            frcops.append("Chine")
            enroas.append("Tibet")
            deroas.append("Tibet")#
            frroas.append("Tibet")#
        if cop == "Togo":
            encops.append("Togo")
            decops.append("Togo")
            frcops.append("Togo")
        if cop == "Tokelau":
            encops.append("New Zealand")
            decops.append("Neuseeland")
            frcops.append("Nouvelle-Zélande")
            enroas.append("Tokelau")
            deroas.append("Tokelau")#
            frroas.append("Tokélaou")#
        if cop == "Tonga":
            encops.append("Tonga")
            decops.append("Tonga")
            frcops.append("Tonga")
        if cop == "Trinidad and Tobago" or cop == "Trinidad und Tobago":
            encops.append("Trinidad and Tobago")
            decops.append("Trinidad und Tobago")
            frcops.append("Trinité-et-Tobago")
        if cop == "Tunesia" or cop == "Tunesien" or cop == "Tunisia":
            encops.append("Tunesia")
            decops.append("Tunesia")
            frcops.append("Tunisia")
        if cop == "Turkey" or cop == "Türkei":
            encops.append("Turkey")
            decops.append("Türkei")
            frcops.append("Turquie")
        if cop == "Turkmenistan":
            encops.append("Turkmenistan")
            decops.append("Turkmenistan")
            frcops.append("Turkménistan")
        if cop == "Turks and Caicos Islands":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
            enroas.append("Turks and Caicos Islands")
            deroas.append("Turks- und Caicosinseln")#
            frroas.append("Turks-et-Caïcos (les Îles)")#
        if cop == "Tuvalu":
            encops.append("Tuvalu")
            decops.append("Tuvalu")
            frcops.append("Tuvalu")
        if cop == "Uganda":
            encops.append("Uganda")
            decops.append("Uganda")
            frcops.append("Ouganda")
        if cop == "Ukraine":
            encops.append("Ukraine")
            decops.append("Ukraine")
            frcops.append("Ukraine")
        if cop == "United Arab Emirates" or cop == "Vereinigte Arabische Emirate":
            encops.append("United Arab Emirates")
            decops.append("Vereinigte Arabische Emirate")
            frcops.append("Émirats arabes unis")
        if cop == "United Kingdom":
            encops.append("United Kingdom (UK)")
            decops.append("Vereinigtes Königreich (UK)")
            frcops.append("Royaume-Uni (UK)")
        if cop == "United States Minor Outlying Islands":
            encops.append("United States of America (USA)")
            decops.append("Vereinigte Staaten von Amerika (USA)")
            frcops.append("États-Unis d'Amérique (USA)")
            enroas.append("United States Minor Outlying Islands")
            deroas.append("Kleinere abgelegene Inseln der Vereinigten Staaten")#
            frroas.append("Îles mineures éloignées des États-Unis")#
        if cop == "United States of America" or cop == "Vereinigte Staaten von Amerika (USA)" or cop == "USA" or cop == "United States of America (USA)":
            encops.append("United States of America (USA)")
            decops.append("Vereinigte Staaten von Amerika (USA)")
            frcops.append("États-Unis d'Amérique (USA)")
        if cop == "Uruguay":
            encops.append("Uruguay")
            decops.append("Uruguay")
            frcops.append("Uruguay")
        if cop == "USSR":
            encops.append("Soviet Union (USSR)")
            decops.append("Sowjetunion (SU)")
            frcops.append("Union soviétique (URSS)")
        if cop == "Uzbekistan" or cop == "Usbekistan":
            encops.append("Uzbekistan")
            decops.append("Usbekistan")
            frcops.append("Ouzbékistan")
        if cop == "Vanuatu":
            encops.append("Vanuatu")
            decops.append("Vanuatu")
            frcops.append("Vanuatu")
        if cop == "Vatican" or cop == "Vatikanstadt":
            encops.append("Vatican City")
            decops.append("Vatikanstadt")
            frcops.append("Vatican (État de la Cité du)")
        if cop == "Venezuela":
            encops.append("Venezuela")
            decops.append("Venezuela")
            frcops.append("Venezuela")
        if cop == "Vietnam":
            encops.append("Vietnam")
            decops.append("Vietnam")
            frcops.append("Viêtnam")
        if cop == "Wallis and Futuna":
            encops.append("France")
            decops.append("Frankreich")
            frcops.append("France")
            enroas.append("Wallis and Futuna")
            deroas.append("Wallis und Futuna")#
            frroas.append("Wallis-et-Futuna")#
        if cop == "Western Sahara":
            encops.append("Morocco")
            decops.append("Marokko ")
            frcops.append("Maroc")
            enroas.append("Western Sahara")
            deroas.append("Westsahara")#
            frroas.append("Sahara occidental")#
        if cop == "Yemen":
            encops.append("Yemen")
            decops.append("Jemen")
            frcops.append("Yémen")
        if cop == "Yugoslavia" or cop == "Jugoslawien":
            encops.append("Yugoslavia")
            decops.append("Jugoslawien")
            frcops.append("Yougoslavie")
        if cop == "Zambia" or cop == "Sambia":
            encops.append("Zambia (Northern Rhodesia)")
            decops.append("Sambia (Nordrhodesien)")
            frcops.append("Zambie (Rhodésie du Nord)")
        if cop == "Zanzibar" or cop == "Sansibar":
            encops.append("Tanzania (Zanzibar)")
            decops.append("Tansania (Sansibar)")
            frcops.append("Tanzanie (Zanzibar)")
        if cop == "Zimbabwe" or cop == "Simbabwe":
            encops.append("Zimbabwe (Rhodesia)")
            decops.append("Simbabwe (Rhodesien)")
            frcops.append("Zimbabwe (Rhodésie)")
    encops = list(dict.fromkeys(encops))
    enroas = list(dict.fromkeys(enroas))
    decops = list(dict.fromkeys(decops))
    deroas = list(dict.fromkeys(deroas))
    frcops = list(dict.fromkeys(frcops))
    frroas = list(dict.fromkeys(frroas))
    return encops, decops, frcops, enroas, deroas, frroas

def lang(input):
    if input == "German":
        enlang = "German"
        delang = "Deutsch"        
        frlang = "allemand"
    if input == "Russian":
        enlang = "Russian"
        delang = "Russisch"
        frlang = "russe"
    if input == "English":
        enlang = "English"
        delang = "Englisch"
        frlang = "anglais"
    if input == "French":
        enlang = "French"
        delang = "Französisch"        
        frlang = "français"
    if input == "Vietnamese":
        enlang = "Vietnamese"
        delang = "Vietnamesisch"
        frlang = "vietnamien"
    return enlang, delang, frlang

