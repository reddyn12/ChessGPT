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

test = "1. e4 d6 2. d4 Nf6 3. Bd3 g6 4. f4 Bg7 5. Nf3 c5 6. c3 O-O 7. dxc5 dxc5 8. e5 Ng4 9. O-O Nc6 10. Na3 a6 11. Be4 Qc7 12. Qe1 Nh6 13. Nh4 Be6 14. f5 Nxf5 15. Bxf5 gxf5 16. Nxf5 Qxe5 17. Nxg7 Qxe1 18. Rxe1 Kxg7 19. Be3 b6 20. b3 Rfd8 21. Rad1 Rxd1 22. Rxd1 f6 23. Bf4 Rc8 24. Nc2 Kf7 25. Ne3 b5 26. Kf2 a5 27. Rd2 Ra8 28. Nd5 b4 29. cxb4 Bxd5 30. Rxd5 Nxb4 31. Rd2 Ke6 32. Be3 Rc8 33. a3 Nd5 34. Rc2 Nxe3 35. Kxe3 Rb8 36. Rc3 Kd5 37. Kd2 Rg8 38. g3 Rg4 39. Rf3 Rd4+ 40. Kc3 Re4 41. Rd3+ Kc6 42. Rf3 h5 43. h3 Kb5 44. Kd3 Rd4+ 45. Kc3 a4 46. bxa4+ Rxa4 47. Kb2 Re4 48. Rb3+ Kc4 49. Rf3 h4 50. g4 Kb5 51. Kb3 Kc6 52. a4 Rb4+ 53. Ka3 Rb1 54. Re3 Rb7 55. g5 fxg5 56. Re5 c4 57. a5"
t1 = movesToFen(test)
print(t1)

test = " Rb5 0-1"
print(movesToFen(test,t1))

test = "1. e4 d6 2. d4 Nf6 3. Bd3 g6 4. f4 Bg7 5. Nf3 c5 6. c3 O-O 7. dxc5 dxc5 8. e5 Ng4 9. O-O Nc6 10. Na3 a6 11. Be4 Qc7 12. Qe1 Nh6 13. Nh4 Be6 14. f5 Nxf5 15. Bxf5 gxf5 16. Nxf5 Qxe5 17. Nxg7 Qxe1 18. Rxe1 Kxg7 19. Be3 b6 20. b3 Rfd8 21. Rad1 Rxd1 22. Rxd1 f6 23. Bf4 Rc8 24. Nc2 Kf7 25. Ne3 b5 26. Kf2 a5 27. Rd2 Ra8 28. Nd5 b4 29. cxb4 Bxd5 30. Rxd5 Nxb4 31. Rd2 Ke6 32. Be3 Rc8 33. a3 Nd5 34. Rc2 Nxe3 35. Kxe3 Rb8 36. Rc3 Kd5 37. Kd2 Rg8 38. g3 Rg4 39. Rf3 Rd4+ 40. Kc3 Re4 41. Rd3+ Kc6 42. Rf3 h5 43. h3 Kb5 44. Kd3 Rd4+ 45. Kc3 a4 46. bxa4+ Rxa4 47. Kb2 Re4 48. Rb3+ Kc4 49. Rf3 h4 50. g4 Kb5 51. Kb3 Kc6 52. a4 Rb4+ 53. Ka3 Rb1 54. Re3 Rb7 55. g5 fxg5 56. Re5 c4 57. a5 Rb5 0-1"
print(movesToFen(test))

test = "1. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Nxd4 Bc5 5. Nxc6 Qf6 6. Qd2 dxc6 7. Nc3 Bd4 8. Bd3 Ne7 9. O-O Ng6 10. Ne2 Bb6 11. Nf4 Ne5 12. Be2 Ng4 13. Nd3 Be6 14. h3 Ne5 15. Nxe5 Qxe5 16. Qf4 Qc5 17. c3 O-O-O 18. Be3 Qd6 19. Rfd1 Qxf4 20. Bxf4 Rxd1+ 21. Bxd1 Rd8 22. Bg4 Re8 23. Re1 a5 24. Kf1 Bc5 25. Be3 Bf8 26. f3 b5 27. Kf2 a4 28. Rd1 Bd6 29. Bd4 g6 30. Bxe6+ fxe6 31. e5 Be7 32. Be3 c5 33. f4 c4 34. a3 h5 35. g3 c5 36. Kf3 Rh8 37. Ke4 Kc7 38. Rg1 Kd7 39. Rg2 Rh7 40. Rd2+ Kc6 41. Rg2 Kd7 42. Bf2 Rh8 43. g4 hxg4 44. hxg4 Rh3 45. f5 gxf5+ 46. gxf5 exf5+ 47. Kxf5 b4 48. Bg3 Rh5+ 49. Ke4 Ke6 50. Bf4 Rh3 51. Rg6+ Kf7 52. Ra6 bxc3 53. bxc3 Rxc3 54. Kf5 Rf3 55. e6+ Kg7 56. Ra7 Kf8 57. Ke4 Rd3 58. Be5 Bh4 59. Rh7 Bd8 60. Kf5 Rf3+ 61. Kg6 Re3 62. e7+ Ke8 63. exd8=Q+ Kxd8 64. Kf6 c3 65. Ke6 Kc8 66. Rc7+ Kb8 67. Rxc5+ Kb7 68. Kd5 c2 69. Bb2 Re2 70. Rc4 Rh2 71. Kc5 Rh6 72. Kd5 Rh5+ 73. Be5 Rh3 74. Bd6 Rd3+ 75. Ke6 Rd2 76. Bf4 Rf2 77. Bc1 Rg2 78. Ke5 Rh2 79. Rc3 Kb6 80. Kd4 Kb5 81. Rc8 Rg2 82. Kc3 Rg6 83. Kb2 Rg2 84. Rb8+ Ka6 85. Rd8 Kb5 86. Rd4 Rh2 87. Bd2 Kc5 88. Rd8 Rh3 89. Bb4+ Kb5 90. Rd5+ Kb6 91. Rd2 Kb5 92. Kxc2 Rh5 93. Rf2 Rg5 94. Bd2 Rc5+ 95. Kb2 Rd5 96. Rg2 Rc5 97. Rg4 Rc4 98. Rg8 Re4 99. Ra8 Rg4 100. Ra5+ Kb6 101. Bb4 Rg2+ 102. Kc3 Rg3+ 103. Kb2 Rg2+ 104. Kc1 Rg1+ 105. Kd2 Rg2+ 106. Ke1 Kc6 107. Rxa4 Kb5 108. Ra8 Ra2 109. Rc8 Rg2 110. Kd1 Ka4 111. Ra8+ Kb3 112. Be7 Rg7 113. Ra7 Rg2 114. Rb7+ Ka4 115. Rb4+ Ka5 116. Bd8+ Ka6 117. Bf6 Rf2 118. Bc3 Rg2 119. Bd2 Rh2 120. Kc2 Rg2 121. a4 Rh2 122. Rd4 Rg2 123. Kb3 Rg6 124. Bb4 Rh6 125. Kc4 Rg6 126. Re4 Rh6 127. Bc5 Kb7 128. Kb5 Rg6 129. Re7+ Kb8 130. Bb6 Rg8 131. Ba7+ Ka8 132. Bc5 Rg6 133. Rd7 Rh6 134. Rg7 Re6 135. a5 Re8 136. Ka6 Rd8 137. Rf7 Kb8 138. Ba7+ Ka8 139. Bb6 Rc8 140. Be3 Rc6+ 141. Kb5 Rc8 142. Ra7+ Kb8 143. Rg7 Ka8 144. Bc5 Rb8+ 145. Kc4 Rc8 146. Rd7 Re8 147. Bb6 Rc8+ 148. Kd5 Rg8 149. Kd6 Rg6+ 150. Kc5 Rg5+ 151. Kc6 Rg6+ 152. Kb5 Rg8 153. Rd1 Re8 154. Rh1 Rg8 155. Rh2 Re8 156. Rh3 Rg8 157. Rh5 Re8 158. Rh2 Rg8 159. Bc5 Rb8+ 160. Kc4 Rg8 161. Bd6 Rc8+ 162. Kd5 Rg8 163. Kc6 Rc8+ 164. Bc7 Rg8 165. a6 Ka7 166. Rh3 Rf8 167. Rh7 Ka8 168. Rh1 Ka7 169. Rb1 Rg8 170. Rf1 Re8 171. Bb6+ Ka8 172. Kb5 Rg8 173. Bc5 Rb8+ 174. Kc4 Rg8 175. Rf4 Rh8 176. Rg4 Re8 177. Rg3 Rh8 178. Rg2 Re8 179. Rg6 Rh8 180. Rf6 Re8 181. Rf5 Rg8 182. Rf4 Rh8 183. Rf3 Rg8 184. Rf2 Rh8 185. Rf1 Rg8 186. Re1 Rh8 187. Re2 Rg8 188. Re3 Rh8 189. Re4 Rg8 190. Re5 Rh8 191. Re6 Rg8 192. Re1 Rh8 193. Rd1 Rg8 194. Rd2 Rh8 195. Rd3 Rg8 196. Rd4 Rh8 197. Rd1 Rg8 198. a7 Rh8 199. Rg1 Re8 200. Kb5 Rh8 201. Rg2 Re8 202. Bd6 Rc8 203. Kb6 Rh8 204. Kc6 Rc8+ 205. Bc7 Rh8 206. Rf2 Rg8 207. Rh2 Rf8 208. Rh5 Rg8 209. Rh1 Rf8 210. Rb1 Rf2 211. Bd6 Rc2+ 212. Kd7 Kxa7 213. Bc7 Rg2 214. Kc8 Rg8+ 215. Bd8 Rg6 216. Rb5 Rh6 217. Bc7 Rc6 218. Ra5+ Ra6 219. Rc5 Rg6 220. Rc1 Ka6 221. Rb1 Rh6 222. Kd7 Rh3 223. Rb6+ Ka7 224. Rb1 Ka6 225. Kc8 Rh5 226. Rb8 Rc5 227. Rb2 Rh5 228. Rb8 Rf5 229. Rb6+ Ka7 230. Rc6 Rf8+ 231. Bd8 Rg8 232. Rc7+ Ka8 233. Rc1 Rg7 234. Bc7 Rg8+ 235. Kd7 Rg7+ 236. Kc6 Rg6+ 237. Bd6 Rg7 238. Rh1 Rh7 239. Re1 1-0"
print(movesToFen(test))

test = "1. e4"
print(movesToFen((test)))