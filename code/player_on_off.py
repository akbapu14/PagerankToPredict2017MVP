from nba_py import player

player_ids = {}
player_ids["LeBron James"] = 2544
player_ids["Jimmy Butler"] = 202710
player_ids["Giannis Antetokounmpo"] = 203507
player_ids["Isaiah Thomas"] = 202738
player_ids["John Wall"] = 202322
player_ids["Carmelo Anthony"] = 2546
player_ids["Kyle Lowry"] = 200768
player_ids["Paul George"] = 202331
player_ids["Kemba Walker"] = 202689
player_ids["Paul Millsap"] = 200794
player_ids["James Harden"] = 201935
player_ids["Kevin Durant"] = 201142
player_ids["Kawhi Leonard"] = 202695
player_ids["Anthony Davis"] = 203076
player_ids["Russell Westbrook"] = 201566
player_ids["Marc Gasol"] = 201188
player_ids["DeAndre Jordan"] = 201599
player_ids["Gordon Hayward"] = 202330


def find_on_off_rating():
	player_oo_dict = {}
	for player1 in player_ids:
		player_oo_dict[player1] = {}
		for player2 in player_ids:
			if player1 != player2:
				p = player.PlayerVsPlayer(player_ids[player1], player_ids[player2])
				try:
					dataframe = p.on_off_court()
					oo_rating = dataframe["PLUS_MINUS"][1] # dataframe["PLUS_MINUS"][0]
					player_oo_dict[player1][player2] = oo_rating
				except:
					print(player1, player2)

	return player_oo_dict

of_dict = find_on_off_rating()


import pickle
pickle.dump(of_dict, open('of_dict.pickle', 'wb'))
