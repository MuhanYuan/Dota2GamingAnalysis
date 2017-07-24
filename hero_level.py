import json

def ave(l):
    return float(reduce(lambda x, y: x + y, l)) / len(l)


h_dic = {}
with open("hero_names.csv","r") as hfile:
    hfile.readline()
    lines = hfile.readlines()
    for l in lines:
        h_dic[l.split(",")[1]] = l.split(",")[2].strip()

#
# hero_dic={}
# for i in range(6):
#     filename = "temp"+str(i)+".json"
#     with open(filename,"r") as tempdata:
#         json_match = tempdata.read()
#         match_dic = json.loads(json_match)
#         for match in match_dic:
#             for p in match_dic[match]["result"]["players"]:
#                 if p["hero_id"] not in hero_dic:
#                     hero_dic[p["hero_id"]] = {}
#                     hero_dic[p["hero_id"]]["kills"] = []
#                     hero_dic[p["hero_id"]]["assists"] = []
#                     hero_dic[p["hero_id"]]["death"] = []
#                     hero_dic[p["hero_id"]]["damage"] = []
#                     hero_dic[p["hero_id"]]["heal"] = []
#                     hero_dic[p["hero_id"]]["lasthit"] = []
#                     hero_dic[p["hero_id"]]["denies"] = []
#                     hero_dic[p["hero_id"]]["level"] = []
#                     hero_dic[p["hero_id"]]["tower_damage"] = []
#                     hero_dic[p["hero_id"]]["win"] = []
#
#                     hero_dic[p["hero_id"]]["kills"].append(p["kills"])
#                     hero_dic[p["hero_id"]]["assists"].append(p["assists"])
#                     hero_dic[p["hero_id"]]["death"].append(p["deaths"])
#                     hero_dic[p["hero_id"]]["damage"].append(p["hero_damage"])
#                     hero_dic[p["hero_id"]]["heal"].append(p["hero_healing"])
#                     hero_dic[p["hero_id"]]["lasthit"].append(p["last_hits"])
#                     hero_dic[p["hero_id"]]["denies"].append(p["denies"])
#                     hero_dic[p["hero_id"]]["level"].append(p["level"])
#                     hero_dic[p["hero_id"]]["tower_damage"].append(p["tower_damage"])
#                     if int(p["player_slot"])<100:
#                         if match_dic[match]["result"]["radiant_win"] == False:
#                             hero_dic[p["hero_id"]]["win"].append(0)
#                         else:
#                             hero_dic[p["hero_id"]]["win"].append(1)
#                     else:
#                         if match_dic[match]["result"]["radiant_win"] == True:
#                             hero_dic[p["hero_id"]]["win"].append(0)
#                         else:
#                             hero_dic[p["hero_id"]]["win"].append(1)
#                 else:
#                     hero_dic[p["hero_id"]]["kills"].append(p["kills"])
#                     hero_dic[p["hero_id"]]["assists"].append(p["assists"])
#                     hero_dic[p["hero_id"]]["death"].append(p["deaths"])
#                     hero_dic[p["hero_id"]]["damage"].append(p["hero_damage"])
#                     hero_dic[p["hero_id"]]["heal"].append(p["hero_healing"])
#                     hero_dic[p["hero_id"]]["lasthit"].append(p["last_hits"])
#                     hero_dic[p["hero_id"]]["denies"].append(p["denies"])
#                     hero_dic[p["hero_id"]]["level"].append(p["level"])
#                     hero_dic[p["hero_id"]]["tower_damage"].append(p["tower_damage"])
#                     if int(p["player_slot"])<100:
#                         if match_dic[match]["result"]["radiant_win"] == False:
#                             hero_dic[p["hero_id"]]["win"].append(0)
#                         else:
#                             hero_dic[p["hero_id"]]["win"].append(1)
#                     else:
#                         if match_dic[match]["result"]["radiant_win"] == True:
#                             hero_dic[p["hero_id"]]["win"].append(0)
#                         else:
#                             hero_dic[p["hero_id"]]["win"].append(1)
#
# print hero_dic.keys()

game_dic={}
with open("match.csv","r") as matchfile:
    matchfile.readline()
    lines = matchfile.readlines()
    match_list = [l.split(",") for l in lines]
    for match in match_list:
        game_dic[match[0]] = {}
        if str(match[9])=="0":
            game_dic[match[0]]["radiwin"] = 0
        else:
            game_dic[match[0]]["radiwin"] = 1

hero_dic1 = {}
fold = open("players.csv","r")
fold.readline()
lines = fold.readlines()
player_list = [l.split(",") for l in lines]


for p in player_list:
    if p[2] not in hero_dic1:
        hero_dic1[p[2]] = {}
        hero_dic1[p[2]]["kills"] = []
        hero_dic1[p[2]]["assists"] = []
        hero_dic1[p[2]]["death"] = []
        hero_dic1[p[2]]["damage"] = []
        hero_dic1[p[2]]["heal"] = []
        hero_dic1[p[2]]["lasthit"] = []
        hero_dic1[p[2]]["denies"] = []
        hero_dic1[p[2]]["level"] = []
        hero_dic1[p[2]]["tower_damage"] = []
        hero_dic1[p[2]]["win"] = []

        hero_dic1[p[2]]["kills"].append(int(p[8]))
        hero_dic1[p[2]]["assists"].append(int(p[10]))
        hero_dic1[p[2]]["death"].append(int(p[9]))
        hero_dic1[p[2]]["damage"].append(int(p[14]))
        hero_dic1[p[2]]["heal"].append(int(p[15]))
        hero_dic1[p[2]]["lasthit"].append(int(p[12]))
        hero_dic1[p[2]]["denies"].append(int(p[11]))
        hero_dic1[p[2]]["level"].append(int(p[23]))
        hero_dic1[p[2]]["tower_damage"].append(int(p[16]))

        if game_dic[p[0]] == 0:
            if int(p[3]) < 100:
                hero_dic1[p[2]]["win"].append(0)
            else:
                hero_dic1[p[2]]["win"].append(1)
        else:
            if int(p[3]) > 100:
                hero_dic1[p[2]]["win"].append(0)
            else:
                hero_dic1[p[2]]["win"].append(1)
    else:
        hero_dic1[p[2]]["kills"].append(int(p[8]))
        hero_dic1[p[2]]["assists"].append(int(p[10]))
        hero_dic1[p[2]]["death"].append(int(p[9]))
        hero_dic1[p[2]]["damage"].append(int(p[14]))
        hero_dic1[p[2]]["heal"].append(int(p[15]))
        hero_dic1[p[2]]["lasthit"].append(int(p[12]))
        hero_dic1[p[2]]["denies"].append(int(p[11]))
        hero_dic1[p[2]]["level"].append(int(p[23]))
        hero_dic1[p[2]]["tower_damage"].append(int(p[16]))

        if game_dic[p[0]] == 0:
            if int(p[3]) < 100:
                hero_dic1[p[2]]["win"].append(0)
            else:
                hero_dic1[p[2]]["win"].append(1)
        else:
            if int(p[3]) > 100:
                hero_dic1[p[2]]["win"].append(0)
            else:
                hero_dic1[p[2]]["win"].append(1)

# fout1 = open("hero7.csv","w")
# fout1.write("Hero,win,kills,deaths,assists,damage,heal,lasthit,denies,level,tower\n")
# for h in hero_dic:
#     if h == 0:
#         continue
#     fout1.write(h_dic[str(h)]+",")
#     fout1.write(str(ave(hero_dic[h]["win"])) +",")
#     fout1.write(str(ave(hero_dic[h]["kills"])) +",")
#     fout1.write(str(ave(hero_dic[h]["death"])) +",")
#     fout1.write(str(ave(hero_dic[h]["assists"])) +",")
#     fout1.write(str(ave(hero_dic[h]["damage"])) +",")
#     fout1.write(str(ave(hero_dic[h]["heal"])) +",")
#     fout1.write(str(ave(hero_dic[h]["lasthit"])) +",")
#     fout1.write(str(ave(hero_dic[h]["denies"])) +",")
#     fout1.write(str(ave(hero_dic[h]["level"])) +",")
#     fout1.write(str(ave(hero_dic[h]["tower_damage"])) +"\n")
# fout1.close()


fout2 = open("hero6.csv","w")
fout2.write("Hero,win,kills,deaths,assists,damage,heal,lasthit,denies,level,tower\n")
for h in hero_dic1:
    if h == "0":
        continue
    fout2.write(h_dic[str(h)]+",")
    fout2.write(str(ave(hero_dic1[h]["win"])) +",")
    fout2.write(str(ave(hero_dic1[h]["kills"])) +",")
    fout2.write(str(ave(hero_dic1[h]["death"])) +",")
    fout2.write(str(ave(hero_dic1[h]["assists"])) +",")
    fout2.write(str(ave(hero_dic1[h]["damage"])) +",")
    fout2.write(str(ave(hero_dic1[h]["heal"])) +",")
    fout2.write(str(ave(hero_dic1[h]["lasthit"])) +",")
    fout2.write(str(ave(hero_dic1[h]["denies"])) +",")
    fout2.write(str(ave(hero_dic1[h]["level"])) +",")
    fout2.write(str(ave(hero_dic1[h]["tower_damage"])) +"\n")
fout2.close()
