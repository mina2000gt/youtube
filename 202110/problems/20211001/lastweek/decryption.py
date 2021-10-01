c = 57353535740682374383891834841143962124987833902028485397962694323440595725298665423958702806083513671509037987642237781932497982200070354605438057469671233848680154720845910844930493471822046391364777885908866201458918218304098709442388543613855818401683157117671028110343867636469191492206037321660939919515
e = 3
n = 103915011925982866770089882960925972693342124743739756775359931566285049666214041684275695613452413047034247388159449807140780498656244725913233908161977596936695794447224316369828302366928704999167256969010568533857967571797417111939598807004191996642203292608635752931792294451293905954773570412281683528341

from Crypto.Util.number import long_to_bytes

i = 0
while True:
    print(i)
    upper = 2**1024
    lower = 2
    while upper - lower > 1:
        mid = (upper+lower)//2
        if mid*mid*mid > c:
            upper = mid
        else:
            lower = mid
    out = long_to_bytes(lower)
    if b'mctf' in out:
       print(out)
       break
    else:
       c += n
    i += 1