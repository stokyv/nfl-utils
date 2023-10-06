
#data: dataframe containing rows of game events
# unique game ids in data
def unique_game_id(data):
    game_ids = data.game_id.unique()
    return game_ids

# games = unique_game_id(data)
# games

def select_game(data, method='random'):
    game_ids = unique_game_id(data)
    return random.choice(game_ids)

# gid1 = select_game(data, 'random')

def get_game_data(data, game_id='random'):
    if game_id == 'random':
        game_id = select_game(data, 'random')
    game_data = data[data['game_id']==game_id].sort_values(by='play_id')
    return game_data

# g1 = get_game_data(data, 'random')
# g1.head()

