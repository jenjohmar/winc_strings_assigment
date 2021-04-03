# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_0 = 'Ruud Gullit '

scorer_1 = 'Marco van Basten '

goal_0 = 32

goal_1 = 54

scorers = scorer_0 + str(goal_0) + ', ' + scorer_1 + str(goal_1)

report = f'{scorer_0}scored in the {str(goal_0)}nd minute\n{scorer_1}scored in the {str(goal_1)}th minute'

print(report)

player = 'Ruud Gullit'

print(player)

x = player.find("Ruud")

print(x)

first_name = player[:4]

print(first_name)

y = player.find("Gullit")
print(y)

print(len(player))

last_name_len = len(player[5:11])

print(last_name_len)

name_short = player[0] + '. ' + player[5:11]

print(name_short)

chant = (first_name + '! ') * 3 + (first_name + '!')

print(chant)

good_chant = (first_name + '! ') != (first_name + ' ')

print(good_chant)


