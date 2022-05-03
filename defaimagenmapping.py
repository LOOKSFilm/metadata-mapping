import json
import main
import dearpygui.dearpygui as dpg
import login
import mapmodules
import xml.etree.ElementTree as et
from lxml import objectify
from functions import cprint


def run(spaces, mapping):
    file = open(main.filepath, encoding='utf-8')
    cprint('Reading File', "yellow")
    if file != '':
        try:
            global records
            records = json.load(file)
        except:
            dpg.add_text(default_value='ERROR: Can not read file...', parent='console', tracked=True, track_offset=1.0)
    else:
        dpg.add_text(default_value='ERROR: Please select a file', parent='console', tracked=True, track_offset=1.0)
    defafile = "C:/Users/Avid9/Documents/Coding/Flow/Metadata/DEFA/20220118_Metadaten_DEFA_Ausschnittdienst_gesamt.xml"
    cprint('Reading DEFA-File', "yellow")
    if defafile != '':
        global xml
        xml = objectify.fromstring(open(defafile, 'rb').read())
        tree = et.parse(defafile)
        root = tree.findall('filme/DEFAFilm/DEFAFilmId')
        global filmids
        filmids = []
        for item in root:
            filmid = item.text
            filmids.append(filmid)
        persons = tree.findall('personen/DEFAPerson')
        global persondict
        persondict = {}
        for person in persons:
            pid = person.find('DEFAPersonId')
            vorname = person.find('Vorname')
            nachname = person.find('Nachname')
            if vorname.text == None:
                vorname.text = ""
            if nachname.text == None:
                nachname.text = ""
            persondict[pid.text] = vorname.text+" "+nachname.text
    cindex = 0
    global space
    global clips
    reconnects = 0    
    for space in spaces:
        cprint('Mapping '+mapping+' Metadata to '+space)
        clips = login.flow.getMediaSpaceClips(space)
        map(cindex, reconnects)

def map(cindex, reconnects):
    try:
        for i, esclipid in enumerate(clips[cindex:]):
            mappings = dict()
            mappings["custom"] = dict()
            try:
                clipinfo = login.flow.getClipData(esclipid)
                clipname = clipinfo.display_name
                esassetid = clipinfo.asset_id
                escaptureid = clipinfo.capture_id
                try:
                    uuid = clipinfo.data['asset']['uuid']
                except:
                    pass
                cindex = clips.index(esclipid)
                print(space, clipname, clips.index(esclipid))
            except KeyError:
                continue
            
            for record in records:
                clipid = record['Original_Clip_Identifier']
                if clipid == None or clipname == None:
                    pass
                else:
                    try:
                        if clipid in clipname:
                            cprint('Map Data to: '+clipname, "yellow")
                            try:
                                mappings["custom"]["field_50"] = record['Original_Clip_Identifier']
                            except KeyError:
                                pass
                            try:
                                if record['Actor'] != None:
                                    act = mapmodules.tags(record['Actor'])
                                    mappings["custom"]["field_139"] = (", ").join(act)
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_130"] = record['Air_date']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_96"] = record['Aspect_Ratio_']
                            except KeyError:
                                pass
                            try:
                                if record['Camera'] != None:
                                    cam = mapmodules.tags(record['Camera'])
                                    mappings["custom"]["field_136"] = (", ").join(cam)
                            except KeyError:
                                pass
                            try:
                                if record['Cleanfeed'] == 'Yes':
                                    mappings["custom"]["field_86"] = 'true'
                                else:
                                    mappings["custom"]["field_86"] = 'false'
                            except KeyError:
                                pass
                            try:
                                collection = mapmodules.collections(record['Collection'])
                                mappings["custom"]["field_56"] = collection
                            except KeyError:
                                pass
                            try:
                                if record['Colour'] == 'Yes':
                                    mappings["custom"]["field_90"] = 'true'
                                else:
                                    mappings["custom"]["field_90"] = 'false'
                            except KeyError:
                                pass
                            try:                                
                                if record['Comments'] != None and record['Internal_Research'] != None:
                                    mappings["custom"]["field_157"] = record['Comments']+'\n'+record['Internal_Research']
                                if record['Internal_Research'] == None and record['Comments'] != None:
                                    mappings["custom"]["field_157"] =  record['Comments']
                                if record['Comments'] == None and record['Internal_Research'] != None:
                                    mappings["custom"]["field_157"] = record['Internal_Research']
                                if record['Comments'] == None and record['Internal_Research'] == None:
                                    mappings["custom"]["field_157"] = ""
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_143"] = record['Commissioner']
                            except KeyError:
                                pass
                            try:
                                if record['Composer'] != None:
                                    composer = mapmodules.tags(record['Composer'])
                                    mappings["custom"]["field_138"] = (", ").join(composer)
                            except:
                                pass
                            try:
                                if record['Country'] != None:
                                    encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(record['Country'])
                                    mappings["custom"]["field_179"] = encops #nur EN, noch übersetzen (074a+c), Multiselect-Feld
                                    mappings["custom"]["field_178"] = decops
                                    mappings["custom"]["field_180"] = frcops   
                            except KeyError:
                                pass
                            try:
                                if record['Country_of_Production'] != None:
                                    encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(record['Country_of_Production'])
                                    mappings["custom"]["field_176"] = encops
                                    mappings["custom"]["field_175"] = decops
                                    mappings["custom"]["field_177"] = frcops
                                    mappings["custom"]["field_182"] = (", ").join(enroas)
                                    mappings["custom"]["field_181"] = (", ").join(deroas)
                                    mappings["custom"]["field_183"] = (", ").join(frroas)
                                if record['Produktionsland'] != None:
                                    encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(record['Produktionsland'])
                                    mappings["custom"]["field_176"] = encops
                                    mappings["custom"]["field_175"] = decops
                                    mappings["custom"]["field_177"] = frcops
                                    mappings["custom"]["field_182"] = (", ").join(enroas)
                                    mappings["custom"]["field_181"] = (", ").join(deroas)
                                    mappings["custom"]["field_183"] = (", ").join(frroas)
                            except KeyError:
                                pass
                            try:
                                decade = mapmodules.decade(record['Decade'])
                                mappings["custom"]["field_133"] = decade
                            except KeyError:
                                pass
                            try:
                                if record['Digitised'] == 'Yes':
                                    mappings["custom"]["field_91"] = 'true'
                                else:
                                    mappings["custom"]["field_91"] = 'false'
                            except KeyError:
                                pass
                            try:
                                if record['Director'] != None:
                                    director = mapmodules.tags(record['Director'])
                                    mappings["custom"]["field_135"] = (", ").join(director)
                            except KeyError:
                                pass
                            try:
                                if record['Editor'] != None:
                                    editor = mapmodules.tags(record["Editor"])
                                    mappings["custom"]["field_142"] = (", ").join(editor)
                            except KeyError:
                                pass
                            try:
                                if record['English_Shotlist'] != None:
                                    mappings["custom"]["field_188"] = record['English_Shotlist']
                                else:
                                    mappings["custom"]["field_188"] = ""
                            except KeyError:
                                pass
                            try:
                                if record['English_Summary'] != None:
                                    mappings["custom"]["field_125"] = record['English_Summary']
                                else:
                                    mappings["custom"]["field_125"] = ""
                            except KeyError:
                                pass
                            try:
                                if record['English_Tags'] != None:
                                    tags = mapmodules.tags(record['English_Tags'])
                                    mappings["custom"]["field_190"] = (", ").join(tags)
                            except KeyError:
                                pass
                            try:
                                if record['Original_Title_English'] != None:
                                    mappings["custom"]["field_65"] = str(record['Original_Title_English'])
                                elif record['English_Title'] != None:
                                    mappings["custom"]["field_65"] = record['English_Title']
                                else:
                                    mappings["custom"]["field_65"] = ""
                            except KeyError:                                            
                                pass
                            try:
                                mappings["custom"]["field_99"] = record['Exploitation_restrictions']
                            except KeyError:
                                pass
                            try:
                                if record['Field84'] != None:
                                    personalities = mapmodules.tags(record['Field84'])
                                    mappings["custom"]["field_194"] = (", ").join(personalities)
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_145"] = record['Filmstudio']
                            except KeyError:
                                pass
                            try:
                                origformat = mapmodules.format(record['Format_of_original'])
                                mappings["custom"]["field_93"] = origformat
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_189"] = record['French_Shotlist']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_187"] = record['French_summary']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_191"] = record['French_Tags']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_66"] = record['French_Title']
                            except KeyError:
                                pass
                            try:
                                engenre, degenre, frgenre, status = mapmodules.genre(record['Genre'])
                                mappings["custom"]["field_192"] = engenre
                                mappings["custom"]["field_153"] = degenre
                                mappings["custom"]["field_193"] = frgenre
                                mappings["custom"]["field_230"] = status
                            except KeyError:
                                pass
                            if reconnects >= 2:
                                with open("C:/Users/Avid9/Documents/Coding/Flow/tools/BetterMapper/mappingErrors.txt", 'a') as f:
                                    f.write(str(clipname)+" "+str(cindex)+"\n")
                                f.close()
                            else:
                                try:
                                    mappings["custom"]["field_149"] = record['German_Shotlist']
                                except KeyError:
                                    pass
                            try:
                                mappings["custom"]["field_147"] = record['German_Summary']
                            except KeyError:
                                pass
                            try:
                                if record['German_Tags'] != None:
                                    detags = mapmodules.tags(record['German_Tags'])
                                    mappings["custom"]["field_151"] = (", ").join(detags)
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_64"] = record['German_Title']
                            except KeyError:
                                pass
                            try:
                                if record['Head_of_Production'] != None:
                                    head = mapmodules.tags(record['Head_of_Production'])
                                    mappings["custom"]["field_141"] = (", ").join(head)
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_52"] = record['Internal_Identifier']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_94"] = record['Location_of_Original']
                            except KeyError:
                                pass
                            try:
                                if record['Nationality'] != None:
                                    ennat, denat, frnat, nn, nn2, nn3 = mapmodules.countries(record['Nationality'])
                                    mappings["custom"]["field_123"] = ennat
                                    mappings["custom"]["field_122"] = denat
                                    mappings["custom"]["field_124"] = frnat
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_100"] = record['Notes_on_exploitation_restrictions']
                            except KeyError:
                                pass
                            try:
                                digiformat = mapmodules.format(record['Original_format_of_digitalization'])
                                mappings["custom"]["field_92"] = digiformat
                            except KeyError:
                                pass
                            try:
                                if record['Original_Language_Film'] != None:
                                    if record['Original_Language_Film'] != "Mute":
                                        enlang, delang, frlang = mapmodules.lang(record['Original_Language_Film'])
                                        mappings["custom"]["field_80"] = enlang
                                        mappings["custom"]["field_226"] = delang
                                        mappings["custom"]["field_227"] = frlang
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_148"] = record['Original_Summary']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_65"] = record['Original_Tilte_English']
                            except KeyError:
                                pass
                            try:
                                if record['Original_Title_in_Original_Language'] != None:
                                    mappings["custom"]["field_63"] = record['Original_Title_in_Original_Language'].strip()
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_67"] = record['Other_title']
                            except KeyError:
                                pass
                            try:
                                if record['Personalities'] != None:
                                    person = mapmodules.tags(record['Personalities'])
                                    mappings["custom"]["field_155"] = (", ").join(person)
                            except KeyError:
                                pass
                            try:
                                if record['Personalities_FR'] != None:
                                    personfr = mapmodules.tags(record['Personalities_FR'])
                                    mappings["custom"]["field_195"] = (", ").join(personfr)
                            except KeyError:
                                pass
                            try:
                                if record['Personalities_secondary'] != None:
                                    pers2 = mapmodules.tags(record['Personalities_secondary'])
                                    mappings["custom"]["field_156"] = (", ").join(pers2)
                            except KeyError:
                                pass
                            try:
                                if record['Photographer'] != None:
                                    photo = mapmodules.tags(record['Photographer'])
                                    mappings["custom"]["field_137"] = (", ").join(photo)
                            except KeyError:
                                pass
                            try:
                                if record['Producer'] != None:
                                    prod = mapmodules.tags(record['Producer'])
                                    mappings["custom"]["field_140"] = (", ").join(prod)
                            except KeyError:
                                pass
                            try:
                                if record['Production_Year'] != None:
                                    try:
                                        mappings["custom"]["field_232"] = int(record['Production_Year'])
                                    except ValueError:
                                        year = record['Production_Year'].split("/")
                                        mappings["custom"]["field_232"] = int(year[-1])
                            except KeyError:
                                pass
                            try:
                                if record['Region_English'] != None:
                                    encit = mapmodules.tags(record['Region_English'])
                                    mappings["custom"]["field_185"] = (", ").join(encit)
                            except KeyError:
                                pass
                            try:
                                if record['Region_French'] != None:
                                    frcit = mapmodules.tags(record['Region_French'])
                                    mappings["custom"]["field_186"] = (", ").join(frcit)
                            except KeyError:
                                pass
                            try:
                                if record['Region_German'] != None:
                                    decit = mapmodules.tags(record['Region_German'])
                                    mappings["custom"]["field_184"] = (", ").join(decit)
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_95"] = record['Resolution']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_98"] = record['Rights_owner']
                            except KeyError:
                                pass
                            try:
                                if record['S2T_English'] == "Yes":
                                    mappings["custom"]["field_109"] = "true"
                                    mappings["custom"]["field_112"] = "Azure"
                                if record['S2T_German'] == "Yes":
                                    mappings["custom"]["field_108"] = "true"
                                    mappings["custom"]["field_112"] = "Azure"
                                if record['Speechmatics_English'] == "Yes":
                                    mappings["custom"]["field_109"] = "true"
                                    mappings["custom"]["field_112"] = "Speechmatics"
                                if record['Speechmatics_German'] == "Yes":
                                    mappings["custom"]["field_108"] = "true"
                                    mappings["custom"]["field_112"] = "Speechmatics"
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_108"] = record['']
                            except KeyError:
                                pass
                            try:
                                if record['S2T_German_check'] == "Yes":
                                    mappings["custom"]["field_111"] = "true"
                                else:
                                    mappings["custom"]["field_111"] = "false"
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_132"] = record['Shoot_Date']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_48"] = record['Shoot_Year_']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_85"] = record['Synchronisation']
                            except KeyError:
                                pass
                            try:
                                if record['Sound'] == 'Yes':
                                    mappings["custom"]["field_89"] = 'true'
                                else:
                                    mappings["custom"]["field_89"] = 'false'
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_55"] = record['Source']
                                accid = mapmodules.accid(record['Source'])
                                mappings["custom"]["field_171"] = accid
                            except KeyError:
                                pass
                            try:
                                user = mapmodules.usergroups(record['User_Group'])
                                mappings["custom"]["field_54"] = user
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_144"] = record['Synchro_Studio']
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_53"] = record['Tape_Can_Box']
                            except KeyError:
                                pass
                            try:
                                if record['Third_Party_Rights'] != None:
                                    if record['Third_Party_Rights'] == "No":
                                        mappings["custom"]["field_101"] = "false"
                                    else:
                                        mappings["custom"]["field_101"] = "true"
                                else:
                                    mappings["custom"]["field_101"] = ""
                            except KeyError:
                                pass
                            try:
                                mappings["custom"]["field_51"] = 'true'
                            except KeyError:
                                pass
                            mappings["custom"]["field_231"] = esclipid
                            mappings["custom"]["field_233"] = esassetid
                            mappings["custom"]["field_235"] = escaptureid
                            mappings["custom"]["field_127"] = uuid
                        else:
                            pass
                            #cprint(clipname+' not found in file')
                    except KeyError:
                        pass
            data = json.dumps(mappings)
            r = login.flow.updateAsset(esassetid, data)
            print(r.text)
            for i, filmid in enumerate(filmids):
                if filmid in clipname:
                    if xml.filme.DEFAFilm[i].Anlaufdatum != None:
                        mappings["custom"]["field_130"] = str(xml.filme.DEFAFilm[i].Anlaufdatum)
                    if xml.filme.DEFAFilm[i].Bestand != None:
                        mappings["custom"]["field_221"] = str(xml.filme.DEFAFilm[i].Bestand)
                        collection = mapmodules.collections(str(xml.filme.DEFAFilm[i].Bestand))
                        mappings["custom"]["field_56"] = collection
                    try:
                        if xml.filme.DEFAFilm[i].Produktionen.DEFAAuftraggeberProduktion.Firma != None:
                            mappings["custom"]["field_145"] = str(xml.filme.DEFAFilm[i].Produktionen.DEFAAuftraggeberProduktion.Firma)
                    except:
                        pass
                    if xml.filme.DEFAFilm[i].DEFAFilmId != None:
                        mappings["custom"]["field_220"] = str(xml.filme.DEFAFilm[i].DEFAFilmId)
                        mappings["custom"]["field_52"] = str(xml.filme.DEFAFilm[i].DEFAFilmId)
                    if xml.filme.DEFAFilm[i].Drehort != None:
                        locations = mapmodules.tags(str(xml.filme.DEFAFilm[i].Drehort))
                        mappings["custom"]["field_184"] = (", ").join(locations)
                    if xml.filme.DEFAFilm[i].Farbe != None:
                        if str(xml.filme.DEFAFilm[i].Farbe) == "fa" or str(xml.filme.DEFAFilm[i].Farbe) == "fa/sw":
                            mappings["custom"]["field_90"] = "true"
                        else:
                            mappings["custom"]["field_90"] = "false"
                    if xml.filme.DEFAFilm[i].FilmVideoFormat != None:
                        format = mapmodules.format(str(xml.filme.DEFAFilm[i].FilmVideoFormat))
                        mappings["custom"]["field_93"] = format
                    try:
                        filmpersonen = xml.filme.DEFAFilm[i].FilmPersonen.DEFAFilmperson
                        darsteller = {}
                        kamera = []
                        komponist = []
                        regie = []
                        schnitt = []
                        pl = []
                        per1 = []
                        per2 = []
                        produzent = []
                        photograph = []
                        syncautor = []
                        drehbuch = []
                        syncregie = []
                        sprecher = []
                        musik = []
                        syncschnitt = []
                        regieass = []
                        syncmusik = []
                        syncton = []
                        szenenbild = []
                        beratung = []
                        maske = []
                        ton = []
                        kostüm = []
                        Aufnahmeleitung = []
                        Dramaturgie = []
                        Requisite = []
                        Kameraassistenz = []
                        Redaktion = []
                        Text = []
                        Gestaltung = []
                        Szenarium = []
                        Animation = [] 
                        Interview = []
                        Moderation = []
                        for filmperson in filmpersonen:
                            typ = str(filmperson.Typ)
                            #print(typ)
                            pid = str(filmperson.DEFAPersonId)
                            rolle = str(filmperson.RolleMusiktitel)
                            if typ == "Darsteller":
                                if filmperson.Anzeigereihenfolge != None:
                                    if rolle != "None":
                                        darsteller[filmperson.Anzeigereihenfolge] = (persondict[pid]+" ("+rolle+")")
                                    else:
                                        darsteller[filmperson.Anzeigereihenfolge] = (persondict[pid])
                                else:
                                    darsteller = persondict[pid]
                            if typ == "Kamera":
                                kamera.append(persondict[pid])
                            if typ == "Musikinterpret":
                                komponist.append(persondict[pid])
                            if typ == "Regie":
                                regie.append(persondict[pid])
                            if typ == "Schnitt":
                                schnitt.append(persondict[pid])
                            if typ == "Produktionsleitung":
                                pl.append(persondict[pid])
                            if typ == "Person, primär":
                                per1.append(persondict[pid])
                            if typ == "Produzent":
                                produzent.append(persondict[pid])
                            if typ == "DEFA-Fotograf":
                                photograph.append(persondict[pid])
                            if typ == "Person, sekundär":
                                per2.append(persondict[pid])
                            if typ == "Synchronisation (Autor)":
                                syncautor.append(persondict[pid]) 
                            if typ == "Drehbuch": 
                                drehbuch.append(persondict[pid]) 
                            if typ == "Synchronisation (Regie)":
                                syncregie.append(persondict[pid])  
                            if typ == "Synchronisation (Sprecher)" or typ == "Sprecher":
                                sprecher.append(persondict[pid]) 
                            if typ == "Musik":
                                musik.append(persondict[pid])  
                            if typ == "Synchronisation (Schnitt)":
                                syncschnitt.append(persondict[pid])  
                            if typ == "Regieassistenz":
                                regieass.append(persondict[pid]) 
                            if typ == "Synchronisation (Ton)": 
                                syncton.append(persondict[pid]) 
                            if typ == "Synchronisation (Musik)": 
                                syncmusik.append(persondict[pid])
                            if typ == "Szenenbild":
                                szenenbild.append(persondict[pid]) 
                            if typ == "Beratung":
                                beratung.append(persondict[pid]) 
                            if typ == "Maske":
                                maske.append(persondict[pid]) 
                            if typ == "Ton":
                                ton.append(persondict[pid]) 
                            if typ == "Kostüm":
                                kostüm.append(persondict[pid]) 
                            if typ == "Aufnahmeleitung":
                                Aufnahmeleitung.append(persondict[pid]) 
                            if typ == "Dramaturgie" or typ == "Dramaturg": 
                                Dramaturgie.append(persondict[pid])
                            if typ == "Requisite":
                                Requisite.append(persondict[pid])
                            if typ == "Kameraassistenz" or typ == "Kamerassistent": 
                                Kameraassistenz.append(persondict[pid])
                            if typ == "Redaktion": 
                                Redaktion.append(persondict[pid])
                            if typ == "Text": 
                                Text.append(persondict[pid])
                            if typ == "Gestaltung": 
                                Gestaltung.append(persondict[pid])
                            if typ == "Szenarium": 
                                Szenarium.append(persondict[pid])
                            if typ == "Animation": 
                                Animation.append(persondict[pid])
                            if typ == "Interview": 
                                Interview.append(persondict[pid])
                            if typ == "Moderation":
                                Moderation.append(persondict[pid])
                        andere = ""
                        if Moderation:
                            andere += "Moderation: "+(", ").join(Moderation)+"\n"
                        if Aufnahmeleitung:
                            andere += "Aufnahmeleitung: "+(", ").join(Aufnahmeleitung)+"\n"
                        if drehbuch:
                            andere += "Drehbuch: "+(", ").join(drehbuch)+"\n"
                        if Dramaturgie:
                            andere += "Dramaturgie: "+(", ").join(Dramaturgie)+"\n"
                        if regieass:
                            andere += "Synchronisation (Autor): "+(", ").join(regieass)+"\n"
                        if Redaktion:
                            andere += "Redaktion: "+(", ").join(Redaktion)+"\n"
                        if Text:
                            andere += "Text: "+(", ").join(Text)+"\n"
                        if Kameraassistenz:
                            andere += "Kameraassistenz: "+(", ").join(Kameraassistenz)+"\n"
                        if ton:
                            andere += "Ton: "+(", ").join(ton)+"\n"
                        if musik:
                            andere += "Musik: "+(", ").join(musik)+"\n"
                        if Animation:
                            andere += "Animation: "+(", ").join(Animation)+"\n"
                        if Szenarium:
                            andere += "Szenarium: "+(", ").join(Szenarium)+"\n"
                        if szenenbild:
                            andere += "Szenenbild: "+(", ").join(szenenbild)+"\n"
                        if Requisite:
                            andere += "Requisite: "+(", ").join(Requisite)+"\n"
                        if Gestaltung:
                            andere += "Gestaltung: "+(", ").join(Gestaltung)+"\n"
                        if maske:
                            andere += "Maske: "+(", ").join(maske)+"\n"
                        if kostüm:
                            andere += "Kostüm: "+(", ").join(kostüm)+"\n"
                        if beratung:
                            andere += "Beratung: "+(", ").join(beratung)+"\n"
                        if Interview:
                            andere += "Interview: "+(", ").join(Interview)+"\n"
                        if syncregie:
                            andere += "Synchronisation (Autor): "+(", ").join(syncregie)+"\n"
                        if syncautor:
                            andere += "Synchronisation (Autor): "+(", ").join(syncautor)+"\n"
                        if sprecher:
                            andere += "Synchronisation (Autor): "+(", ").join(sprecher)+"\n"
                        if syncton:
                            andere += "Synchronisation (Autor): "+(", ").join(syncton)+"\n"
                        if syncmusik:
                            andere += "Synchronisation (Autor): "+(", ").join(syncmusik)+"\n"
                        if syncschnitt:
                            andere += "Synchronisation (Autor): "+(", ").join(syncschnitt)+"\n"
                        sorteddarsteller = {}
                        for d in sorted(darsteller):
                            sorteddarsteller[d] = darsteller[d]
                        mappings["custom"]["field_139"] = (", ").join(sorteddarsteller.values())
                        mappings["custom"]["field_136"] = (", ").join(kamera)
                        mappings["custom"]["field_138"] = (", ").join(komponist)
                        mappings["custom"]["field_135"] = (", ").join(regie)
                        mappings["custom"]["field_142"] = (", ").join(schnitt)
                        mappings["custom"]["field_141"] = (", ").join(pl)
                        mappings["custom"]["field_155"] = (", ").join(per1)
                        mappings["custom"]["field_140"] = (", ").join(produzent)
                        mappings["custom"]["field_156"] = (", ").join(per2)
                        mappings["custom"]["field_137"] = (", ").join(photograph)
                        mappings["custom"]["field_146"] = andere
                    except:
                        pass
                    if xml.filme.DEFAFilm[i].Genre != None:
                        mappings["custom"]["field_154"] = str(xml.filme.DEFAFilm[i].Genre)
                    if xml.filme.DEFAFilm[i].HerstellungsjahrBis != None:
                        if xml.filme.DEFAFilm[i].HerstellungsjahrBis != "":
                            try:
                                dif = int(xml.filme.DEFAFilm[i].HerstellungsjahrBis) - int(xml.filme.DEFAFilm[i].HerstellungsjahrVon)
                            except ValueError:
                                bis = str(xml.filme.DEFAFilm[i].HerstellungsjahrBis).split("/")
                                von = str(xml.filme.DEFAFilm[i].HerstellungsjahrVon).split("/")
                                dif = int(bis[-1]) - int(von[0]) 
                            if dif <= 10:
                                mappings["custom"]["field_232"] = str(str(xml.filme.DEFAFilm[i].HerstellungsjahrVon)+" - "+str(xml.filme.DEFAFilm[i].HerstellungsjahrBis))
                            else:
                                try:
                                    mappings["custom"]["field_232"] = int(xml.filme.DEFAFilm[i].HerstellungsjahrVon)
                                except ValueError:
                                    von = str(xml.filme.DEFAFilm[i].HerstellungsjahrVon).split("/")
                                    mappings["custom"]["field_232"] = int(von[-1])
                        else:
                            try:
                                if xml.filme.DEFAFilm[i].HerstellungsjahrVon != None:
                                    mappings["custom"]["field_232"] = int(xml.filme.DEFAFilm[i].HerstellungsjahrVon)
                                else:
                                    pass
                            except ValueError:
                                von = str(xml.filme.DEFAFilm[i].HerstellungsjahrVon).split("/")
                                mappings["custom"]["field_232"] = int(von[-1])
                    if xml.filme.DEFAFilm[i].InhaltEnglisch != None:
                        mappings["custom"]["field_125"] = str(xml.filme.DEFAFilm[i].InhaltEnglisch)
                    if xml.filme.DEFAFilm[i].Kurzinhalt != None:
                        mappings["custom"]["field_147"] = str(xml.filme.DEFAFilm[i].Kurzinhalt)
                    if reconnects >= 2:
                        with open("C:/Users/Avid9/Documents/Coding/Flow/tools/BetterMapper/mappingErrors.txt", 'a') as f:
                            f.write(str(clipname)+" "+str(cindex)+"\n")
                        f.close()
                        reconnects = 0
                    elif xml.filme.DEFAFilm[i].Langinhalt != None:
                        mappings["custom"]["field_149"] = str(xml.filme.DEFAFilm[i].Langinhalt)
                    if xml.filme.DEFAFilm[i].ModifyDate != None:
                        mappings["custom"]["field_61"] = str(xml.filme.DEFAFilm[i].ModifyDate)
                    if xml.filme.DEFAFilm[i].Produktionsland != None:
                        encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(str(xml.filme.DEFAFilm[i].Produktionsland))
                        mappings["custom"]["field_176"] = encops
                        mappings["custom"]["field_175"] = decops
                        mappings["custom"]["field_177"] = frcops
                        mappings["custom"]["field_182"] = (", ").join(enroas)
                        mappings["custom"]["field_181"] = (", ").join(deroas)
                        mappings["custom"]["field_183"] = (", ").join(frroas)
                    if xml.filme.DEFAFilm[i].Schlagworte != None:
                        tags = mapmodules.tags(str(xml.filme.DEFAFilm[i].Schlagworte))
                        mappings["custom"]["field_151"] = (", ").join(tags)
                    if xml.filme.DEFAFilm[i].SyncStudio != None:
                        mappings["custom"]["field_144"] = str(xml.filme.DEFAFilm[i].SyncStudio)
                    if xml.filme.DEFAFilm[i].TitelEnglisch != None:
                        mappings["custom"]["field_65"] = str(xml.filme.DEFAFilm[i].TitelEnglisch)
                    if xml.filme.DEFAFilm[i].TitelOriginalArchiv != None:
                        mappings["custom"]["field_63"] = str(xml.filme.DEFAFilm[i].TitelOriginalArchiv)
                    if xml.filme.DEFAFilm[i].TitelSonstige != None:
                        mappings["custom"]["field_67"] = str(xml.filme.DEFAFilm[i].TitelSonstige)
                    if xml.filme.DEFAFilm[i].TitelVerleihDeutsch != None:
                        mappings["custom"]["field_64"] = str(xml.filme.DEFAFilm[i].TitelVerleihDeutsch)
                    mappings["custom"]["field_231"] = esclipid
                    mappings["custom"]["field_233"] = esassetid
                    mappings["custom"]["field_235"] = escaptureid
                    mappings["custom"]["field_127"] = uuid
        data = json.dumps(mappings)
        r = login.flow.updateAsset(esassetid, data)
        print(r.text)
        cprint('------------------ MAPPING DONE ----------------------------')
    except:
        reconnects += 1
        conn = False
        cprint("Lost connection to ES", "red")
        while conn == False:
            try:
                login.flow.ping()
                conn = True
                cprint("Connected")
                map(cindex, reconnects)
            except:
                cprint("Trying to reconnect...", "yellow")
                pass
        

