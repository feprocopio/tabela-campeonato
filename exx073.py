times = ('Botafogo', 'Flamengo', 'Fluminense','Palmeiras',
         'Bragantino', 'Gremio','Athletico- Pr', 'Cuiaba', 'Internacional',
         'São Paulo','Atletico- MG', 'Cruzeiro','Fortaleza', 'Corinthians',
         'Goiais', 'Bahia', 'Santos', 'Coritiba', 'Vasco da Gama',
         'América- MG')
print(f'Lista de times do Campeonato Brasileiro: {times}')
print('=-' * 30)
print(f'Os 5 primeiros são {times[:5]}')
print('=-' * 30)
print(f'Os 4 ultimos são: {times[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabética {sorted(times)}')
print('=-' * 30)
print(f'Em que posição está o São Paulo: {times.index("São Paulo") +1}° colocado')