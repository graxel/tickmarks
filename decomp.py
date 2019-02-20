import math

def decomp(number):
    logarithm = math.log10(number)
    mantissa, exponent = math.modf(logarithm)
    if logarithm < 0:
        mantissa += 1
        exponent -= 1
    significand = math.pow(10, mantissa)
    return significand, exponent



x = [30, 34, 38, 45, 52, 65]
y = [2.4, 2.2, 4.3, 3.7, 5.0, 5.2]

hi = max(y)
lo = min(y)
diff = hi - lo

print(decomp(lo))
print(decomp(hi))
print(decomp(diff))
print('')
print('low: ', lo)
print('high:', hi)
print('diff:', diff)

sigdiff, expdiff = decomp(diff)
print(sigdiff, expdiff)
print(sigdiff, sigdiff*2)

for step,next_step in zip([1,2,5],[2,5,10]):
    print('trying', step)
    if sigdiff < step & step <= sigdiff*next_step/step:
        print(step,'worked')
        print(sigdiff, '<', step, '<=', sigdiff*next_step/step)




