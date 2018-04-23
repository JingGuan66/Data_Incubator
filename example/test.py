import requests
'''
ri_male =requests.get("https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_002E&for=state:44")
ri_female = requests.get("https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_026E&for=state:44")

print ri_female.json()
print ri_female.json()[1][1]

e= [['ri_male','B01001_002E'],['ri_female','B01001_026E']]
for i in e:
    print 'https://api.census.gov/data/2016/acs/acs1?get=NAME,'+i[1]+'&for=state:44'
'''
w=[['ct','09'],
['me','23'],
['ma','25'],
['nh','33'],
['vt','50']]
index =[]
for j in w:
    e =[[j[0]+'_male','B01001_002E'],[j[0]+'_female','B01001_026E'],[j[0]+'_total','B01001_001E']
        ]
    for i in e:
        data=requests.get('https://api.census.gov/data/2016/acs/acs1?get=NAME,'+i[1]+'&for=state:'+j[1])
 #       print data.json()
        i.append(data.json()[1][1])
 #       print i
        index.append(i)
print index

with open('data.csv', 'w') as the_file:
    the_file.write('Title,Data\n')
    for i in index:
        the_file.write(i[0])
        the_file.write(',')
        the_file.write(i[2])
        the_file.write('\n')
        