def countAndSay(res: str, n: int):
    for _ in range(n):
        new_res = ""
        counter = 0
        rep = 'a'
        for e in res:
            if e != rep:
                if counter > 0:
                    new_res += str(counter) + rep
        
                    counter = 0
                rep = e
            counter += 1
        
        new_res += str(counter) + rep

        res = new_res
    return res

print(len(countAndSay('1321131112', 40)))
print(len(countAndSay('1321131112', 50)))
