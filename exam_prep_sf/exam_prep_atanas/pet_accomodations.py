def accommodate_new_pets(capacity, weight, *pets):
    result = []
    pets_map = {}

    for pet_type, pet_weight in pets:

        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break

        if pet_weight > weight:
            continue

        if pet_type not in pets_map:
            pets_map[pet_type] = 0
        pets_map[pet_type] += 1
        capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}")

    result.append("Accommodated pets:")

    for pet_typ, pet_count in sorted(pets_map.items()):
        result.append(f"{pet_typ}: {pet_count}")

    return '\n'.join(result)
