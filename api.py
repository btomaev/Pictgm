import uvicorn
from fastapi import Request, FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from bs4 import BeautifulSoup as bs
from datetime import date

app = FastAPI()

def getv(value):
    return value if value<=22 else value-22

@app.post("/calc")
async def calc(request: Request):
    try:
        data = await request.json()
        birth = data['birth']
        type = data['type']
        day, month, year = map(int, birth.split("."))

        a = getv(day)
        b = getv(month)
        c = getv(sum(map(int,list(str(year)))))

        d = getv(a+b+c)
        e = getv(2*d)
        f = getv(a+e)
        g = getv(a+f)
        i = getv(e+b)
        j = getv(i+b)
        h = getv(e+c)
        k = getv(h+c)
        l = getv(e+d)
        m = getv(l+d)
        n = getv(a+b)
        o = getv(d+c)
        p = getv(b+c)
        r = getv(a+d)
        s = getv(getv(n+p)+getv(o+r))
        t = getv(l+h)
        u = getv(t+h)
        w = getv(l+t)

        x = getv(b+d)
        y = getv(a+c)
        z = getv(n+o)

        star = getv(r+p)
        circle = getv(x+y)
        square = getv(z+star)

        result = {}

        if('a' in type):
            with open('matrix.html') as file:
                soup = bs(file, 'html.parser')

            soup.find(class_='im-b').string = str(b)
            soup.find(class_='im-i').string = str(j)
            soup.find(class_='im-q').string = str(n)
            soup.find(class_='im-h').string = str(i)
            soup.find(class_='im-r').string = str(p)
            soup.find(class_='im-a').string = str(a)
            soup.find(class_='im-g').string = str(g)
            soup.find(class_='im-f').string = str(f)
            soup.find(class_='im-eu').string = str(e)+"•"+str(s)
            soup.find(class_='im-j').string = str(h)
            soup.find(class_='im-k').string = str(k)
            soup.find(class_='im-c').string = str(c)
            soup.find(class_='im-o').string = str(u)
            soup.find(class_='im-n').string = str(t)
            soup.find(class_='im-p').string = str(w)
            soup.find(class_='im-t').string = str(r)
            soup.find(class_='im-l').string = str(l)
            soup.find(class_='im-s').string = str(o)
            soup.find(class_='im-m').string = str(m)
            soup.find(class_='im-d').string = str(d)

            result.update({'pictgm':str(soup)})

        if("b" in type):
            with open('table.html', encoding="utf-8") as file:
                table = file.read()
            
            table = table.replace("&12",str(c))
            table = table.replace("&13",str(d))
            table = table.replace("&11",str(getv(c+d)))
            table = table.replace("&21",str(k))
            table = table.replace("&22",str(m))
            table = table.replace("&23",str(getv(k+m)))
            table = table.replace("&31",str(h))
            table = table.replace("&32",str(l))
            table = table.replace("&33",str(getv(h+l)))
            table = table.replace("&41",str(s))
            table = table.replace("&42",str(e))
            table = table.replace("&43",str(getv(s+e)))
            table = table.replace("&51",str(f))
            table = table.replace("&52",str(i))
            table = table.replace("&53",str(getv(f+i)))
            table = table.replace("&61",str(g))
            table = table.replace("&62",str(i))
            table = table.replace("&63",str(getv(g+i)))
            table = table.replace("&71",str(a))
            table = table.replace("&72",str(b))
            table = table.replace("&73",str(getv(a+b)))

            table = table.replace("&ka",str(x))
            table = table.replace("&kb",str(y))
            table = table.replace("&kr",str(circle))
            table = table.replace("&ga",str(z))
            table = table.replace("&gb",str(star))
            table = table.replace("&gr",str(square))
            table = table.replace("&dr",str(getv(circle+square)))

            today = date.today()

            table = table.replace("&date",str(birth))
            table = table.replace("&age",str((today-date(year,month,day)).days//365))

            table = table.replace("&y1",str(today.year))
            table = table.replace("&y2",str(today.year+1))
            table = table.replace("&y3",str(today.year+2))

            table = table.replace("&ya",str(getv(getv(a+b)+getv(sum(map(int, list(str(today.year))))))))
            table = table.replace("&yb",str(getv(getv(a+b)+getv(sum(map(int, list(str(today.year+1))))))))
            table = table.replace("&yc",str(getv(getv(a+b)+getv(sum(map(int, list(str(today.year+2))))))))

            result.update({'table':table})

        return JSONResponse(result)
    except:
        return HTMLResponse(content="error", status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)