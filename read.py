data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了,總共有 ', len(data), '筆資料')

# my version
num = 0
i = 0
while True:
	num = num + len(data[i])
	i += 1
	if i >= len(data):
		break
num = num / len(data)
print('留言平均長度為', num)

# teacher's version
sum_len = 0
for d in data:
	sum_len += len(d)

print('留言平均長度為', sum_len / len(data))

# add篩選功能

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言字數小餘100')
print(new[0])

# add 篩選指定字樣留言
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言中有提到good')
print(good[0])

# list comprehension 清單快寫法
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言中有提到good')
