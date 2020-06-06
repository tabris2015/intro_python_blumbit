primero_A = {'juan', 'alex', 'edgar', 'arturo'}
primero_B = {'julia', 'diana', 'paola', 'oscar'}
equipo_volley = {'alex', 'arturo', 'paola', 'raul'}

# alex, arturo
print(f'equipo de volley del primero A: {primero_A & equipo_volley}')
# juan, alex, edgar, arturo, julia, diana, paola, oscar
print(f'todos los del primero: {primero_A | primero_B}')
# julia, diana, oscar
print(f'primero B que no estan en volley: {primero_B - equipo_volley}')

prim_A = ['juan', 'alex', 'edgar', 'arturo']

letra_a = [est for est in prim_A if est[0].lower() == 'a']
print(letra_a)