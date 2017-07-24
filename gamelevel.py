import json

game_dic={}
for i in range(6):
    filename = "temp"+str(i)+".json"
    with open(filename,"r") as tempdata:
        json_match = tempdata.read()
        match_dic = json.loads(json_match)
        for match in match_dic:
            game_dic[match] = {}
            game_dic[match]["matchid"] = match_dic[match]["result"]["match_id"]
            if match_dic[match]["result"]["radiant_win"] == False:
                game_dic[match]["radiwin"] = 0
            else:
                game_dic[match]["radiwin"] = 1
            game_dic[match]["time"] = match_dic[match]["result"]["duration"]
            game_dic[match]["fbtime"] = match_dic[match]["result"]["first_blood_time"]
            game_dic[match]["radi_totalkill"] = 0
            game_dic[match]["dire_totalkill"] = 0

            game_dic[match]["radi_totalassist"] = 0
            game_dic[match]["dire_totalassist"] = 0

            game_dic[match]["radi_denies"] = 0
            game_dic[match]["dire_denies"] = 0

            game_dic[match]["radi_networth"] = 0
            game_dic[match]["dire_networth"] = 0

            game_dic[match]["radi_damage"] = 0
            game_dic[match]["dire_damage"] = 0

            game_dic[match]["radi_level"] = 0
            game_dic[match]["dire_level"] = 0

            game_dic[match]["radi_heal"] = 0
            game_dic[match]["dire_heal"] = 0

            game_dic[match]["version"] = "7.00"
            game_dic[match]["mode"] = match_dic[match]["result"]["game_mode"]

            for p in match_dic[match]["result"]["players"]:
                if int(p["player_slot"])<100:
                    game_dic[match]["radi_totalkill"] += p["kills"]
                    game_dic[match]["radi_totalassist"] += p["assists"]
                    game_dic[match]["radi_denies"] += p["denies"]
                    game_dic[match]["radi_networth"] += p["gold_spent"]
                    game_dic[match]["radi_damage"] += p["hero_damage"]
                    game_dic[match]["radi_level"] += p["level"]
                    game_dic[match]["radi_heal"] += p["hero_healing"]
                else:
                    game_dic[match]["dire_totalkill"] += p["kills"]
                    game_dic[match]["dire_totalassist"] += p["assists"]
                    game_dic[match]["dire_denies"] += p["denies"]
                    game_dic[match]["dire_networth"] += p["gold_spent"]
                    game_dic[match]["dire_damage"] += p["hero_damage"]
                    game_dic[match]["dire_level"] += p["level"]
                    game_dic[match]["dire_heal"] += p["hero_healing"]



print "1"

with open("match.csv","r") as matchfile:
    matchfile.readline()
    lines = matchfile.readlines()
    match_list = [l.split(",") for l in lines]
    for match in match_list:
        game_dic[match[0]] = {}
        game_dic[match[0]]["matchid"] = match[0]
        if str(match[9])=="0":
            game_dic[match[0]]["radiwin"] = 0
            print "~"
        else:
            game_dic[match[0]]["radiwin"] = 1
        game_dic[match[0]]["time"] = match[2]
        game_dic[match[0]]["fbtime"] = match[7]

        game_dic[match[0]]["radi_totalkill"] = 0
        game_dic[match[0]]["dire_totalkill"] = 0

        game_dic[match[0]]["radi_totalassist"] = 0
        game_dic[match[0]]["dire_totalassist"] = 0

        game_dic[match[0]]["radi_denies"] = 0
        game_dic[match[0]]["dire_denies"] = 0

        game_dic[match[0]]["radi_networth"] = 0
        game_dic[match[0]]["dire_networth"] = 0

        game_dic[match[0]]["radi_damage"] = 0
        game_dic[match[0]]["dire_damage"] = 0

        game_dic[match[0]]["radi_level"] = 0
        game_dic[match[0]]["dire_level"] = 0

        game_dic[match[0]]["radi_heal"] = 0
        game_dic[match[0]]["dire_heal"] = 0

        game_dic[match[0]]["version"] = "6.88"
        game_dic[match[0]]["mode"] = match[8]

print "2"

with open("players.csv","r") as playerfile:
    playerfile.readline()
    plines = playerfile.readlines()
    playerlist = [l.split(",") for l in plines]
    for p in playerlist:
        if int(p[3])<100:
            game_dic[p[0]]["radi_totalkill"] += int(p[8])
            game_dic[p[0]]["radi_totalassist"] += int(p[10])
            game_dic[p[0]]["radi_denies"] += int(p[11])
            game_dic[p[0]]["radi_networth"] += int(p[5])
            game_dic[p[0]]["radi_damage"] += int(p[14])
            game_dic[p[0]]["radi_level"] += int(p[23])
            game_dic[p[0]]["radi_heal"] += int(p[15])
        else:
            game_dic[p[0]]["dire_totalkill"] += int(p[8])
            game_dic[p[0]]["dire_totalassist"] += int(p[10])
            game_dic[p[0]]["dire_denies"] += int(p[11])
            game_dic[p[0]]["dire_networth"] += int(p[5])
            game_dic[p[0]]["dire_damage"] += int(p[14])
            game_dic[p[0]]["dire_level"] += int(p[23])
            game_dic[p[0]]["dire_heal"] += int(p[15])

print "3"

fout = open("overallmatch.csv","w")
fout.write("matchid,radiwin,time,fbtime,radi_totalkill,dire_totalkill,radi_totalassist,dire_totalassist,radi_denies,dire_denies,radi_networth,dire_networth,radi_damage,dire_damage,radi_level,dire_level,radi_heal,dire_heal,mode,version\n")
for match in game_dic:
    fout.write(str(game_dic[match]["matchid"])+","+str(game_dic[match]["radiwin"])+","+str(game_dic[match]["time"])+","+str(game_dic[match]["fbtime"])+","+str(game_dic[match]["radi_totalkill"])+","+str(game_dic[match]["dire_totalkill"])+","+str(game_dic[match]["radi_totalassist"])+","+str(game_dic[match]["dire_totalassist"])+","+str(game_dic[match]["radi_denies"])+","+str(game_dic[match]["dire_denies"])+","+str(game_dic[match]["radi_networth"])+","+str(game_dic[match]["dire_networth"])+","+str(game_dic[match]["radi_damage"])+","+str(game_dic[match]["dire_damage"])+","+str(game_dic[match]["radi_level"])+","+str(game_dic[match]["dire_level"])+","+str(game_dic[match]["radi_heal"])+","+str(game_dic[match]["dire_heal"])+","+str(game_dic[match]["mode"])+","+str(game_dic[match]["version"])+"\n")

fout.close()
#
# for i in game_dic:
#     print i
#     break
#


#
# matchid
# result
# time
# radi_kill
# dire_kill
# radi_totallasthit
# dire_totallasthit
# radi_denies
# dire_denies
# radi_totaldamage
# dire_totaldamage
# radi_networth
# dire_networth
# mode
# first_blood_time
#
#
# matchid
# time
# first_blood_time
# totalkill
# version
#
#
# hero??
