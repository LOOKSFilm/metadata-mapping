import main
import dearpygui.dearpygui as dpg
import login
import mapmodules
import xml.etree.ElementTree as et
from lxml import objectify
from EditShareAPI import FlowMetadata
import requests
from functions import cprint, mapfield


def run(spaces, mapping):
    file = main.filepath
    cprint('Reading File')
    if file != '':
        #try:
        xml = objectify.fromstring(open(file, 'rb').read())
        tree = et.parse(file)
        root = tree.findall('filme/DEFAFilm/DEFAFilmId')
        filmids = []
        for item in root:
            filmid = item.text
            filmids.append(filmid)
        persons = tree.findall('personen/DEFAPerson')
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
    else:
        dpg.add_text(default_value='ERROR: Please select a file', parent='console', tracked=True, track_offset=1.0)
    print(spaces)
    for space in spaces:
        cprint('Mapping '+mapping+' Metadata to '+space)
        clips = login.flow.getMediaSpaceClips(space)
        for esclipid in clips:
            try:
                clipinfo = login.flow.getClipData(esclipid)
                clipname = clipinfo.display_name
                esassetid = clipinfo.asset_id
                escaptureid = clipinfo.capture_id
                try:
                    uuid = clipinfo.data['asset']['uuid']
                except:
                    pass
                print(clipname, clips.index(esclipid))
            except KeyError:
                continue
            try:
                for i, filmid in enumerate(filmids):
                    if filmid in clipname:
                        if xml.filme.DEFAFilm[i].Anlaufdatum != None:
                            mapfield("field_130", str(xml.filme.DEFAFilm[i].Anlaufdatum), esassetid)
                        if xml.filme.DEFAFilm[i].Bestand != None:
                            mapfield("field_221", str(xml.filme.DEFAFilm[i].Bestand), esassetid)
                            collection = mapmodules.collections(str(xml.filme.DEFAFilm[i].Bestand))
                            mapfield("field_56", collection, esassetid)
                        try:
                            if xml.filme.DEFAFilm[i].Produktionen.DEFAAuftraggeberProduktion.Firma != None:
                                mapfield("field_145", str(xml.filme.DEFAFilm[i].Produktionen.DEFAAuftraggeberProduktion.Firma), esassetid)
                        except:
                            pass
                        if xml.filme.DEFAFilm[i].DEFAFilmId != None:
                            mapfield("field_220", str(xml.filme.DEFAFilm[i].DEFAFilmId), esassetid)
                            mapfield("field_52", str(xml.filme.DEFAFilm[i].DEFAFilmId), esassetid)
                        if xml.filme.DEFAFilm[i].Drehort != None:
                            locations = mapmodules.tags(str(xml.filme.DEFAFilm[i].Drehort))
                            mapfield("field_184", (" ,").join(locations), esassetid)
                        if xml.filme.DEFAFilm[i].Farbe != None:
                            if str(xml.filme.DEFAFilm[i].Farbe) == "fa" or str(xml.filme.DEFAFilm[i].Farbe) == "fa/sw":
                                mapfield("field_90", "true", esassetid)
                            else:
                                mapfield("field_90", "false", esassetid)
                        if xml.filme.DEFAFilm[i].FilmVideoFormat != None:
                            format = mapmodules.format(str(xml.filme.DEFAFilm[i].FilmVideoFormat))
                            mapfield("field_93", format, esassetid)
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
                            mapfield("field_139", (", ").join(sorteddarsteller.values()), esassetid)
                            mapfield("field_136", (", ").join(kamera), esassetid)
                            mapfield("field_138", (", ").join(komponist), esassetid)
                            mapfield("field_135", (", ").join(regie), esassetid)
                            mapfield("field_142", (", ").join(schnitt), esassetid)
                            mapfield("field_141", (", ").join(pl), esassetid)
                            mapfield("field_155", (", ").join(per1), esassetid)
                            mapfield("field_140", (", ").join(produzent), esassetid)
                            mapfield("field_156", (", ").join(per2), esassetid)
                            mapfield("field_137", (", ").join(photograph), esassetid)
                            mapfield("field_146", andere, esassetid)
                        except:
                            pass
                        if xml.filme.DEFAFilm[i].Genre != None:
                            mapfield("field_154", str(xml.filme.DEFAFilm[i].Genre), esassetid)
                        if xml.filme.DEFAFilm[i].HerstellungsjahrBis != None:
                            if xml.filme.DEFAFilm[i].HerstellungsjahrBis != "":
                                try:
                                    dif = int(xml.filme.DEFAFilm[i].HerstellungsjahrBis) - int(xml.filme.DEFAFilm[i].HerstellungsjahrVon)
                                except ValueError:
                                    bis = str(xml.filme.DEFAFilm[i].HerstellungsjahrBis).split("/")
                                    von = str(xml.filme.DEFAFilm[i].HerstellungsjahrVon).split("/")
                                    dif = int(bis[-1]) - int(von[0]) 
                                if dif <= 10:
                                    mapfield("field_232", str(str(xml.filme.DEFAFilm[i].HerstellungsjahrVon)+" - "+str(xml.filme.DEFAFilm[i].HerstellungsjahrBis)), esassetid)
                                else:
                                    try:
                                        mapfield("field_232", int(xml.filme.DEFAFilm[i].HerstellungsjahrVon), esassetid)
                                    except ValueError:
                                        von = str(xml.filme.DEFAFilm[i].HerstellungsjahrVon).split("/")
                                        mapfield("field_232", int(von[-1]), esassetid)
                            else:
                                try:
                                    if xml.filme.DEFAFilm[i].HerstellungsjahrVon != None:
                                        mapfield("field_232", int(xml.filme.DEFAFilm[i].HerstellungsjahrVon), esassetid)
                                    else:
                                        pass
                                except ValueError:
                                    von = str(xml.filme.DEFAFilm[i].HerstellungsjahrVon).split("/")
                                    mapfield("field_232", int(von[-1]), esassetid)
                        if xml.filme.DEFAFilm[i].InhaltEnglisch != None:
                            mapfield("field_125", str(xml.filme.DEFAFilm[i].InhaltEnglisch), esassetid)
                        if xml.filme.DEFAFilm[i].Kurzinhalt != None:
                            mapfield("field_147", str(xml.filme.DEFAFilm[i].Kurzinhalt), esassetid)
                        if xml.filme.DEFAFilm[i].Langinhalt != None:
                            mapfield("field_149", str(xml.filme.DEFAFilm[i].Langinhalt), esassetid)
                        if xml.filme.DEFAFilm[i].ModifyDate != None:
                            mapfield("field_61", str(xml.filme.DEFAFilm[i].ModifyDate), esassetid)
                        if xml.filme.DEFAFilm[i].Produktionsland != None:
                            encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(str(xml.filme.DEFAFilm[i].Produktionsland))
                            mapfield("field_176", encops, esassetid)
                            mapfield("field_175", decops, esassetid)
                            mapfield("field_177", frcops, esassetid)
                            mapfield("field_182", (", ").join(enroas), esassetid)
                            mapfield("field_181", (", ").join(deroas), esassetid)
                            mapfield("field_183", (", ").join(frroas), esassetid)
                        if xml.filme.DEFAFilm[i].Schlagworte != None:
                            tags = mapmodules.tags(str(xml.filme.DEFAFilm[i].Schlagworte))
                            mapfield("field_151", (", ").join(tags), esassetid)
                        if xml.filme.DEFAFilm[i].SyncStudio != None:
                            mapfield("field_144", str(xml.filme.DEFAFilm[i].SyncStudio), esassetid)
                        if xml.filme.DEFAFilm[i].TitelEnglisch != None:
                            mapfield("field_65", str(xml.filme.DEFAFilm[i].TitelEnglisch), esassetid)
                        if xml.filme.DEFAFilm[i].TitelOriginalArchiv != None:
                            mapfield("field_63", str(xml.filme.DEFAFilm[i].TitelOriginalArchiv), esassetid)
                        if xml.filme.DEFAFilm[i].TitelSonstige != None:
                            mapfield("field_67", str(xml.filme.DEFAFilm[i].TitelSonstige), esassetid)
                        if xml.filme.DEFAFilm[i].TitelVerleihDeutsch != None:
                            mapfield("field_64", str(xml.filme.DEFAFilm[i].TitelVerleihDeutsch), esassetid)
                        mapfield("field_231", esclipid, esassetid)
                        mapfield("field_233", esassetid, esassetid)
                        mapfield("field_235", escaptureid, esassetid)
                        mapfield("field_127", uuid, esassetid)
            except requests.exceptions.ConnectionError:
                conn = False
                while conn == False:
                    try:
                        flow = FlowMetadata("10.0.77.14", "christoph", "looksfilm")
                        if flow.connection != "true":
                            conn = False
                        else:
                            conn = True
                            print("Connected")
                    except:
                        cprint("Lost connection to ES")
    cprint('------------------ MAPPING DONE ----------------------------')