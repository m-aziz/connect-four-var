



#print the matrix with formatting
def print_matrix(board):
	for row in board:
		print(row)

#print the board version of matrix
def print_board(board):
	n = len(board)
	while n != 0:
		print(board[n-1]) 
		n-=1

def invalidity_finder(board, col_selection, ROW_COUNT):
	if (board[ROW_COUNT - 1][col_selection] == 0):
		return False
	else:
		print("Column is full")
	return True

#places the current player number in the selected column of the matrix and return the row which it is placed in
def drop_piece(board,column_selection, current_player, player_indicator, COLUMN_COUNT, ROW_COUNT):
	for r in range(ROW_COUNT): #from 0 to 5
		if board[r][column_selection] == 0:
			board[r][column_selection] = player_indicator[current_player]
			return r

def check_for_win(board,row,column,ROW_COUNT,COLUMN_COUNT,current_player,player_indicator):
	h_win = horizontal_win(board,row,column,ROW_COUNT,COLUMN_COUNT, player_indicator[current_player])
	v_win = vertical_win(board,row,column,ROW_COUNT,COLUMN_COUNT, player_indicator[current_player])
	d_win = diag_win(board,row,column,ROW_COUNT,COLUMN_COUNT, player_indicator[current_player])

	if h_win or v_win or d_win:
		return True
	else:
		return False

def vertical_win(board,row,column,ROW_COUNT,COLUMN_COUNT, player_number):
	pieces_in_sequence = 0
	for r in range(ROW_COUNT):
		if board[r][column] == player_number:
			pieces_in_sequence +=1
			if pieces_in_sequence == 4:
				return True
		else: 
			pieces_in_sequence = 0
	return False

def horizontal_win(board,row,column,ROW_COUNT,COLUMN_COUNT, player_number):
	pieces_in_sequence = 0
	for c in range(COLUMN_COUNT):
		if board[row][c] == player_number:
			pieces_in_sequence +=1
			if pieces_in_sequence == 4:
				return True
		else: 
			pieces_in_sequence = 0
	return False

def diag_win(board,row,column,ROW_COUNT,COLUMN_COUNT, player_number): 
	pieces_in_sequence_nw_to_se = 0
	pieces_in_sequence_ne_to_sw = 0
	for n in range(-4,5):
		#northwest to southeast diagnol 
		if (index_in_board(board,row-n,column-n) and board[row-n][column-n] == player_number):
			pieces_in_sequence_nw_to_se +=1
			if pieces_in_sequence_nw_to_se == 4:
				return True
		else:
			#northeast to southwest diagnol
			pieces_in_sequence_nw_to_se = 0
		if (index_in_board(board,row-n,column+n) and board[row-n][column+n] == player_number):
			pieces_in_sequence_ne_to_sw +=1
			if pieces_in_sequence_ne_to_sw == 4:
				return True
		else:
			pieces_in_sequence_ne_to_sw = 0
	return False


def index_in_board(board,row_index,column_index):
	try:
		possible_index = board[row_index][column_index]
		return True
	except Exception:
		return False





#MAIN METHOD TO SIMULATE GAMEPLAY
#INITIALIZE VARIABLES

#creates board
ROW_COUNT = int(input("Enter the # of rows your would like your board to be (6):"))
COLUMN_COUNT = int(input("Enter the # of columns your would like your board to be (7):"))
board = [[0 for row in range(COLUMN_COUNT)] for i in range(ROW_COUNT)]
"""
board = [
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
]
print_board(test_board)
"""

#game variables
pieces_placed = 0
game_finished = False
players = ["Yellow", "Red"]
player_indicator = {"Yellow": 1, "Red": 2}
num_of_players = 2

while not game_finished and pieces_placed != (ROW_COUNT * COLUMN_COUNT):

	#game is designed so unlimited numbers of players allowed to play in same board
	current_player = players[pieces_placed % num_of_players]
	print(current_player + "'s turn")
	turn_played = False


	while(turn_played == False):
		print_board(board)
		column_selection = int(input("Enter a column to place peice in (1-7):")) - 1
		if invalidity_finder(board,column_selection, ROW_COUNT):
			continue
		row_selection = drop_piece(board,column_selection, current_player, player_indicator,COLUMN_COUNT, ROW_COUNT)
		turn_played = True
		#game_finished = check_for_win()

	pieces_placed += 1
	winner = check_for_win(board,row_selection,column_selection,ROW_COUNT,COLUMN_COUNT,current_player,player_indicator)
	
	
	if (winner):
		game_finished = True
		print("/n" +current_player + " is the Winner!")

print()
print_board(board)












