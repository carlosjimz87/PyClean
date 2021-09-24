names = ['Corey', 'Chris', 'Dave', 'Travis']

names2 = ['Peter', 'Clark', 'Wade', 'Bruce']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

if __name__ == '__main__':
    for i, name in enumerate(names, start=1):
        print(i, name)

    for name, hero, universe in zip(names2, heroes, universes):
        print(f'{name} is actually {hero} from {universe}')
