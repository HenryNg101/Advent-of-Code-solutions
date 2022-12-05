f = open("input")
content = f.read()

st = [
  ['Z','J','G'],
  ['Q','L','R','P','W','F','V','C'],
  ['F','P','M','C','L','G','R'],
  ['L','F','B','W','P','H','M'],
  ['G','C','F','S','V','Q'],
  ['W','H','J','Z','M','Q','T','L'],
  ['H','F','S','B','V'],
  ['F','J','Z','S'],
  ['M','C','D','P','F','H','B','T']
]

for line in content.split('\n'):
  arr = line.split(' ')
  if(len(arr) != 3):
    continue
  arr = [int(x) for x in arr]
  for _ in range(arr[0]):
    st[arr[2]-1].append(st[arr[1]-1].pop())

res = ""
for e in st:
  res += e[-1]
print(res)
