characters = [('Bowser',10,0,0,10,10,10,10,0,0,0,0),('Donkey Kong',8,1,1,9,9,9,9,2,2,2,2),('Wario',9,0,0,10,10,10,10,1,1,1,1)]
fullKarts = [('Standard Kart',2,4,4,3,3,3,3,3,2,3,3),('Pipe Frame',1,6,6,1,3,1,1,5,4,4,2),('Mach 8',3,3,4,3,3,5,4,2,2,4,2),('Cat Cruiser',2,5,5,2,3,4,4,4,2,3,4),('Prancer',1,2,3,4,3,3,3,3,3,2,3),('Biddybuggy',0,7,7,0,1,2,1,5,4,5,4),('Landship',0,6,6,1,5,0,2,4,5,2,3),('Sneeker',2,2,3,4,2,3,3,3,2,3,2),('Standard Bike',1,5,5,2,2,4,3,4,3,4,3),('Blue Falcon',0,3,3,4,2,4,3,2,3,5,1)]
optimisedKarts = [('Pipe Frame',1,6,6,1,3,1,1,5,4,4,2),('Cat Cruiser',2,5,5,2,3,4,4,4,2,3,4),('Biddybuggy',0,7,7,0,1,2,1,5,4,5,4),('Landship',0,6,6,1,5,0,2,4,5,2,3),('Standard Bike',1,5,5,2,2,4,3,4,3,4,3)]
fullTyres = [('Standard',2,4,3,2,3,2,3,3,3,3,3),('Roller',0,6,6,0,3,0,3,4,4,4,4),('Slim',2,2,2,3,2,4,2,4,4,3,4),('Button',0,5,5,1,2,2,2,3,3,4,2),('Sponge',1,4,4,1,1,1,4,2,1,2,3)]
optimisedTyres = [('Roller',0,6,6,0,3,0,3,4,4,4,4),('Button',0,5,5,1,2,2,2,3,3,4,2),('Sponge',1,4,4,1,1,1,4,2,1,2,3)]
fullGliders = [('Super Glider',1,1,1,1,1,0,2,1,0,1,1),('Cloud Glider',0,2,2,0,1,1,1,1,0,1,2),('Wario Wing', 2,1,1,1,0,1,2,1,1,0,1),('Peach Parasol',1,2,2,0,0,1,1,1,1,0,2)]
optimisedGliders = [('Cloud Glider',0,2,2,0,1,1,1,1,0,1,2),('Peach Parasol',1,2,2,0,0,1,1,1,1,0,2)]
combos = []

multL = 0.645
multW = 0.032
multA = 0.251
multG = 0.072

def pr(x): #swaps spaces to _ if printableMode == true
    if redditMode:
        print(x)
    elif printableMode:
        print(" "+x.replace(" ","_"))
    else:
        print(" "+x) #looks nicer with space in front of each line

def p(x):
    print(x)

def ps(x):
    if redditMode:
        print(x)
    else:
        print(" "+x)

printableMode = False #enable this when copy+pasting somewhere (eg email/reddit); looks ugly but some websites/apps don't preserve multiple spaces
redditMode = True #formats output in reddit-table format
optimised = True #only includes the very best combos, if false many are still excluded
sortByMT = True #sort by miniturbo first, rather than MT+SX; better with optimised=False

if optimised:
    karts = optimisedKarts
    tyres = optimisedTyres
    gliders = optimisedGliders
else:
    karts = fullKarts
    tyres = fullTyres
    gliders = fullGliders

if redditMode:
    sc = "|"
else:
    sc = " "

print()
if redditMode:
    ps("Welcome to gurneyguy101's MK8DX kart combo calculator V3!")
    p("\n|**Name|Kart|Tyre|Glider|WG|AC|MT|SX|TX|MT+SX|Total**|")
    p("|---|---|---|---|---|---|---|---|---|---|---|-----|")
elif printableMode:
    ps("Welcome to Henry's MK8DX kart combo calculator V3!")
    p("\n Name__________Kart____________Tyre_______Glider__________WG__AC__MT___SX____TX_____MT+SX___Total\n")
else:
    ps("Welcome to Henry's MK8DX kart combo calculator V3!")
    p("\n Name          Kart            Tyre       Glider          WG  AC  MT   SX    TX     MT+SX   Total\n")
  
for character in characters:
    for kart in karts:
        for tyre in tyres:
            for glider in gliders:
                comboWG = character[1]+kart[1]+tyre[1]+glider[1]
                comboAC = character[2]+kart[2]+tyre[2]+glider[2]
                comboMT = character[3]+kart[3]+tyre[3]+glider[3]
                comboSL = character[4]+kart[4]+tyre[4]+glider[4]
                comboSW = character[5]+kart[5]+tyre[5]+glider[5]
                comboSA = character[6]+kart[6]+tyre[6]+glider[6]
                comboSG = character[7]+kart[7]+tyre[7]+glider[7]
                comboTL = character[8]+kart[8]+tyre[8]+glider[8]
                comboTW = character[9]+kart[9]+tyre[9]+glider[9]
                comboTA = character[10]+kart[10]+tyre[10]+glider[10]
                comboTG = character[11]+kart[11]+tyre[11]+glider[11]
                comboSX = "{:.1f}".format((comboSL*multL)+(comboSW*multW)+(comboSA*multA)+(comboSG*multG),1)
                comboTX = "{:.1f}".format((comboTL*multL)+(comboTW*multW)+(comboTA*multA)+(comboTG*multG),1)
                combos.append((character[0]+","+kart[0]+","+tyre[0]+","+glider[0]+","+str(comboWG)+","+str(comboAC)+","+str(comboMT)+","+comboSX+","+comboTX).split(","))

if sortByMT:
    sortedCombos = sorted(combos, key=lambda x: (float(x[6]), float(x[6])+float(x[7]), float(x[4])+float(x[5])+float(x[6])+float(x[7])+float(x[8])), reverse=True)
else:
    sortedCombos = sorted(combos, key=lambda x: (float(x[6])+float(x[7]), float(x[4])+float(x[5])+float(x[6])+float(x[7])+float(x[8])), reverse=True)

for i in sortedCombos:
    gap1 = 14-len(i[0]) #normalising gaps for better readability
    gap2 = 16-len(i[1])
    gap3 = 11-len(i[2])
    gap4 = 14-len(i[3])
    gap5 = 2-len(str(i[4]))
    gap6 = 2-len(str(i[5]))
    gap7 = 2-len(str(i[6]))
    gap8 = 4-len(str(i[7]))
    gap9 = 6-len(str(i[8]))
    gap10 = 2
    if redditMode:
        pr("|"+i[0]+"|"+i[1]+"|"+i[2]+"|"+i[3]+"|"+str(i[4])+"|"+str(i[5])+"|"+str(i[6])+"|"+str(i[7])+"|"+str(i[8])+"|"+str(float(i[6])+float(i[7]))+"|"+str("{:.1f}".format(float(i[4])+float(i[5])+float(i[6])+float(i[7])+float(i[8])))+"|")
    else:
        pr(i[0]+gap1*" "+i[1]+gap2*" "+i[2]+gap3*" "+i[3]+gap4*" "+"  "+str(i[4])+gap5*" "+"  "+str(i[5])+gap6*" "+"  "+str(i[6])+gap7*" "+"  "+str(i[7])+gap8*" "+"  "+str(i[8])+gap9*" "+"  "+str(float(i[6])+float(i[7]))+gap10*" "+"  "+str("{:.1f}".format(float(i[4])+float(i[5])+float(i[6])+float(i[7])+float(i[8]))))

print("\n")
ps("Equivalents:\n")
ps("Characters")
ps("Bowser: Morton")
ps("Donkey Kong: Waluigi, Roy")
ps("Wario: Dry Bowser\n")
ps("Karts")
ps("Standard Kart: The Duke, 300 SL Roadster")
ps("Pipe Frame: Varmint, City Tripper")
if not optimised:
    ps("Mach 8: Sports Coupe, Inkstriker")
ps("Cat Cruiser: Comet, Yoshi Bike, Teddy Buggy")
if not optimised:
    ps("Prancer: Sport Bike, Jet Bike")
ps("Biddybuggy: Mr. Scooty")
ps("Landship: Streetle")
if not optimised:
    ps("Sneeker: Gold Standard, Master Cycle")
ps("Standard Bike: Flame Rider, Wild Wiggler, W 25 Silver Arrow")
if not optimised:
    ps("Blue Falcon: Splat Buggy")
print()
ps("Tyres")
if not optimised:
    ps("Standard: Blue Standard, GLA Tires")
ps("Roller: Azure Roller")
if not optimised:
    ps("Slim: Wood, Crimson Slim")
ps("Button: Leaf tyres")
ps("Sponge: Cushion\n")
ps("Gliders")
if not optimised:
    ps("Super Glider: Waddle Wing, Hylian Kite")
ps("Cloud Glider: Parachute, Flower Glider, Paper Glider")
if not optimised:
    ps("Wario Wing: Plane Glider, Gold Glider, Paraglider")
ps("Peach Parasol: Parafoil, Bowser Kite, MKTV Parafoil")

print("\n")
ps("This is a list of character/kart combinations, sorted by miniturbo strength, where suboptimal combos and duplicates (though noted above) are omitted.")
ps("The key to the stats is as follows: WG = weight, AC = acceleration, MT = miniturbo, SX = speed*, TX = handling*")
ps("*These comprise of their 4 composite stats, averaged and weighted by surface prevalence (method for determining this is found below)")
ps("Some stats have been combined/removed for ease of use, as their omission makes little difference to overall strength")
ps("The two most important stats and miniturbo and speed, hence the focus on them\n")
ps("Credit for the raw data: Super Mario Wiki (https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics)\n")
