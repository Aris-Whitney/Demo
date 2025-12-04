
m = 10      # bit array size
bit_array = [0] * m

# Hard-coded hash outputs for consistency
# Each word returns 2 hash positions
def get_hashes(item):
    if item == "cat":
        return [1, 4]
    if item == "dog":
        return [2, 4]
    if item == "bird":
        return [6, 8]

    # "fish" overlaps intentionally → False positive
    if item == "fish":
        return [1, 2]   # both already set from cat/dog

    # "zebra" must NOT overlap → True negative
    if item == "zebra":
        return [7, 9]   # at least one of these = 0

    # fallback for unknown words
    return [hash(item) % m, (hash(item) * 3) % m]


def add(item):
    for h in get_hashes(item):
        bit_array[h] = 1


def check(item):
    for h in get_hashes(item):
        if bit_array[h] == 0:
            return False
    return True


# ---------------------
# DEMO
# ---------------------

add("cat")
add("dog")
add("bird")

print("Bit array:", bit_array)
print()

print("'cat':", check("cat"))
print("'dog':", check("dog"))
print("'bird':", check("bird"))
print("'fish':", check("fish"))     # FALSE POSITIVE
print("'zebra':", check("zebra"))   # CORRECT NEGATIVE

