from datetime import datetime


class Isik:
    def __init__(self, nimi, sundinud, amet, surnud):
        self.nimi = nimi
        self.sundinud = datetime.strptime(sundinud, '%Y-%m-%d')
        self.amet = amet
        self.surnud = None if surnud == '0000-00-00' else datetime.strptime(surnud, '%Y-%m-%d')

    def __str__(self):
        surnud = self.surnud.strftime('%d.%m.%Y') if self.surnud else '00.00.0000'
        return f'{self.nimi} {self.sundinud.strftime("%d.%m.%Y")} {self.amet} {surnud}'

    @property
    def vanus(self):
        today = datetime.now()
        years_difference = today.year - self.sundinud.year
        is_before_birthday = (today.month, today.day) < (self.sundinud.month, self.sundinud.day)
        return years_difference - int(is_before_birthday)

    @property
    def elus(self):
        return self.surnud is None
