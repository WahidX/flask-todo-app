id_seq = 0

# Generating sequence number for id
def get_id():
	global id_seq
	id_seq += 1
	return id_seq