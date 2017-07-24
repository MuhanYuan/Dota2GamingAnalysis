import requests
import json

dota_api = "5893D96762028E80A2BA393B7671E06C"

last_match_id = 2863356816
# last_match_id = 2851772870
# last_match_id = 2863336816
# last_match_id = 2859190160
# last_match_id = 2859137572
# last_match_id = 2859127572

match_cache = {}
dota2_url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/"
# Be careful when you set this number larger than 1000. The caching file could be big.
match_number = 10000
match_id = last_match_id
for i in range(match_number):
    try:
        h = requests.get(dota2_url,params={"key":dota_api,"match_id":match_id})
        match_his = json.loads(h.text)
        if "error" not in  match_his[u'result'].keys():
            if "radiant_win" in match_his[u'result'].keys():
                match_cache[match_id] = match_his
                match_dic[match_id] = match_his
                change_made=True
                # print "New match found"
    except:
        # print "gg"
        pass
    match_id +=1

f =open("temp.json","w")
f.write(json.dumps(match_cache))
f.close()
