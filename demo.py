import csv

with open('michelle_artists.csv', 'rU') as csvfile:
    m_a = csv.reader(csvfile, delimiter=',', quotechar='|')
    m_a = list(m_a)
    #print m_a

with open('tanmay_artists.csv', 'rU') as csvfile:
    t_a = csv.reader(csvfile, delimiter=',', quotechar='|')
    t_a = list(t_a)
    #print t_a

with open('michelle_songs.csv', 'rU') as csvfile:
    m_s = csv.reader(csvfile, delimiter=',', quotechar='|')
    m_s = list(m_s)

with open('tanmay_songs.csv', 'rU') as csvfile:
    t_s = csv.reader(csvfile, delimiter=',', quotechar='|')
    t_s = list(t_s)

#     for row in m_a:
#         print row
#         #print ', '.join(row)
#
# with open('tanmay_artists.csv', 'rU') as csvfile:
#     t_a = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in t_a:
#         print row
#
new_list = []
for element in m_a:
    if element in t_a:
        new_list.append(element)

print new_list

songs_list = []
for element in m_s:
    if element is t_s:
        songs_list.append(element)

print songs_list
