import requests
import json
import random
import re
import os
import sys
import  json, requests
import MySQLdb
from pathlib import Path
##########CONFIG N°1###############
database=""
host=""
username=''
password=''
def connectiondb(host,username,password,database):
   cnx = MySQLdb.connect(host,username,password,database)
   cnx.set_character_set('utf8')
   return cnx
def Paginate_pinger():


# import requests

    cookies = {
        'bcookie': '"v=2&6cfa2b05-f26d-40c2-8bd6-02d394c56918"',
        'bscookie': '"v=1&20220820132434e9b94a4b-fb1a-4150-8bba-7cf788d4ccd1AQHAOA_Cj-iXPUNgapf_mndcLgK0Vhw0"',
        'li_rm': 'AQEq8fLeZ-x4ZAAAAYK7bWuMSodGonCJkA1XobdeeOheplFHnJ5n014oOY2QNHFu9L3Xt7LpEuqbkyCi0HqtZpduuEm5c1he3tgCw-X-j20cSWAA4948ssXO',
        'G_ENABLED_IDPS': 'google',
        'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
        'aam_uuid': '67467649985396917883114524228080519169',
        '_gcl_au': '1.1.238934523.1661003071',
        'li_at': 'AQEDATk7fN8AOJH3AAABgrt_hKoAAAGC34wIqk0Ay-GtIjWMeuiOPMrk9RLwHfq_q5y0EzLuPRYRMRJYkHKY_eYVA7mhrN-FabgyLWrOxmq4S-koMLfMhfV9yeHtKsSyfVtQXvlaDI7fJ-AoWFSAEBp1',
        'liap': 'true',
        'JSESSIONID': '"ajax:7056486476108294304"',
        'lang': 'v=2&lang=fr-fr',
        'timezone': 'Europe/Paris',
        'li_theme': 'light',
        'li_theme_set': 'app',
        'li_sugr': '77d281a6-ce12-4122-9f01-c73067a34387',
        'AnalyticsSyncHistory': 'AQLRqtXsk1SHgQAAAYK7f_1_EqPz9Toh7YK7OwMRzPRZ8_xPxUvAa3Vm5Zm3FULobfgJBDlaxu4ToaoH8Luppw',
        'lms_ads': 'AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O',
        'lms_analytics': 'AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O',
        '_guid': '59c7578d-93da-4f2f-83ab-8336ad3573f8',
        'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19225%7CMCMID%7C67324550795701587913167768264896199626%7CMCAAMLH-1661688057%7C6%7CMCAAMB-1661688057%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1661090457s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1823039368',
        'UserMatchHistory': 'AQKHNaH7Ja_JkwAAAYLAW3C_n-H-VIc5BJztBAmAQNdlSN7NP1tXvH_Xn0XEHacLafJgLMYCt757_mI09r0fb-yFH9yc4BpwTkzbJrqBpImcMK6-v5DfvlsNDhP6NkdDuj6p_sIiFB2oHjp91aQnitgac0z8tcHKFXcIv2vYE_6TV63k06PorAtpxDoxG4SG6MKjEloK4hFzENacjCuDtKmzgyyLoI8yG6qUGYG22ds1jyIuHjQSn3InUpte7RrBwYOSZuhgiO88bHnF2WidhaCGY9NHSzneqZ_7uW8',
        'lidc': '"b=VB03:s=V:r=V:a=V:p=V:g=4377:u=3:x=1:i=1661084595:t=1661115354:v=2:sig=AQGijAfaw0Tq1VAWFuszlQnObwrynhO-"',
    }

    headers = {
        'authority': 'www.linkedin.com',
        'accept': 'application/vnd.linkedin.normalized+json+2.1',
        'accept-language': 'en',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'bcookie="v=2&6cfa2b05-f26d-40c2-8bd6-02d394c56918"; bscookie="v=1&20220820132434e9b94a4b-fb1a-4150-8bba-7cf788d4ccd1AQHAOA_Cj-iXPUNgapf_mndcLgK0Vhw0"; li_rm=AQEq8fLeZ-x4ZAAAAYK7bWuMSodGonCJkA1XobdeeOheplFHnJ5n014oOY2QNHFu9L3Xt7LpEuqbkyCi0HqtZpduuEm5c1he3tgCw-X-j20cSWAA4948ssXO; G_ENABLED_IDPS=google; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=67467649985396917883114524228080519169; _gcl_au=1.1.238934523.1661003071; li_at=AQEDATk7fN8AOJH3AAABgrt_hKoAAAGC34wIqk0Ay-GtIjWMeuiOPMrk9RLwHfq_q5y0EzLuPRYRMRJYkHKY_eYVA7mhrN-FabgyLWrOxmq4S-koMLfMhfV9yeHtKsSyfVtQXvlaDI7fJ-AoWFSAEBp1; liap=true; JSESSIONID="ajax:7056486476108294304"; lang=v=2&lang=fr-fr; timezone=Europe/Paris; li_theme=light; li_theme_set=app; li_sugr=77d281a6-ce12-4122-9f01-c73067a34387; AnalyticsSyncHistory=AQLRqtXsk1SHgQAAAYK7f_1_EqPz9Toh7YK7OwMRzPRZ8_xPxUvAa3Vm5Zm3FULobfgJBDlaxu4ToaoH8Luppw; lms_ads=AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O; lms_analytics=AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O; _guid=59c7578d-93da-4f2f-83ab-8336ad3573f8; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19225%7CMCMID%7C67324550795701587913167768264896199626%7CMCAAMLH-1661688057%7C6%7CMCAAMB-1661688057%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1661090457s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1823039368; UserMatchHistory=AQKHNaH7Ja_JkwAAAYLAW3C_n-H-VIc5BJztBAmAQNdlSN7NP1tXvH_Xn0XEHacLafJgLMYCt757_mI09r0fb-yFH9yc4BpwTkzbJrqBpImcMK6-v5DfvlsNDhP6NkdDuj6p_sIiFB2oHjp91aQnitgac0z8tcHKFXcIv2vYE_6TV63k06PorAtpxDoxG4SG6MKjEloK4hFzENacjCuDtKmzgyyLoI8yG6qUGYG22ds1jyIuHjQSn3InUpte7RrBwYOSZuhgiO88bHnF2WidhaCGY9NHSzneqZ_7uW8; lidc="b=VB03:s=V:r=V:a=V:p=V:g=4377:u=3:x=1:i=1661084595:t=1661115354:v=2:sig=AQGijAfaw0Tq1VAWFuszlQnObwrynhO-"',
        'csrf-token': 'ajax:7056486476108294304',
        'referer': 'https://www.linkedin.com/showcase/une-opportunit%C3%A9-de-travailler-au-maroc/posts/?feedView=all',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-li-lang': 'fr_FR',
        'x-li-page-instance': 'urn:li:page:showcase_showcase_posts_index;aff6419e-3f3b-4841-b08c-c3941f46474e',
        'x-li-pem-metadata': 'Voyager - Feed - Comments=load-comments',
        'x-li-track': '{"clientVersion":"1.10.8960","mpVersion":"1.10.8960","osName":"web","timezoneOffset":2,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1366,"displayHeight":768}',
        'x-restli-protocol-version': '2.0.0',
    }

    params = {
        'count': '10',
        'paginationToken': '960199903-1661088814818-a2b37ebf452a1207294a221e9d166890',
        'q': 'comments',
        'sortOrder': 'RELEVANCE',
        'start': '12',
        'updateId': 'activity:6967066590819323904',
    }

    response = requests.get('https://www.linkedin.com/voyager/api/feed/comments', params=params, cookies=cookies, headers=headers)
# print(json.loads(response.text)["data"]["paging"]['count'])
# print(json.loads(response.text)["data"]["paging"]['start'])
    # input(json.loads(response.text)["data"]["paging"]['total'])
    # input(json.loads(response.text))
        
        
    return json.loads(response.text)["data"]["paging"]
    
   
 
def Get_ALL(start):

# import requests

    cookies = {
        'bcookie': '"v=2&6cfa2b05-f26d-40c2-8bd6-02d394c56918"',
        'bscookie': '"v=1&20220820132434e9b94a4b-fb1a-4150-8bba-7cf788d4ccd1AQHAOA_Cj-iXPUNgapf_mndcLgK0Vhw0"',
        'li_rm': 'AQEq8fLeZ-x4ZAAAAYK7bWuMSodGonCJkA1XobdeeOheplFHnJ5n014oOY2QNHFu9L3Xt7LpEuqbkyCi0HqtZpduuEm5c1he3tgCw-X-j20cSWAA4948ssXO',
        'G_ENABLED_IDPS': 'google',
        'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
        'aam_uuid': '67467649985396917883114524228080519169',
        '_gcl_au': '1.1.238934523.1661003071',
        'li_at': 'AQEDATk7fN8AOJH3AAABgrt_hKoAAAGC34wIqk0Ay-GtIjWMeuiOPMrk9RLwHfq_q5y0EzLuPRYRMRJYkHKY_eYVA7mhrN-FabgyLWrOxmq4S-koMLfMhfV9yeHtKsSyfVtQXvlaDI7fJ-AoWFSAEBp1',
        'liap': 'true',
        'JSESSIONID': '"ajax:7056486476108294304"',
        'lang': 'v=2&lang=fr-fr',
        'timezone': 'Europe/Paris',
        'li_theme': 'light',
        'li_theme_set': 'app',
        'li_sugr': '77d281a6-ce12-4122-9f01-c73067a34387',
        'AnalyticsSyncHistory': 'AQLRqtXsk1SHgQAAAYK7f_1_EqPz9Toh7YK7OwMRzPRZ8_xPxUvAa3Vm5Zm3FULobfgJBDlaxu4ToaoH8Luppw',
        'lms_ads': 'AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O',
        'lms_analytics': 'AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O',
        '_guid': '59c7578d-93da-4f2f-83ab-8336ad3573f8',
        'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19225%7CMCMID%7C67324550795701587913167768264896199626%7CMCAAMLH-1661688057%7C6%7CMCAAMB-1661688057%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1661090457s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1823039368',
        'UserMatchHistory': 'AQKHNaH7Ja_JkwAAAYLAW3C_n-H-VIc5BJztBAmAQNdlSN7NP1tXvH_Xn0XEHacLafJgLMYCt757_mI09r0fb-yFH9yc4BpwTkzbJrqBpImcMK6-v5DfvlsNDhP6NkdDuj6p_sIiFB2oHjp91aQnitgac0z8tcHKFXcIv2vYE_6TV63k06PorAtpxDoxG4SG6MKjEloK4hFzENacjCuDtKmzgyyLoI8yG6qUGYG22ds1jyIuHjQSn3InUpte7RrBwYOSZuhgiO88bHnF2WidhaCGY9NHSzneqZ_7uW8',
        'lidc': '"b=VB03:s=V:r=V:a=V:p=V:g=4377:u=3:x=1:i=1661084595:t=1661115354:v=2:sig=AQGijAfaw0Tq1VAWFuszlQnObwrynhO-"',
    }

    headers = {
        'authority': 'www.linkedin.com',
        'accept': 'application/vnd.linkedin.normalized+json+2.1',
        'accept-language': 'en',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'bcookie="v=2&6cfa2b05-f26d-40c2-8bd6-02d394c56918"; bscookie="v=1&20220820132434e9b94a4b-fb1a-4150-8bba-7cf788d4ccd1AQHAOA_Cj-iXPUNgapf_mndcLgK0Vhw0"; li_rm=AQEq8fLeZ-x4ZAAAAYK7bWuMSodGonCJkA1XobdeeOheplFHnJ5n014oOY2QNHFu9L3Xt7LpEuqbkyCi0HqtZpduuEm5c1he3tgCw-X-j20cSWAA4948ssXO; G_ENABLED_IDPS=google; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=67467649985396917883114524228080519169; _gcl_au=1.1.238934523.1661003071; li_at=AQEDATk7fN8AOJH3AAABgrt_hKoAAAGC34wIqk0Ay-GtIjWMeuiOPMrk9RLwHfq_q5y0EzLuPRYRMRJYkHKY_eYVA7mhrN-FabgyLWrOxmq4S-koMLfMhfV9yeHtKsSyfVtQXvlaDI7fJ-AoWFSAEBp1; liap=true; JSESSIONID="ajax:7056486476108294304"; lang=v=2&lang=fr-fr; timezone=Europe/Paris; li_theme=light; li_theme_set=app; li_sugr=77d281a6-ce12-4122-9f01-c73067a34387; AnalyticsSyncHistory=AQLRqtXsk1SHgQAAAYK7f_1_EqPz9Toh7YK7OwMRzPRZ8_xPxUvAa3Vm5Zm3FULobfgJBDlaxu4ToaoH8Luppw; lms_ads=AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O; lms_analytics=AQE5c4ne0Pr2LgAAAYK7gAFcn8KXmM1N8FTFZd4McJwsD7ILJvBfMxA8JEA63E7aNvz_DhONhL716Nl1EOpyEth9xQ_nI37O; _guid=59c7578d-93da-4f2f-83ab-8336ad3573f8; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19225%7CMCMID%7C67324550795701587913167768264896199626%7CMCAAMLH-1661688057%7C6%7CMCAAMB-1661688057%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1661090457s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1823039368; UserMatchHistory=AQKHNaH7Ja_JkwAAAYLAW3C_n-H-VIc5BJztBAmAQNdlSN7NP1tXvH_Xn0XEHacLafJgLMYCt757_mI09r0fb-yFH9yc4BpwTkzbJrqBpImcMK6-v5DfvlsNDhP6NkdDuj6p_sIiFB2oHjp91aQnitgac0z8tcHKFXcIv2vYE_6TV63k06PorAtpxDoxG4SG6MKjEloK4hFzENacjCuDtKmzgyyLoI8yG6qUGYG22ds1jyIuHjQSn3InUpte7RrBwYOSZuhgiO88bHnF2WidhaCGY9NHSzneqZ_7uW8; lidc="b=VB03:s=V:r=V:a=V:p=V:g=4377:u=3:x=1:i=1661084595:t=1661115354:v=2:sig=AQGijAfaw0Tq1VAWFuszlQnObwrynhO-"',
        'csrf-token': 'ajax:7056486476108294304',
        'referer': 'https://www.linkedin.com/showcase/une-opportunit%C3%A9-de-travailler-au-maroc/posts/?feedView=all',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-li-lang': 'fr_FR',
        'x-li-page-instance': 'urn:li:page:showcase_showcase_posts_index;aff6419e-3f3b-4841-b08c-c3941f46474e',
        'x-li-pem-metadata': 'Voyager - Feed - Comments=load-comments',
        'x-li-track': '{"clientVersion":"1.10.8960","mpVersion":"1.10.8960","osName":"web","timezoneOffset":2,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1366,"displayHeight":768}',
        'x-restli-protocol-version': '2.0.0',
    }

    params = {
        'count': '100',
        'paginationToken': '960199903-1661088814818-a2b37ebf452a1207294a221e9d166890',
        'q': 'comments',
        'sortOrder': 'RELEVANCE',
        'start': start,
        'updateId': 'activity:6967066590819323904',
    }

    response = requests.get('https://www.linkedin.com/voyager/api/feed/comments', params=params, cookies=cookies, headers=headers)
    # input(response.text)

    dt=json.loads(response.text)["included"]
    # if "commentV2" in dt:
         # input(dt)
    j=0
    info=[]
    to_check=[]
    for i in dt:
        email=dt[j]
        e=re.findall('[a-zA-Z0-9\.\-\_i]+@[\w.]+',json.dumps(email))
        #######################
        if len(e)!=0:
          if(e[0] in json.dumps(email)):
             if "commenter" in json.dumps(email):
                found_mail=e[0]
                found_member=email["commenter"]["urn"]
             # input(email)
             elif "commenter" not in  json.dumps(email):
                found_mail=email["occupation"]
                # input(found_mail)
                found_member=email["objectUrn"]
                # input(found_member)
             else:
                pass
             
             to_check.append({"email":found_mail,"found_member":found_member})
        if "occupation" in email:
          # print(email["lastName"])         
             member=email["objectUrn"]
             occupation=email["occupation"]
             identifier=email["publicIdentifier"]
             info.append({"member":member,"Identifier":identifier,"Occupation":occupation})
        j=j+1
        ##########################
        
        
    return [info,to_check]

def Filter(inf,t_check):
    final=[]
    for u in t_check:
        similar=list(filter(lambda x:x["member"]==u["found_member"],inf))
        final.append({"Email":u["email"],"Identifier":similar[0]["Identifier"],"member":similar[0]["member"],"Occupation":similar[0]["Occupation"]})
    return final





#####################Data#################################
def Save(cnx,full_name,email,occupation,linkedin_link):
      try:
         curs = cnx.cursor()
         # https://www.linkedin.com/in/cheick-oumar-traore-906472249/
         # print(full_name,occupation,str(email))
         # input()
         curs.execute("""INSERT INTO `emails`(`full_name`,`occupation`,`email`,`linkedin_link`,`interest`) VALUES (%s,%s,%s,%s,%s)""", (full_name,occupation,str(email),linkedin_link,interest))
         # curs.execute("select * from tbl_mp3 where 1") 
         print("Info : inserted successfully. \n ")
         save = cnx.commit() 
         return save
      except MySQLdb.Error as err:  
         print("Something went wrong: (emails) {}".format(err)) 
	 
# def Loads():

	# lists = []
	# li  = []
	# anonfile="./combos.txt"
	# _combo_ = open(anonfile, "r").readlines()
	# lists = [items.rstrip() for items in _combo_]
	# return lists

def Engin(results):
    cnx=connectiondb(host,username,password,database)
    for i in results:
        prefex="https://www.linkedin.com/in/"
        full=i["Identifier"].split("-")
        del full[-1]
        full_name= ' '.join(full)
        full_name=full_name.capitalize()
        occupation=i["Occupation"]
        email=i["Email"]
        # input(email)
        linkedin_link=prefex+i["Identifier"]
        ######Saving#######
        Save(cnx,full_name,email,occupation,linkedin_link)
    return "..."



# input(Paginate_pinger())
Pg=Paginate_pinger()
count=Pg["count"]
start=Pg["start"]
total=Pg["total"]
interest=input("Mention the interest:")
for k in range(int(total/count)):
    if start<=total:
       print("Paging...: "+str(start)+"/"+str(total))
       all_data=Get_ALL(start)   
       inf=all_data[0]
       t_check=all_data[1]
       results=Filter(inf,t_check)
       # final=[]
       try:
          print(Engin(results))
          start=start+10
       except:
          err=1
print("Done Paging.")
    
