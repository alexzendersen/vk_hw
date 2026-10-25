def feed_animals(animals, portions):
    animals = sorted(animals)
    portions = sorted(portions)
    fed = 0

    for portion in portions:
        if fed == len(animals):
            break

        if portion >= animals[fed]:
            fed += 1

    return fed


animals = [1, 2, 3]
portions = [1, 1, 3]
print(feed_animals(animals, portions))
