import requests
import json
import wget

#static globals
client_id="82013fb3a531d5414f478747c1aca622"

print("Dobrodošli v RTV-4D prenešalnik")
print("Za vas pripravil Lightning5\n")

originalUrl=input("Vnesite URL videa na RTV-4D:")
showID=originalUrl.split("/")[-1]

print("VideoID: " + showID)

#Pridobi jwt drm token
r = requests.get('https://api.rtvslo.si/ava/getRecordingDrm/' + showID, params = {'client_id': client_id } )
drm = json.loads(r.content)
jwt=drm['response']['jwt']

#Pridobi seznam
r = requests.get('https://api.rtvslo.si/ava/getMedia/' + showID, params = {'client_id': client_id, 'jwt': jwt })
mediaInfo = json.loads(r.content)
mediaArr=mediaInfo['response']['mediaFiles']

print("Izberi bitrate: (more is better)")

for i in range(len(mediaArr)):
    print(str(i) + ") " +  str(mediaArr[i]['bitrate']) + " bps")

izbranaKvaliteta = int(input())

dlUrl = mediaArr[izbranaKvaliteta]['streams']['http']
wget.download(dlUrl)
