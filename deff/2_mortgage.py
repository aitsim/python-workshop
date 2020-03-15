principale = 2002020
_payment = 30303
rate = 0.05
total_paid = 0

out = open('test.txt','r')
print(out.read())
# print('{:>15s} {:>15s} {:>10s}'.format('interest', "principale", "payment"),file=out)
#
# while principale > 0:
#         if rate > 1:
#             interest = principale * (rate / 12)
#         else:
#             interest = principale * (rate / 6)
#         principale = principale + interest -_payment
#         total_paid += _payment
#         print('{:>15.2f} {:>15.2f} {:>10d}'.format(interest, principale, _payment), file=out)

out.close()

# print(interest,principale,_payment,total_paid)




#string

a = "hello mohamed   "
b = "     zzzz   zz   "



print(a[0])

print(a[7:9])
print(a[:9])

print(a[-5:])
print(len(a))
print(a+b)
# z = a.strip()
print(a.replace(" ", ","))
print(a.split(" "))



z = b.strip()
print(z)