def solve_micro_nerdle(history):
    ## history is a list [(guess1, feedback1), (guess2, feedback2), ....]. 
    ## Each element is a tuple containing a previous guess with the feedback it received.
    ## The most recent guess is the last element of history.
    
#     print('history', history, "\n")    
    print('turns', len(history))
    
    def update_glyphs(history, index):
        G_set = set()
        B_set = set()
        R_set = set()
        opp_glyph_list = [0, 1, 2, 3]
        num_glyph_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        opp_dict = {
            "+": 0,
            "-": 1,
            "*": 2,
            "/": 3,
        }
        
        for tuple in history:
#             print('\n', 'tuple', tuple)
#             print('index', index)
#             print('char', tuple[1][index])
            if tuple[1][index] == "G":
                if index == 1:
                    opp_glyph_list = [opp_dict[(tuple[0][index])]]
                else:
                    G_set.add(tuple[0][index])
                    num_glyph_list = [int(tuple[0][index])]
            if tuple[1][index] == "B":
                if index == 1:
                    opp_glyph_list.remove(opp_dict[tuple[0][index]])
                else:
                    B_set.add(tuple[0][index])
                    num_glyph_list.remove(int(tuple[0][index]))
            if tuple[1][index] == "R":
                if index == 1:
                    opp_glyph_list.remove(opp_dict[tuple[0][index]])
                else:
                    R_set.add(int(tuple[0][index]))
                    num_glyph_list.remove(int(tuple[0][index]))
        if index == 1:
            return opp_glyph_list, B_set, R_set, G_set
        else:
            return num_glyph_list, B_set, R_set, G_set


    
    first_glyph = update_glyphs(history, 0)[0]
#     print('first', first_glyph)
    opp_glyph = update_glyphs(history, 1)[0]
#     print('opp', opp_glyph)
    third_glyph = update_glyphs(history, 2)[0]
#     print('third', third_glyph)
    sum_glyph = update_glyphs(history, 4)[0]
#     print('sum', sum_glyph, "\n")
    B_set = update_glyphs(history, 0)[1]
    B_set.update(update_glyphs(history, 2)[1])
    B_set.update(update_glyphs(history, 4)[1])
#     print('B_set', B_set)
    R_set = update_glyphs(history, 0)[2]
    R_set.update(update_glyphs(history, 2)[2])
    R_set.update(update_glyphs(history, 4)[2])
#     print('R_set', R_set)
    G_set = update_glyphs(history, 0)[3]
    G_set.update(update_glyphs(history, 2)[3])
    G_set.update(update_glyphs(history, 4)[3])
#     print('G_set', G_set)
    
    def valid_guess(first_glyph, opp_glyph, third_glyph, sum_glyph, B_set, R_set, G_set): 
#         print('valid guess input', opp_glyph)
        
#         def trim(lst, B_set):
#             return [number for number in lst if str(number) not in B_set]

#         first = trim(first_glyph, B_set)
#         third = trim(third_glyph, B_set)
#         sum_nums = trim(sum_glyph, B_set)

                    
#         first = trim(first_glyph, B_set)
#         print('first', first)
#         second = trim(third_glyph, B_set)
#         print('second', second)
#         sum = trim(sum_glyph, B_set)
#         print('sum', sum)
        
    
        for number in first_glyph:
            for opp in opp_glyph:
                for glyph in third_glyph:
                    for sum_num in sum_glyph:
                        if opp == 0:
                            if number + glyph == sum_num:
#                                 print('guess', str(number) + '+' + str(glyph) + '=' + str(sum_num))
                                return str(number) + '+' + str(glyph) + '=' + str(sum_num)
                        elif opp == 1:
                            if number - glyph == sum_num:
#                                 print('guess', str(number) + '-' + str(glyph) + '=' + str(sum_num))
                                return str(number) + '-' + str(glyph) + '=' + str(sum_num)
                        elif opp == 2:
                            if number * glyph == sum_num:
#                                 print('guess', str(number) + '*' + str(glyph) + '=' + str(sum_num))
                                return str(number) + '*' + str(glyph) + '=' + str(sum_num)
                        elif opp == 3:
                            if glyph == 0:
                                continue
                            if number / glyph == sum_num:
#                                 print('guess', str(number) + '/' + str(glyph) + '=' + str(sum_num))
                                return str(number) + '/' + str(glyph) + '=' + str(sum_num)

    if history == []: guess = '0/1=0' ## guess = any valid arithmetic expression of length 5
    else: guess = valid_guess(first_glyph, opp_glyph, third_glyph, sum_glyph, B_set, R_set, G_set)
#     print('next guess', type(guess))
    return guess
