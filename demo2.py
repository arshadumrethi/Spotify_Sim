from itertools import permutations

mic_a = [['Toro y Moi'], ['Tycho'], ['Tame Impala'], ['Jungle'], ['FKJ'], ['LA Priest'], ['Romare'], ['Card On Spokes']]

tan_a = [['Tame Impala'], ['Com Truise'], ['J.Views'], ['Pedestrian'], ['Disclosure'], ['Miguel'], ['Francis and the Lights'], ['Swell'], ['Esbe']]

nic_a = [['Drake'], ['deadmau5'], ['Kendrick Lamar'], ['Dream Theater'], ['Slash'], ['The Black Eyed Peas'], ['Natiruts'], ['Calvin Harris']]

ars_a = [['Kendrick Lamar'], ['deadmau5'], ['Noname'], ['Beacon'], ['Sampha'], ['KAYTRANADA'], ['Duke Dumont'], ['The Deli'], ['Anderson.Paak'], ['Maggie Rogers']]

aam_a = [['The xx'], ['Bonobo'], ['Lorde'], ['Flume'], ['STRFKR'], ['Golden Vessel'], ['Drake'], ['Isaac Delusion']]

abh_a = [['Toro y Moi'], ['Tame Impala'], ['Linkin Park'], ['Portugal. The Man'], ['Four Tet'], ['Mura Masa'], ['Santigold'], ['ODESZA']]

ani_a = [['Kasabian'], ['Foster The People'], ['STRFKR'], ['Electric Guest'], ['Arctic Monkeys'], ['Jagwar Ma'], ['The Arcs'], ['KAYTRANADA'], ['GUM']]

jen_a = [['Drake'], ['Kings of Leon'], ['Kendrick Lamar'], ['Foo Fighters'], ['Frank Ocean'], ['Romare'], ['Halsey'], ['Lorde']]

zee_a = [['Bonobo'], ['The Black Keys'], ['Jungle'], ['The Knocks'], ['Kanye West'], ['Jain'], ['Todd Terje'], ['TOBACCO'], ['DJ Shadow']]


artist_list = [mic_a, tan_a, nic_a, ars_a, aam_a, abh_a, ani_a, jen_a, zee_a]

print list(permutations(artist_list))


# def artist_sim_score(a, b):
#     new_list = []
#     for element in a:
#         if element in b:
#             new_list.append(element)
#             print "Your common artists is/are: %s" % new_list
#             score = len(new_list) #For each simillar artist 1 point is assigned.
#             print "Your artist simillarity score is %d" % score
#
# for list in list of lists:
#     artist_sim_score(person1, permutations(persons))
#
# artist_sim_score(mic_a, tan_a)
# artist_sim_score(mic_a, nic_a)
# artist_sim_score(mic_a, ars_a)
# artist_sim_score(mic_a, aam_a)
# artist_sim_score(mic_a, abh_a)
# artist_sim_score(mic_a, ani_a)
# artist_sim_score(mic_a, jen_a)
# artist_sim_score(mic_a, zee_a)
