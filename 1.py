"""1"""

# def sekund_oraligi(vaqt1, vaqt2):
#     sekundlar = abs(vaqt1 - vaqt2)
#     return sekundlar
#
# # Misol:
# vaqt1 = 3600
# vaqt2 = 5400
# print(sekund_oraligi(vaqt1, vaqt2))


"""2"""

# def juft_boluvchilar_soni(N):
#     juft_sonlar = [x for x in range(1, N + 1) if x % 2 == 0]
#     return len(juft_sonlar)
#
# # Misol:
# N = 10
# print(juft_boluvchilar_soni(N))


"""3"""

# def tup_sonlar(n):
#     for i in range(1, n + 1):
#         yield i ** 2
#
# n = 5
# for tup in tup_sonlar(n):
#     print(tup)


"""4"""

# def tub_boluvchilar(son):
#     for i in range(2, son):
#         if son % i == 0:
#             break
#     else:
#         yield son
#
# son = 20
# for tub in tub_boluvchilar(son):
#     print(tub)


"""5"""

# def juft_sonlar(royxat):
#     for son in royxat:
#         if son % 2 == 0:
#             yield son
#
# royxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for juft in juft_sonlar(royxat):
#     print(juft)


"""6"""

# def soz_uzunligi(matn):
#     sozlar = matn.split()
#     for soz in sozlar:
#         yield len(soz)
#
# # Misol:
# matn = "Bu bir matn misoli"
# for uzunlik in soz_uzunligi(matn):
#     print(uzunlik)


"""7"""

# def uzun_sozlar(matn):
#     sozlar = matn.split()
#     for soz in sozlar:
#         if len(soz) > 5:
#             yield soz
#
# matn = "Bu bir uzun so'zlar matni misoli"
# for uzun in uzun_sozlar(matn):
#     print(uzun)


"""8"""

# def qatnashgan_sonlar(royxat):
#     for son in royxat:
#         if royxat.count(son) == 3:
#             yield son
#
# royxat = [1, 2, 3, 2, 4, 5, 2, 6, 7, 2]
# for qatnashgan in qatnashgan_sonlar(royxat):
#     print(qatnashgan)
