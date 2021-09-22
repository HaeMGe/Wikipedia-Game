import requests
import json


def main():
    startwert = input("Wo soll angefangen Werden? ")
    titel = startwert
    endwert = input("Wo soll die Suche beendet werden? ")
    # titel ="Fru%CC%88hstu%CC%88cksfleisch"
    i = 0
    while startwert != endwert:
        r = requests.get(
            'https://de.wikipedia.org/w/api.php?action=query&prop=links&pllimit=max&format=json&titles=' + str(titel))
        with open('Wikipedia.json', 'w') as jsondatei:
            json.dump(r.json(), jsondatei)
        with open('Wikipedia.json', 'r') as jsondatei:
            data = json.load(jsondatei)
            i = i + 1
            page_id = data['query']['pages'].keys()
            for page in page_id:

                titel = data['query']['pages'][page]["links"]
                liste = []
                x = 0
                for link in titel:
                    print(str(x) + " " + link["title"])
                    liste.append(link["title"])
                    x += 1
        print("------------------------------------")
        zahl = int(input("Rate doch!"))
        titel = liste[zahl]

    print("Fertichhhh in" + i)


# https://www.utf8-chartable.de/
# {"batchcomplete":"","query":{"pages":{"-1":{"ns":0,"title":"SUCHBEGRIFF","missing":""}}},"limits":{"links":500}}


if __name__ == '__main__':
    main()
