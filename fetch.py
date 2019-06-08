from urllib import request


def p(id):
    x=str(id)
    while len(x)<3:
        x="0"+x
    return x

def get(id):
    try:
            
        url="http://media.52poke.com/assets/sprite/b2w2/front/"+p(id)+".gif"
        print("Fetching:"+url)

        l=None
        cc=5
        while True:
            try:
                l=request.urlopen(url,timeout=5)
                
                break
            except Exception as err:
                print("Open error {0}".format(err))
                cc-=1
                print("Retrying Left:",cc)
                if cc==0:
                    raise Exception('retry failed')
            
        print("Open success")
        f=open("front/"+str(id)+".gif","wb")
        f.write(l.read())
        f.flush()
        f.close()
        print("Done!")
    except Exception as err:
        print("Failed! {0}".format(err))
        return False

limit=int(input("Limit to="))

frm=int(input("From="))

cnt=frm
while True:
    print("====="+str(cnt)+"====")
    if get(cnt)==False:
        break
    cnt+=1
    if cnt>limit:
        break
print("Done! Total "+str(cnt-1)+" Pokemons are saved!")

print("Compresing HTML")
f=open("front/compress.html","w")
f.write("""
<html>
<body>
<h1>Compress Object</h1>
""")
for i in range(1,cnt):
    f.write('<img src="'+str(i)+'.gif"></img>')
f.write("""
</body></html>
""")
f.close()
