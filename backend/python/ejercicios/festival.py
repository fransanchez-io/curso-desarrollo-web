### COMPARATIVA DE HORARIOS##

escenarios = {
    "mainstage": {
        1: ("everything always", "alesso", "afrojack", "tiesto", "subtronincs", "timmy trumpet", "sam felot"),
        2: ("hardwell", "skrillex", "axwell", "anyma and solomun", "armin van buuren", "steve aoki", "joel corry", "frank walker", "kapunchon", "gil glaze"),
        3: ("martin garrix", "zedd", "gruffin", "special guest", "sonny fodera", "morten", "odd mob", "mykris", "jev")
    },
    "worldwidestage": {
        1: ("armin van buuren con maddix y  oliver heldens","armin van buuren","oliver heldens","maddix","nifra","ruben de ronde","schrotthagen"),
        2: ("deadmaus","pendulum","atliens","hedex","crankdat","knife party","maradua","wilkinson","barclay crenshaw","ltj bukem","level up", "dillon nathaniel"),
        3: ("deadmaus","nightmre","sullivan king","peekaboo","dimension","andy c","alleycvt","jessica auduffred","flux pavilion", "doctor p","sota","julian cross")
    },
    "resistancemegastage": {
        1: ("charlotte de wite","boris brejcha","artbat","mis monique","marco faraone","mar-t"),
        2: ("carl crox","adam beyer","richie hawtin","stephan boozin"," jorisvoorn","dubfire","marc romboy","carl crox y christopher coe"),
        3: ("solomun","four tet","mau p","chloe caillet", "rafael cerato")
    },
    "resitancecovestage": {
        1: ("eli brown","patrick topping","nick fanciulli","josh wink","joyhauser"),
        2: ("massand","chris avantgarde","kevin de vries","korolova","kasia","olympe","mortiz hofbauer","maga"),
        3: ("buci nireb","i hate models","999999999","popof x space 92","charlie sparks"," juliet fox","nusha")
    },
    "livestage": {
        1: ("zeds dead","pendulum","chase and status","nero","modestep","skepsis"),
        2: ("gesaffelstein","kshmr","tokimonsta","becky hill","voiish"),
        3: ("above beyond","lszee","said the sky","infected mushroom","afrobeta")
    },
    "umfstage": {
        1: ("?b2b","ahadadream","vtss","ketbois69","skream","interplanetary criminal","partiboi69","juicy romance"),
        2: ("mr.black","terra","shlomo","vini vici","blazy","omiki","alchimyst","fernanda pistelli","coexist","khromata","zorza","roe revolution"),
        3: ("kami","roller","da tweekaz","brennan heart","coone","sub zero project","the purge","adrenalize","darksiderz")
    },
    "oasisstage": {
        1: ("marco ninni","jack vice","purple","los de la vega","ben nigrelli","richard fraioli","jimmie page","dj ideal","wiener bros","andy ares"),
        2: ("metaphysical","tone abstract","tak shak","wags","lemony snkickettes","audio sal","rod b","sandro bianchi","like hunter","bassett","andy pate","josh wetherington","christopher james","jay p","soul goodman","dabura","omar deaz","juno","cj","marvin delgado"),
        3: ("victor cardenas","luca testa","de xenia","alex pizzuti","tank","jda","x-con","wyzzard","bill kelly","rodrigo vieira","adam de great","abel","cvmrn","maahez")
    }
}

print("Hola bebe, esto es para ti :*")
entrada = input("¿Qué artistas quieres ver? (separa por comas): ").strip().lower()
artistas_buscar = [artista.strip() for artista in entrada.split(",")]  

encontrados = []


for artista in artistas_buscar:
    encontrado = False
    for escenario, dias in escenarios.items():
        for dia, artistas in dias.items():
            if artista in map(str.lower, artistas):  
                orden = artistas.index(next(a for a in artistas if a.lower() == artista)) + 1
                encontrados.append(f"{artista.title()} estará en **{escenario.replace('_', ' ').title()}** el día {dia} en la posición {orden}.")
                encontrado = True
    if not encontrado:
        encontrados.append(f"{artista.title()} no está en la lista de artistas del festival.")


print("\n".join(encontrados))
print("Espero que sea loque buscaras bb")