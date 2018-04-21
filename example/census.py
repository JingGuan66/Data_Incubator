import requests
'''
ri_male = requests.get("https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_002E&for=state:44")
print ri_male.json()
print ri_male.json()[1][1]
female = requests.get("https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_026E&for=state:44")
#Rhode Island total population of male and famale 
ri_county_male =requests.get("https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_002E&for=county:*&in=state:44")
#print ri_county_male.text
ri_county_female =requests.get("https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_026E&for=county:*&in=state:44")
print ri_county_female.json()

print '***************'
'''
'''e = [['ri_male','B01001_002E'],
     ['ri_female','B01001_026E']
    ]
for i in e:
    print 'https://api.census.gov/data/2016/acs/acs1?get=NAME' + i[1] + '&for=state:44'
'''  

w = [['ct','09'],['me','23'],['ma','25'],['nh','33'],['ri', '44'],['vt','50']
    ]
index = []
for j in w:
    e = [[j[0]+'_male','B01001_002E'],
       [j[0]+'_female','B01001_026E'],
       [j[0]+'_total','B01001_001E']
       ] 
    for i in e:
        data = requests.get('https://api.census.gov/data/2016/acs/acs1?get=NAME,'+ i[1] + '&for=state:'+ j[1])
        i.append(data.json()[1][1])
        index.append(i)
#print index
for i in index:
    print i
    
    
