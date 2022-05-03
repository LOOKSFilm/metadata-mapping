import dearpygui.dearpygui as dpg
from tkinter import filedialog
import tkinter as tk
import login
import imagenmapping
import defamapping
import defaimagenmapping
import defaupdatemapping
import threading

def start():
    selmapping = dpg.get_value(item='selmapping')
    selspaces = []
    selspace = dpg.get_value(item='selspaces')
    if selspace == 'All Spaces':
        selspaces = spaceslist
    if selspace == 'All Progress Einspiel':
        selspaces = ["Progress Einspiel", "Progress Einspiel 2", "Progress Einspiel 2020"]
    else:
        selspaces.append(selspace)
    if selmapping == 'Imagen':
        runmapping = threading.Thread(target=imagenmapping.run, args=(selspaces, selmapping))
    elif selmapping == "DEFA":
        runmapping = threading.Thread(target=defamapping.run, args=(selspaces, selmapping))
    elif selmapping == "DEFA & Imagen":
        runmapping = threading.Thread(target=defaimagenmapping.run, args=(selspaces, selmapping))
    elif selmapping == "DEFA Update":
        runmapping = threading.Thread(target=defaupdatemapping.run, args=(selspaces, selmapping))
    runmapping.start()

            

def openfile(sender, event):
    if event == None or event == False:                
        root = tk.Tk()
        root.withdraw()
        global filepath
        filepath = filedialog.askopenfilename(initialdir='D:/Cloud/Coding/Python/flow/', filetypes=[[('xml', 'json'), ('*.xml', '*.json')]])
        if filepath == '':
            dpg.set_item_label(item='importbtn', label='Open XML/JSON')
            pass
        else:
            dpg.enable_item(item='startimport')    
            dpg.set_item_label(item='importbtn', label=filepath)


def main():
    dpg.set_viewport_resizable(True)
    with dpg.window(tag='mainwindow', menubar=True, no_scrollbar=True) as mainwindow:
        dpg.set_primary_window('mainwindow', True)
        with dpg.child_window(tag='import', border=False):
            with dpg.table(tag='selections', header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    dpg.add_combo(label='Select Mapping', items=['DEFA', 'Imagen', 'DEFA & Imagen', 'DEFA Update'], tag='selmapping')
                    spaceslistcomp = ['All Archives', 'All Progress Einspiel', 'All Spaces']
                    global spaceslist
                    spaceslist = []
                    mediaspaces = login.flow.getMediaSpaces()
                    for space in mediaspaces:
                        space = space['name'].replace('"', '')
                        space.replace(' ', '%20')
                        spaceslist.append(space)
                    spaceslistcomp.extend(spaceslist)
                    dpg.add_combo(label='Select Meadiaspaces', items=spaceslistcomp, tag='selspaces')

            dpg.add_button(label='Open XML/JSON', callback=openfile, tag='importbtn')
            dpg.add_button(label='Import', callback=start, tag='startimport', enabled=False)
            dpg.add_child_window(label='Console', tag='console')
            
    #MENUBAR
    with dpg.menu_bar(parent='mainwindow'):            
        with dpg.menu(label='File', tag='filemenu'):
            dpg.add_menu_item(label='Exit', callback=lambda: dpg.stop_dearpygui())
        with dpg.menu(label='Window', tag='windowmenu'):
            dpg.add_menu_item(label='toggle Fullscreen', callback=lambda: dpg.toggle_viewport_fullscreen())
        with dpg.menu(label='Help', tag='helpmenu'):
            dpg.add_menu_item(label='Dearpy Commands', callback=lambda: dpg.show_documentation())
            dpg.add_menu_item(label='Style Editor', callback=lambda: dpg.show_style_editor())
            dpg.add_menu_item(label='Logs', callback=help)