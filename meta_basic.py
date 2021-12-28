# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:05:52 2021

@author: Playdata
"""

import folium

import webbrowser
map_y = folium.Map([37.52860, 126.93431])
map_y.save('folium_map_1.html')
webbrowser.open_new("folium_map_1.html")


map_y = folium.Map([37.52860, 126.93431], zoom_start=15)
map_y.save('folium_map_2.html')
webbrowser.open_new('folium_map_2.html')


lat, long = 37.52860, 126.93431
map_y = folium.Map([lat, long], zoom_start=15)
map_y.save('folium_map_3.html')
webbrowser.open_new('folium_map_3.html')


lat, long = 37.52860, 126.93431
map_y = folium.Map([lat, long], zoom_start=15)
folium.Marker([lat, long]).add_to(map_y)

map_y.save('folium_map_3.html')
webbrowser.open_new("folium_map_3.html")


lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889

map_y = folium.Map([lat1, long1], zoom_start=15)
folium.Marker([lat1, long1]).add_to(map_y)
folium.Marker([lat2, long2]).add_to(map_y)

map_y.save('folium_map_4.html')
webbrowser.open_new("folium_map_4.html")

lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889

map_y = folium.Map([lat1, long1], zoom_start=15)
folium.Marker([lat1, long1], tooltip='여의도 한강공원').add_to(map_y)
folium.Marker([lat2, long2], tooltip='여의도 공원').add_to(map_y)

map_y.save('folium_map_5.html')
webbrowser.open_new("folium_map_5.html")


lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889

map_y = folium.Map([lat1, long1], zoom_start=15)
folium.Marker([lat1, long1], popup='여의도 한강공원').add_to(map_y)
folium.Marker([lat2, long2], popup='여의도 공원').add_to(map_y)

map_y.save('folium_map_6.html')
webbrowser.open_new('folium_map_6.html')



lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889
lat3, long3 = 37.51865, 126.92041

map_y = folium.Map([lat1, long1], zoom_start=15)
folium.Marker([lat1, long1], tooltip='여의도 한강공원').add_to(map_y)
folium.Marker([lat2, long2], tooltip='여의도 공원').add_to(map_y)
folium.Marker([lat3, long3], tooltip='샛강생태공원').add_to(map_y)

map_y.save('folium_map_7.html')
webbrowser.open_new('folium_map_7.html')

lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889
lat3, long3 = 37.51865, 126.92041

map_y = folium.Map([lat1, long1], zoom_start=15)
folium.Marker([lat1, long1], tooltip='여의도 한강공원', icon=folium.Icon(color='red')).add_to(map_y)
folium.Marker([lat2, long2], tooltip='여의도 공원', icon=folium.Icon(color='blue')).add_to(map_y)
folium.Marker([lat3, long3], tooltip='샛강생태공원', icon=folium.Icon(color='purple')).add_to(map_y)
 
map_y.save('folium_map_8.html')
webbrowser.open_new("folium_map_8.html")


lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889
lat3, long3 = 37.51865, 126.92041

map_y = folium.Map([lat1, long1], zoom_start=15)
folium.Marker([lat1, long1], tooltip='여의도 한강공원', icon=folium.Icon(color='red', icon='heart')).add_to(map_y)
folium.Marker([lat2, long2], tooltip='여의도 공원', icon=folium.Icon(color='blue', icon='home')).add_to(map_y)
folium.Marker([lat3, long3], tooltip='샛강생태공원', icon=folium.Icon(color='purple', icon='flag')).add_to(map_y)

map_y.save('folium_map_9.html')
webbrowser.open_new("folium_map_9.html")


folium.Marker(
    [lat1, long1], tooltip='여의도 한강공원', icon=folium.Icon(color='red', icon='automobile', prefix='fa')).add_to(map_y)
folium.Marker(
    [lat2, long2], tooltip='여의도 공원', icon=folium.Icon(color='blue', icon='balance-scale', prefix='fa')).add_to(map_y)
folium.Marker(
    [lat3, long3], tooltip='샛강생태공원', icon=folium.Icon(color='purple', icon='ban', prefix='fa')).add_to(map_y)

map_y.save('folium_map_10.html')
webbrowser.open_new("folium_map_10.html")


lat = [37.52860, 37.52400, 37.51865]
long= [126.93431, 126.91889, 126.92041]
names = ['여의도 한강공원', '여의도 공원', '샛강생태공원']
icons = ['automobile', 'balance-scale', 'ban']
colors = ['red', 'blue', 'purple']

map_y = folium.Map([lat[0], long[0]], zoom_start=15)

for i in range(len(lat)):
    folium.Marker([lat[i], long[i]], tooltip=names[i], icon=folium.Icon(color=colors[i], icon=icons[i], perfix='fa')).add_to(map_y)
    
map_y.save('folium_map_11.html')
webbrowser.open_new("folium_map_11.html")    



### ======================================= ###

import re

txt1 = "Life is too short, you need python"
txt2 = "The best moments of my life"

print(re.search('Life', txt1))
print(re.search('Life', txt2))

match =  re.search('Life', txt1)
match.group()

match.start()

match.end()

match.span()

print(re.search('Life', txt2))
print(re.search('Life', txt2))

txt1 = "Life is too short, you need python"
txt2 = "The best moments of my life"
txt3 = "My Life My Choice"

print(re.search('^Life', txt1))
print(re.search('^Life', txt2))
print(re.search('^Life', txt3))
print(re.search('Life', txt3))

re.search('My', txt3)

txt3 = "Life is like a box of chocolates"
txt4 = "My Life My Choice"

print(re.search('^Life', txt1))
print(re.search('^Life', txt2))
print(re.search('^Life', txt3))
print(re.search('^Life', txt4))

print(re.search('Life', txt1))
print(re.search('Life', txt2))

re.findall('MY', txt4)

txt1 = 'Who are you to judge the life l live'
txt2 = 'The best moments of my life'

print(re.search('life$', txt1))
print(re.search('life$', txt2))

import re

re.search('A.. A', 'ABA')
re.search('A.. A', 'ABBA')
re.search('A.. A', 'ABBBA')

re.search('AB', 'A')
re.search('AB*', 'AA')
re.search('AB*', 'J-HOP')
re.search('AB*', 'X-MAN')
re.search('AB*', 'CABBA')
re.search('AB*', 'CABBBBBA')

re.search('AB+', 'A')
re.search('AB+', 'AA')
re.search('AB+', 'J-HOP')
re.search('AB+', 'X-MAN')
re.search('AB+', 'CABBA')
re.search('AB+', 'CABBBBBA')

txt3 = 'My life my life my life in the sumshine'
re.findall('[Mm]y', txt3)