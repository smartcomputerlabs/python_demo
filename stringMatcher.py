import numpy as np

ciphertext = int('247855859397007213149309069189849136383',10)
hex_string = "0xba774d59bb6986f467f845caff4dbcff"
#for i in range(0, 121):
   # ct_temp = ciphertext >> i
ct_temp = ciphertext >> 120
#print(ct_temp)
print(hex(ct_temp))
ct_temp = ciphertext >> 96
#print(ct_temp)
print(hex(ct_temp))
ct_temp = ciphertext >> 88
#print(ct_temp)
print(hex(ct_temp))