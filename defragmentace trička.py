#modrá		-- .a
#žlutá		-- .b
#červená	-- .c
#zelená		-- .d
#margin		–– ?

sirkaObd			= 13
margin				= 3
pricitam			= 0.1
sirkaMar			= sirkaObd + margin
sance 				= 0
sancePlus			= 0.0003
sirkaVelkyObdelnik	= (sirkaObd+margin)*12
sirkaWin			= sirkaVelkyObdelnik*4
vyskaWin			= 500

import random,sys #<-- takto?, Tom řekl ok

def obdelnicek(x,y,barva, bůl):
	if bůl:
		posunSirka = margin + pricitam
		posunXAxis = -margin
	else:
		posunSirka = pricitam
		posunXAxis = 0
	return f"<rect class=\"{barva}\" width=\"{sirkaObd + posunSirka}\" height=\"{sirkaObd}\" x=\"{x*sirkaMar + posunXAxis}\" y=\"{y*sirkaMar}\" z=\"100\"/>"

nactenySoubor = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {sirkaWin} {vyskaWin}">
	<defs>
		<style>.a{{fill:#339cd6;}}.b{{fill:#eedc64;}}.c{{fill:#bd5349;}}.d{{fill:#72a54f;}}</style>
	</defs>
	<title>defragmentace trička</title>
	<rect class="a" width="{sirkaWin}" height="494" x="0" y="0"/>'''
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
		#sys.stderr.write(f"{novaBarva} -lol- {posledniBarva} \n")
		nactenySoubor += obdelnicek(xx, yy, novaBarva, novaBarva == posledniBarva)
		posledniBarva = novaBarva
		posledniPosledniBarva = posledniBarva
		nactenySoubor += f'<rect class="a" width="{sirkaVelkyObdelnik - margin*0.5}" height="80" x="0" y="414"/>'
		nactenySoubor += f'<rect class="b" width="{sirkaVelkyObdelnik}" height="80" x="{1*sirkaVelkyObdelnik - margin*0.5}" y="414"/>'
		nactenySoubor += f'<rect class="c" width="{sirkaVelkyObdelnik}" height="80" x="{2*sirkaVelkyObdelnik - margin*0.5}" y="414"/>'
		nactenySoubor += f'<rect class="d" width="{sirkaVelkyObdelnik + margin*0.5}" height="80" x="{3*sirkaVelkyObdelnik - margin*0.5}" y="414"/>'
#nactenySoubor += f'<rect class="a" width="{sirkaVelkyObdelnik}" height="80" x="0" y="414" z="420"/><rect class="b" x="200" y="414" width="{sirkaVelkyObdelnik}" height="80" z="420"/><rect class="c" x="400" y="414" width="{sirkaVelkyObdelnik}" height="80" z="420"/><rect class="d" x="600" y="414" width="{sirkaVelkyObdelnik}" height="80" z="420"/></svg>'
nactenySoubor += "</svg>"
print(nactenySoubor)
