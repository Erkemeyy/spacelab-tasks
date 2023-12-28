def battle(zombies, plants):
    zombies_attack_rate = sum(zombies)
    plants_attack_rate = sum(plants)
    zombies_soldiers = len(zombies)
    plants_soldiers = len(plants)

    alive_zombies = 0
    alive_plants = 0

    if zombies_soldiers > plants_soldiers:
        for i in range(len(zombies)):
            try:
                if zombies[i] > plants[i]:
                    alive_zombies += 1
                elif zombies[i] == plants[i]:
                    pass
                else:
                    alive_plants += 1
            except IndexError:
                alive_zombies += 1
    else:
        for i in range(len(plants)):
            try:
                if plants[i] > zombies[i]:
                    alive_plants += 1
                elif zombies[i] == plants[i]:
                    pass
                else:
                    alive_zombies += 1
            except IndexError:
                alive_zombies += 1

    print(alive_zombies)
    print(alive_plants)
    if alive_plants > alive_zombies:
        return True
    elif alive_plants == alive_zombies:
        if plants_attack_rate > zombies_attack_rate:
            return True
        elif plants_attack_rate == zombies_attack_rate:
            return True
        else:
            return False
    else:
        return False


print(battle(zombies=[1, 3, 5, 7], plants=[1, 3, 7, 5]))
