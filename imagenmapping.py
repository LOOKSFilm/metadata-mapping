import json
import main
import requests
import dearpygui.dearpygui as dpg
import login
from functions import pretty, cprint, ctabprint, mapfield
import mapmodules
from EditShareAPI import FlowMetadata


def run(spaces, mapping):
    file = open(main.filepath, encoding='utf-8')
    cprint('Reading File')
    if file != '':
        try:
            records = json.load(file)
        except:
            dpg.add_text(default_value='ERROR: Can not read file...', parent='console', tracked=True, track_offset=1.0)
    else:
        dpg.add_text(default_value='ERROR: Please select a file', parent='console', tracked=True, track_offset=1.0)
    for space in spaces:
        cprint('Mapping '+mapping+' Metadata to '+space)
        clips = login.flow.getMediaSpaceClips(space)
        for i, esclipid in enumerate(clips):
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
                for record in records:
                    clipid = record['Original_Clip_Identifier']
                    if clipid == None or clipname == None:
                        pass
                    else:
                        try:
                            if clipid in clipname:
                                cprint('Map Data to: '+clipname)
                                try:
                                    mapfield("field_50", record['Original_Clip_Identifier'], esassetid) #>>> print '12'.zfill(5) > 00012 (für DEFA00000)
                                except KeyError:
                                    pass
                                try:
                                    if record['Actor'] != None:
                                        act = mapmodules.tags(record['Actor'])
                                        mapfield("field_139", (", ").join(act), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_130", record['Air_date'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_96", record['Aspect_Ratio_'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Camera'] != None:
                                        cam = mapmodules.tags(record['Camera'])
                                        mapfield("field_136", (", ").join(cam), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Cleanfeed'] == 'Yes':
                                        mapfield("field_86", 'true', esassetid)
                                    else:
                                        mapfield("field_86", 'false', esassetid)
                                except KeyError:
                                    pass
                                try:
                                    collection = mapmodules.collections(record['Collection'])
                                    mapfield("field_56", collection, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Colour'] == 'Yes':
                                        mapfield("field_90", 'true', esassetid)
                                    else:
                                        mapfield("field_90", 'false', esassetid)
                                except KeyError:
                                    pass
                                try:                                
                                    if record['Comments'] != None and record['Internal_Research'] != None:
                                        mapfield("field_157", record['Comments']+'\n'+record['Internal_Research'], esassetid) 
                                    if record['Internal_Research'] == None and record['Comments'] != None:
                                        mapfield("field_157", record['Comments'], esassetid)
                                    if record['Comments'] == None and record['Internal_Research'] != None:
                                        mapfield("field_157", record['Internal_Research'], esassetid)
                                    if record['Comments'] == None and record['Internal_Research'] == None:
                                        mapfield("field_157", "", esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_143", record['Commissioner'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Composer'] != None:
                                        composer = mapmodules.tags(record['Composer'])
                                        mapfield("field_138", (", ").join(composer), esassetid)
                                except:
                                    pass
                                try:
                                    if record['Country'] != None:
                                        encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(record['Country'])
                                        mapfield("field_179", encops, esassetid) #nur EN, noch übersetzen (074a+c), Multiselect-Feld
                                        mapfield("field_178", decops, esassetid)
                                        mapfield("field_180", frcops, esassetid)   
                                except KeyError:
                                    pass
                                try:
                                    if record['Country_of_Production'] != None:
                                        encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(record['Country_of_Production'])
                                        mapfield("field_176", encops, esassetid)
                                        mapfield("field_175", decops, esassetid)
                                        mapfield("field_177", frcops, esassetid)
                                        mapfield("field_182", (", ").join(enroas), esassetid)
                                        mapfield("field_181", (", ").join(deroas), esassetid)
                                        mapfield("field_183", (", ").join(frroas), esassetid)
                                    if record['Produktionsland'] != None:
                                        encops, decops, frcops, enroas, deroas, frroas = mapmodules.countries(record['Produktionsland'])
                                        mapfield("field_176", encops, esassetid)
                                        mapfield("field_175", decops, esassetid)
                                        mapfield("field_177", frcops, esassetid)
                                        mapfield("field_182", (", ").join(enroas), esassetid)
                                        mapfield("field_181", (", ").join(deroas), esassetid)
                                        mapfield("field_183", (", ").join(frroas), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    decade = mapmodules.decade(record['Decade'])
                                    mapfield("field_133", decade, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Digitised'] == 'Yes':
                                        mapfield("field_91", 'true', esassetid)
                                    else:
                                        mapfield("field_91", 'false', esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Director'] != None:
                                        director = mapmodules.tags(record['Director'])
                                        mapfield("field_135", (", ").join(director), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Editor'] != None:
                                        editor = mapmodules.tags(record["Editor"])
                                        mapfield("field_142", (", ").join(editor), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['English_Shotlist'] != None:
                                        mapfield("field_188", record['English_Shotlist'], esassetid)
                                    else:
                                        mapfield("field_188", "", esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['English_Summary'] != None:
                                        mapfield("field_125", record['English_Summary'], esassetid)
                                    else:
                                        mapfield("field_125", "", esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['English_Tags'] != None:
                                        tags = mapmodules.tags(record['English_Tags'])
                                        mapfield("field_190", (", ").join(tags), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Original_Title_English'] != None:
                                        mapfield("field_65", str(record['Original_Title_English']), esassetid)
                                    elif record['English_Title'] != None:
                                        mapfield("field_65", record['English_Title'], esassetid)
                                    else:
                                        mapfield("field_65", "", esassetid)
                                except KeyError:                                            
                                    pass
                                try:
                                    mapfield("field_99", record['Exploitation_restrictions'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Field84'] != None:
                                        personalities = mapmodules.tags(record['Field84'])
                                        mapfield("field_194", (", ").join(personalities), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_145", record['Filmstudio'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    origformat = mapmodules.format(record['Format_of_original'])
                                    mapfield("field_93", origformat, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_189", record['French_Shotlist'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_187", record['French_summary'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_191", record['French_Tags'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_66", record['French_Title'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    engenre, degenre, frgenre, status = mapmodules.genre(record['Genre'])
                                    mapfield("field_192", engenre, esassetid)
                                    mapfield("field_153", degenre, esassetid)
                                    mapfield("field_193", frgenre, esassetid)
                                    mapfield("field_230", status, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_149", record['German_Shotlist'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_147", record['German_Summary'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['German_Tags'] != None:
                                        detags = mapmodules.tags(record['German_Tags'])
                                        mapfield("field_151", (", ").join(detags), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_64", record['German_Title'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Head_of_Production'] != None:
                                        head = mapmodules.tags(record['Head_of_Production'])
                                        mapfield("field_141", (", ").join(head), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_52", record['Internal_Identifier'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_94", record['Location_of_Original'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Nationality'] != None:
                                        ennat, denat, frnat, nn, nn2, nn3 = mapmodules.countries(record['Nationality'])
                                        mapfield("field_123", ennat, esassetid)
                                        mapfield("field_122", denat, esassetid)
                                        mapfield("field_124", frnat, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_100", record['Notes_on_exploitation_restrictions'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    digiformat = mapmodules.format(record['Original_format_of_digitalization'])
                                    mapfield("field_92", digiformat, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Original_Language_Film'] != None:
                                        if record['Original_Language_Film'] != "Mute":
                                            enlang, delang, frlang = mapmodules.lang(record['Original_Language_Film'])
                                            mapfield("field_80", enlang, esassetid)
                                            mapfield("field_226", delang, esassetid)
                                            mapfield("field_227", frlang, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_148", record['Original_Summary'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_65", record['Original_Tilte_English'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Original_Title_in_Original_Language'] != None:
                                        mapfield("field_63", record['Original_Title_in_Original_Language'].strip(), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_67", record['Other_title'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Personalities'] != None:
                                        person = mapmodules.tags(record['Personalities'])
                                        mapfield("field_155", (", ").join(person), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Personalities_FR'] != None:
                                        personfr = mapmodules.tags(record['Personalities_FR'])
                                        mapfield("field_195", (", ").join(personfr), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Personalities_secondary'] != None:
                                        pers2 = mapmodules.tags(record['Personalities_secondary'])
                                        mapfield("field_156", (", ").join(pers2), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Photographer'] != None:
                                        photo = mapmodules.tags(record['Photographer'])
                                        mapfield("field_137", (", ").join(photo), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Producer'] != None:
                                        prod = mapmodules.tags(record['Producer'])
                                        mapfield("field_140", (", ").join(prod), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Production_Year'] != None:
                                        try:
                                            mapfield("field_232", str(record['Production_Year']), esassetid)
                                        except ValueError:
                                            year = record['Production_Year'].split("/")
                                            mapfield("field_232", int(year[-1]), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Region_English'] != None:
                                        encit = mapmodules.tags(record['Region_English'])
                                        mapfield("field_185", (", ").join(encit), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Region_French'] != None:
                                        frcit = mapmodules.tags(record['Region_French'])
                                        mapfield("field_186", (", ").join(frcit), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Region_German'] != None:
                                        decit = mapmodules.tags(record['Region_German'])
                                        mapfield("field_184", (", ").join(decit), esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_95", record['Resolution'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_98", record['Rights_owner'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['S2T_English'] == "Yes":
                                        mapfield("field_109", "true", esassetid)
                                        mapfield("field_112", "Azure", esassetid)
                                    if record['S2T_German'] == "Yes":
                                        mapfield("field_108", "true", esassetid)
                                        mapfield("field_112", "Azure", esassetid)
                                    if record['Speechmatics_English'] == "Yes":
                                        mapfield("field_109", "true", esassetid)
                                        mapfield("field_112", "Speechmatics", esassetid)
                                    if record['Speechmatics_German'] == "Yes":
                                        mapfield("field_108", "true", esassetid)
                                        mapfield("field_112", "Speechmatics", esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_108", record[''], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['S2T_German_check'] == "Yes":
                                        mapfield("field_111", "true", esassetid)
                                    else:
                                        mapfield("field_111", "false", esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_132", record['Shoot_Date'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_48", record['Shoot_Year_'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_85", record['Synchronisation'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Sound'] == 'Yes':
                                        mapfield("field_89", 'true', esassetid)
                                    else:
                                        mapfield("field_89", 'false', esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_55", record['Source'], esassetid)
                                    accid = mapmodules.accid(record['Source'])
                                    mapfield("field_171", accid, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    user = mapmodules.usergroups(record['User_Group'])
                                    mapfield("field_54", user, esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_144", record['Synchro_Studio'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_53", record['Tape_Can_Box'], esassetid)
                                except KeyError:
                                    pass
                                try:
                                    if record['Third_Party_Rights'] != None:
                                        if record['Third_Party_Rights'] == "No":
                                            mapfield("field_101", "false", esassetid)
                                        else:
                                            mapfield("field_101", "true", esassetid)
                                    else:
                                        mapfield("field_101", "", esassetid)
                                except KeyError:
                                    pass
                                try:
                                    mapfield("field_51", 'true', esassetid)
                                except KeyError:
                                    pass
                                mapfield("field_231", esclipid, esassetid)
                                mapfield("field_233", esassetid, esassetid)
                                mapfield("field_235", escaptureid, esassetid)
                                mapfield("field_127", uuid, esassetid)
                            else:
                                pass
                                #cprint(clipname+' not found in file')
                        except KeyError:
                            pass
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

