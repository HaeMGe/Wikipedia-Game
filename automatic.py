import requests
import json
import pprint


def main():
    startwert = input("Wo soll angefangen Werden? ")
    endwert = input("Wo soll die Suche beendet werden? ")
    #durchgehen = ["Fru%CC%88hstu%CC%88cksfleisch"]
    durchgehen = [ startwert]
    alle = [" "]
    anzahlDurchgang = [0]
    titel = durchgehen[0]
    #durchgehen.pop(0)

    i = 0
    # Python%20(Programmiersprache)
    while titel != endwert:
        print(titel+str(anzahlDurchgang[0]))

        r = requests.get(
            'https://de.wikipedia.org/w/api.php?action=query&prop=links&pllimit=max&format=json&titles=' + str(titel))
        with open('Wikipedia.json', 'w') as jsondatei:
            json.dump(r.json(), jsondatei)
        with open('Wikipedia.json', 'r') as jsondatei:
            data = json.load(jsondatei)
            i = i + 1
            page_id = data['query']['pages'].keys()
            #print(page_id)
            for e in page_id:
                #print(i)
                l = e
            #print(l)
            if int(l) > 0:
                for page in page_id:

                    titel = data['query']['pages'][page]["links"]
                    liste = []
                    x = 0
                    for link in titel:
                        #print(str(x) + " " + link["title"])
                        if link['title'] in durchgehen:
                          #print(" ")
                          u = 0
                        elif link['title'] in alle:
                          #print(" ")
                          u = 0
                        else:
                          durchgehen.append(link["title"])
                        
                          anzahlDurchgang.append(anzahlDurchgang[0]+1)
                        #liste.append(link["title"])
                          x += 1
        print("------------------------------------")
        #zahl = int(input("Rate doch!"))
        #titel = liste[zahl]
        alle.append(durchgehen[0])
        durchgehen.pop(0)
        anzahlDurchgang.pop(0)
        if durchgehen[0] != None:
            titel = durchgehen[0]
        else:
            print("Leider gibt es keinen Weg dorthin")



    #print("Fertichhhh in " + str(i))
    print("Vom Start bis Ende kommt man mit "+str(anzahlDurchgang[0])+" Schritten")


# https://www.utf8-chartable.de/
# {"batchcomplete":"","query":{"pages":{"-1":{"ns":0,"title":"SUCHBEGRIFF","missing":""}}},"limits":{"links":500}}


if __name__ == '__main__':
    main()
