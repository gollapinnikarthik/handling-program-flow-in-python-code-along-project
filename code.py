# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

 #print(data) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
deliveries_faced = data['innings'][0]['1st innings']['deliveries']
#print(deliveries_faced)
deliveries_count = 0
for deliveries in deliveries_faced:
    for delivery_info, delivery_faced in deliveries.items():
        if delivery_faced['batsman'] == 'SC Ganguly':
            deliveries_count += 1
print('No of deliveries faced by Batsman SC Ganguly are:-', deliveries_count)

#  Who was man of the match and how many runs did he scored ?
man_of_the_match = data['info']['player_of_match'][0]
runs_scored = 0
for player_of_match in deliveries_faced:
    for delivery_info, delivery_faced in player_of_match.items():
        if delivery_faced['batsman'] == 'BB McCullum':
            runs_scored += delivery_faced['runs']['batsman']

print("Man of the Match was: " + man_of_the_match + " " + "and number od runs scored are: " + str(runs_scored))

#  Which batsman played in the first inning?
batsman = []
for batsman_played in deliveries_faced:
    for delivery_info, delivery_faced in batsman_played.items():
        batsman.append(delivery_faced['batsman'])
print('All the batsman who played in first innings are : ', list(set(batsman)))

# Which batsman had the most no. of sixes in first inning ?
most_sixes = []
for sixes in deliveries_faced:
    for delivery_info, delivery_faced in sixes.items():
        if delivery_faced['runs']['batsman'] == 6:
            most_sixes.append(delivery_faced['batsman'])

#Defining a function to calcuate frequencies in a list using a dictionary
def freqcountlist(most_sixes):
    six = {}
    for freq in most_sixes:
        if freq in six:
            six[freq] += 1
        else:
            six[freq] = 1
    return max(six, key = six.get)

print('The batsman who had maximum no.of sixes in first innings:', freqcountlist(most_sixes))


# Find the names of all players that got bowled out in the second innings.
bowled_out_2nd = data['innings'][1]['2nd innings']['deliveries']
bowled_out_list= []
for bowled_out in bowled_out_2nd:
    for delivery_info, delivery_faced in bowled_out.items():
        try:
            if delivery_faced['wicket']['kind'] == 'bowled':
                bowled_out_list.append(delivery_faced['wicket']['player_out'])
        #As the value does not exist in all the keys we get key error so we use try except to pass so the for loop block executes as long as the condtion is met
        except:
            pass
print('Names of the players who got bowled out in second innings are: ', bowled_out_list)       

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
def get_extras(extras):
    extra_runs = 0
    for extra_runs in extras:
        for delivery_info, delivery_faced in extra_runs.items():
            if delivery_faced['runs'] == 'extras':
                extra_runs += delivery_faced['runs']['extras']
    return extra_runs

extras_1st_innings = get_extras(deliveries_faced)
extras_2nd_innings = get_extras(bowled_out_2nd)
difference = len(extras_1st_innings) - len(extras_2nd_innings)
print("2nd innings had ", abs(difference), " more extras than 1st innings")


# Code ends here


