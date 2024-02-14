
def chess_players(file_name: str):
    data_file = open(file_name)

    chess_players_list = []

    for player in data_file:
        
        Rank, Name, Country, Rating, Birth_year = player.split("; ")
        player_tuple = int(Rank), Name, Country, int(Rating), int(Birth_year)
        chess_players_list.append(player_tuple)
    return chess_players_list


def sort_players(chess_players):
    sort_dict = {}
    for player in chess_players:
        (Rank, Name, Country, Rating, Birth_year) = player

        if Country not in sort_dict:
            sort_dict[Country] = [(Name, Rating)]
        else:
            sort_dict[Country].append((Name, Rating))
    return sort_dict


        



chess_players_list = chess_players("countries.txt")
