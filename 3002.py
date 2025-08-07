def cd(s,a,b):
  return int(s.replace(str(a),str(b)))
a,b=input().split()
mina=cd(a,6,5)
minb=cd(b,6,5)
print(mina+minb,end=" ")
maxa=cd(a,5,6)
maxb=cd(b,5,6)
print(maxa+maxb)