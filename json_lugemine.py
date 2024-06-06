import json
from tkinter import Tk, Label
from Isik import Isik

with open('2018-09-18_tuntud_eesti.json', 'r') as f:
    andmed = json.load(f)
    isikud = [Isik(**isik) for isik in andmed]

root = Tk()

stats = {
    'kokku': 0,
    'pikim_nimi': '',
    'vanim_elus': None,
    'vanim_surnud': None,
    'näitleja': 0,
    'sündinud_1997': 0,
    'elukutse': set(),
    'kaks_nime': 0,
    'sama_sünd_surm': 0,
    'elus': 0,
    'surnud': 0
}

for isik in isikud:
    stats['kokku'] += 1
    if len(isik.nimi.replace(' ', '')) > len(stats['pikim_nimi'].replace(' ', '')):
        stats['pikim_nimi'] = isik.nimi
    if isik.elus:
        stats['elus'] += 1
        if stats['vanim_elus'] is None or isik.vanus > stats['vanim_elus'].vanus:
            stats['vanim_elus'] = isik
    else:
        stats['surnud'] += 1
        vanus_surma_hetkel = (isik.surnud - isik.sundinud).days // 365
        if stats['vanim_surnud'] is None or vanus_surma_hetkel > stats['vanim_surnud']['vanus']:
            stats['vanim_surnud'] = {
                'nimi': isik.nimi,
                'vanus': vanus_surma_hetkel,
                'surnud': isik.surnud,
                'sundinud': isik.sundinud  # Add this line
            }
    if "näitleja" in isik.amet.lower():  # Count people whose profession includes "actor"
        stats['näitleja'] += 1
    if isik.sundinud.year == 1997:
        stats['sündinud_1997'] += 1
    stats['elukutse'].add(isik.amet)
    if len(isik.nimi.split(' ')) > 2:
        stats['kaks_nime'] += 1
    if isik.surnud and isik.surnud.day == isik.sundinud.day and isik.surnud.month == isik.sundinud.month:
        stats['sama_sünd_surm'] += 1

Label(root, text=f'Isikute arv kokku: {stats["kokku"]}').pack()
Label(root, text=f'Kõige pikem nimi ja tähemärkide arv (ilma tühikuteta): {stats["pikim_nimi"]}, '
                 f'{len(stats["pikim_nimi"].replace(" ", ""))}').pack()
Label(root, text=f'Kõige vanem elav inimene: {stats["vanim_elus"].nimi}, {stats["vanim_elus"].vanus}, '
                 f'Sünd: {stats["vanim_elus"].sundinud.strftime("%d.%m.%Y")}').pack()
Label(root, text=f'Kõige vanem surnud inimene: {stats["vanim_surnud"]["nimi"]}, '
                 f'{stats["vanim_surnud"]["vanus"]}, Sünd: {stats["vanim_surnud"]["sundinud"].strftime("%d.%m.%Y")}, '
                 f'Surnud: {stats["vanim_surnud"]["surnud"].strftime("%d.%m.%Y")}').pack()
Label(root, text=f'Näitlejate koguarv: {stats["näitleja"]}').pack()
Label(root, text=f'Sündinud 1997 aastal: {stats["sündinud_1997"]}').pack()
Label(root, text=f'Kui palju on erinevaid elukutseid: {len(stats["elukutse"])}').pack()
Label(root, text=f'Nimi sisaldab rohkem kui kaks nime: {stats["kaks_nime"]}').pack()
Label(root, text=f'Sünniaeg ja surmaaega on sama va. aasta: {stats["sama_sünd_surm"]}').pack()
Label(root, text=f'Elavaid ja surnud isikud: {stats["elus"]}, {stats["surnud"]}').pack()

root.mainloop()

