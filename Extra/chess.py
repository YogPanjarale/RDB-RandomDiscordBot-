a1,a2,a3,a4,a5,a6,a7,a8='wr2','wh2','wb2','wk1','wq1','wb1','wh1','wr2'
b1,b2,b3,b4,b5,b6,b7,b8='wp1','wp2','wp3','wp4','wp5','wp5','wp6','wp7'
c1,c2,c3,c4,c5,c6,c7,c8='   ','   ','   ','   ','   ','   ','   ','   '
d1,d2,d3,d4,d5,d6,d7,d8='   ','   ','   ','   ','   ','   ','   ','   '
e1,e2,e3,e4,e5,e6,e7,e8='   ','   ','   ','   ','   ','   ','   ','   '
f1,f2,f3,f4,f5,f6,f7,f8='   ','   ','   ','   ','   ','   ','   ','   '
g1,g2,g3,g4,g5,g6,g7,g8='bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8'
h1,h2,h3,h4,h5,h6,h7,h8='br1','bh1','bb1','bk1','bq1','bb2','bh2','br2'
print("+---+---+---+---+---+---+---+---+")
print(f"|{a1}|{a2}|{a3}|{a4}|{a5}|{a6}|{a7}|{a8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{b1}|{b2}|{b3}|{b4}|{b5}|{b6}|{b7}|{b8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{c1}|{c2}|{c3}|{c4}|{c5}|{c6}|{c7}|{c8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{d1}|{d2}|{d3}|{d4}|{d5}|{d6}|{d7}|{d8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{e1}|{e2}|{e3}|{e4}|{e5}|{e6}|{e7}|{e8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{f1}|{f2}|{f3}|{f4}|{f5}|{f6}|{f7}|{f8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{g1}|{g2}|{g3}|{g4}|{g5}|{g6}|{g7}|{g8}|")
print("+---+---+---+---+---+---+---+---+")
print(f"|{h1}|{h2}|{h3}|{h4}|{h5}|{h6}|{h7}|{h8}|")
print("+---+---+---+---+---+---+---+---+")
def piecemove():
    x = input("enter a piece location")
    y = input("enter piece destination")
    
def move():
    a=['R1','H1','B1','K1','Q1','B2','H2','R2']
    b=['P1','P2','P3','P4','P5','P6','P7','P8']
    c=['z3',' ',' ',' ',' ',' ',' ',' ']
    d=[' ',' ',' ',' ',' ',' ',' ',' ']
    e=[' ',' ',' ',' ',' ',' ',' ',' ']
    f=[' ',' ',' ',' ',' ',' ',' ',' ']
    g=['P1','P2','P3','P4','P5','P6','P7','P8']
    h=['R1','H1','B1','K1','Q1','B2','H2','R2']
    col1 = input("enter a col id: \n")
    col2 = input("enter a col id: \n")
    piece1 = input("enter a piece id: \n")
    piece2 = input("enter a piece id: \n")
    col1 = str(col1).replace(f'{piece1}',' ')
    col2 = str(col2).replace(f'{piece2}',f'{piece1}')
    print("----------------------------------------")
    print(a)
    print("----------------------------------------")
    print(b)
    print("----------------------------------------")
    print(c)
    print("----------------------------------------")
    print(d)
    print("----------------------------------------")
    print(e)
    print("----------------------------------------")
    print(f)
    print("----------------------------------------")
    print(g)
    print("----------------------------------------")
    print(h)
    print("----------------------------------------")

