import chess


def movesToFen(pgn_moves, fen_string=None):
    board = chess.Board(fen=fen_string) if fen_string else chess.Board()
    moves = pgn_moves.split()
    for move in moves:
        if "." in move:
            pass
        elif "0-1"==move:
            pass
        elif "1-0"==move:
            pass
        elif "1/2-1/2"==move:
            pass
        else:
            board.push_san(move)
    return board.fen()



baseStart = "rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR"

# # empty spaces will have e instead of number of consecutive empty
# def movesToFen(moves:str, startFen=baseStart):
#     moves = moves.split(" ")
#     board = Board(startFen)
#     for move in moves:
#         if "." in move:
#             # print(move)
#             pass
#         else:
#             board.makeMove(move)

test = "1. e4 d6 2. d4 Nf6 3. Bd3 g6 4. f4 Bg7 5. Nf3 c5 6. c3 O-O 7. dxc5 dxc5 8. e5 Ng4 9. O-O Nc6 10. Na3 a6 11. Be4 Qc7 12. Qe1 Nh6 13. Nh4 Be6 14. f5 Nxf5 15. Bxf5 gxf5 16. Nxf5 Qxe5 17. Nxg7 Qxe1 18. Rxe1 Kxg7 19. Be3 b6 20. b3 Rfd8 21. Rad1 Rxd1 22. Rxd1 f6 23. Bf4 Rc8 24. Nc2 Kf7 25. Ne3 b5 26. Kf2 a5 27. Rd2 Ra8 28. Nd5 b4 29. cxb4 Bxd5 30. Rxd5 Nxb4 31. Rd2 Ke6 32. Be3 Rc8 33. a3 Nd5 34. Rc2 Nxe3 35. Kxe3 Rb8 36. Rc3 Kd5 37. Kd2 Rg8 38. g3 Rg4 39. Rf3 Rd4+ 40. Kc3 Re4 41. Rd3+ Kc6 42. Rf3 h5 43. h3 Kb5 44. Kd3 Rd4+ 45. Kc3 a4 46. bxa4+ Rxa4 47. Kb2 Re4 48. Rb3+ Kc4 49. Rf3 h4 50. g4 Kb5 51. Kb3 Kc6 52. a4 Rb4+ 53. Ka3 Rb1 54. Re3 Rb7 55. g5 fxg5 56. Re5 c4 57. a5 Rb5 0-1"
print(movesToFen(test))