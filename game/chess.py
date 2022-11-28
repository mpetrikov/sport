def is_in_field(field_size, movement):
    return movement[0] >= 0 and movement[1] >= 0 and movement[0] < field_size and movement[1] < field_size


# (a = 1 and b = 2) or (a = 2 and b = 1) is classic chess movement
def find_all_moves_from_position(field_size, a, b, a_pos, b_pos):
    movements = [
        (a_pos + a, b_pos + b),
        (a_pos + a, b_pos - b),
        (a_pos - a, b_pos + b),
        (a_pos - a, b_pos - b)
    ]

    if a != b:
        movements = movements + [
            (a_pos + b, b_pos + a),
            (a_pos + b, b_pos - a),
            (a_pos - b, b_pos + a),
            (a_pos - b, b_pos - a)
        ]

    return list(filter(lambda m: is_in_field(field_size, m), movements))


def get_chess_step_to_end_of_field(field_size, a, b):
    field = [[-1 for y in range(field_size)] for x in range(field_size)]
    field[0][0] = 0

    moves_count = 0
    step = 1
    moves = find_all_moves_from_position(field_size, a, b, 0, 0)
    moves_count += len(moves)
    while len(moves) != 0:
        is_present_in_moves = {}
        temp_moves = []
        for move in moves:
            field[move[0]][move[1]] = step
            found_moves = find_all_moves_from_position(field_size, a, b, move[0], move[1])
            temp_moves += found_moves

        new_moves = []
        for move in temp_moves:
            if field[move[0]][move[1]] != -1:
                continue
            move_hash = str(move[0]) + "-" + str(move[1])
            if move_hash in is_present_in_moves:
                continue
            is_present_in_moves[move_hash] = 1
            new_moves.append(move)
        moves_count += len(new_moves)
        step += 1
        moves = new_moves

    return field[field_size - 1][field_size - 1]
