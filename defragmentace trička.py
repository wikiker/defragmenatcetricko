#modrá		-- .a
#žlutá		-- .b
#červená	-- .c
#zelená		-- .d
#margin		–– ?

sirkaObd	= 13
sirkaWin	= 800
vyskaWin	= 500
margin		= 3 #BÚNO
sirkaMar	= sirkaObd + margin
sance 		= 0
sancePlus	= 0.0003

import random,sys #<-- takto?, Tom řekl ok

def obdelnicek(x,y,barva, bůl):
	if bůl:
		mamToPosunoutInt = -3
	else:
		mamToPosunoutInt = 0
	return f"<rect class=\"{barva}\" width=\"{sirkaObd - mamToPosunoutInt}\" height=\"{sirkaObd}\" x=\"{x*sirkaMar + mamToPosunoutInt}\" y=\"{y*sirkaMar}\" z=\"100\"/>"

with open("defragmentace trička.svg") as soubor:
	nactenySoubor = soubor.read()
	#print(nactenySoubor[0:-6])
	#nactenySoubor = nactenySoubor[0:-6]
	posledniPosledniBarva = ""
	for yy in range(int(vyskaWin / sirkaMar)):
		posledniBarva = ""
		for xx in range(int(sirkaWin / sirkaMar)):
			sance += sancePlus
			#if(random.random()>sance):
			novaBarva = random.choice(["a", "b", "c", "d"])
			#else:
			#	novaBarva = posledniPosledniBarva
			sys.stderr.write(f"{novaBarva} -lol- {posledniBarva} \n")
			nactenySoubor += obdelnicek(xx, yy, novaBarva, novaBarva == posledniBarva)
			posledniBarva = novaBarva
			posledniPosledniBarva = posledniBarva
	nactenySoubor += '<rect class="a" width="200" height="80" x="0" y="414" z="420"/><rect class="b" x="200" y="414" width="200" height="80" z="420"/><rect class="c" x="400" y="414" width="200" height="80" z="420"/><rect class="d" x="600" y="414" width="200" height="80" z="420"/></svg>'
	print(nactenySoubor)
