
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	# 假如s[0] = 13:34Allen, 可以寫s[0][:5]來取出字串的部分內容 => s[0][:5] = 13:34
	# s[0][2:4] = :3    , s[0][-2:] = en   , s[0][:-2] = 13:34All    , s[0][-5:-2] = All
	# "字串"可以當作"清單"來看待
	time = s[0][:5]
	name = s[0][5:]
	print(name)