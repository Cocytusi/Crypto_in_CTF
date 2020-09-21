# Challenges:
# ‘I was surfing the crimson wave and oh my gosh I was totally bugging. I also tried out the lilac hair trend but it didn’t work out. That’s not to say you are any better, you are a snob and a half. But let’s get back to the main question here- Who am I? (You don’t know my name)’
# Ciphertext = “52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e”
# (hex) Key = “12123”

import base64

cipher = "52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e".split('f')
key = ['3' + i for i in "12123"]

res = []
for i, n in enumerate(cipher):
	x = int(n, 16)
	y = int(key[i % len(key)], 16)
	res.append(hex(x ^ y)[2:])

res = "".join(res)
print(bytes.fromhex(res).decode())