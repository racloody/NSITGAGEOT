class temps():
    def __init__(self,h,m,s):
        self.heure = h
        self.minute = m
        self.seconde = s

    def __str__(self):
        return "{}:{}:{}".format(self.heure,self.minute,self.seconde)

    def __add__(self,tps2):
        sec_fin = (self.seconde + tps2.seconde) % 60
        min_fin = (self.minute + tps2.minute + (self.seconde + tps2.seconde)//60) % 60
        hr_fin = (self.heure + tps2.heure + (self.minute + tps2.minute)//60)
        return "{}:{}:{}".format(hr_fin,min_fin,sec_fin)
    
    def __sub__(self,tps2):
        if tps2.heure <= self.heure:
            if tps2.seconde > self.seconde or tps2.minute > self.minute:
                if tps2.seconde > self.seconde :
                    self.minute += -1
                    self.seconde += 60
                    if self.minute < tps2.minute:
                        self.heure+= -1
                        self.minute += 60

                    hr_fin = self.heure - tps2.heure
                    min_fin = self.minute - tps2.minute
                    sec_fin = self.seconde - tps2.seconde
                    return "{}:{}:{}".format(hr_fin,min_fin,sec_fin)
            
                elif tps2.minute > self.minute:
                    self.heure += -1
                    self.minute += 60
                    hr_fin = self.heure - tps2.heure
                    min_fin = self.minute - tps2.minute
                    sec_fin = self.seconde - tps2.seconde
                    return "{}:{}:{}".format(hr_fin,min_fin,sec_fin)
            else:
                hr_fin = self.heure - tps2.heure
                min_fin = self.minute - tps2.minute
                sec_fin = self.seconde - tps2.seconde
                return "{}:{}:{}".format(hr_fin,min_fin,sec_fin)
        else:
            return "improssible à déterminer, entrez une heure inferieure à la première"
heure_1 = input("Entrez une heure 1 sous la forme HH:MM:SS : ")
hours1 , minutes1 , seconds1 = heure_1.split(':')
heure_2 = input("Entrez une heure 2 sous la forme HH:MM:SS : ")
hours2 , minutes2 , seconds2 = heure_2.split(':')
hours1 , minutes1 , seconds1, hours2 , minutes2 , seconds2 = int(hours1) , int(minutes1) , int(seconds1) , int(hours2) , int(minutes2) , int(seconds2)
temps1=temps(hours1,minutes1,seconds1)
temps2=temps(hours2,minutes2,seconds2)
opé=input("Choisissez une opération (+/-) : ")
if opé == "-":
    print(f"Le résultat est {temps1-temps2}")
else:
    print(f"Le résultat est {temps1+temps2}")