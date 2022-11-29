UNIT = 50

p = [
    [0, 1],
    [1, 1],
    [1, 0],
    [0, 0],
    [0.5, 1],
    [1, 0.5],
    [0.5, 0],
    [0, 0.5],
    [0.5, 0.5],  # additional middle point
]

NORMAL_PATTERN = [
    [],                                 # 0000
    p[0] + p[4] + p[7],           # 0001
    p[1] + p[5] + p[4],           # 0010
    p[0] + p[1] + p[5] + p[7],    # 0011
    p[2] + p[6] + p[5],           # 0100
    p[0] + p[4] + p[5] + p[2] + p[6] + p[7],  # 0101
    p[1] + p[2] + p[6] + p[4],                    # 0110
    p[0] + p[1] + p[2] + p[6] + p[7],             # 0111
    p[3] + p[7] + p[6],                           # 1000
    p[0] + p[4] + p[6] + p[3],                    # 1001
    p[1] + p[5] + p[6] + p[3] + p[7] + p[4],  # 1010
    p[0] + p[1] + p[5] + p[6] + p[3],             # 1011
    p[2] + p[3] + p[7] + p[5],                    # 1100
    p[0] + p[4] + p[5] + p[2] + p[3],             # 1101
    p[1] + p[2] + p[3] + p[7] + p[4],             # 1110
    p[0] + p[1] + p[2] + p[3],                           # 1111
]


GRID_PATTERN = [
    [],                                 # 0000
    p[0] + p[4] + p[8] + p[7],           # 0001
    p[1] + p[5] + p[8] + p[4],           # 0010
    p[0] + p[1] + p[5] + p[7],    # 0011
    p[2] + p[6] + p[8] + p[5],           # 0100
    p[0] + p[4] + p[6] + p[2] + p[5] + p[7],  # 0101
    p[1] + p[2] + p[6] + p[4],                    # 0110
    p[0] + p[1] + p[2] + p[6] + p[8] + p[7],             # 0111
    p[3] + p[7] + p[8] + p[6],                           # 1000
    p[0] + p[4] + p[6] + p[3],                    # 1001
    p[1] + p[5] + p[7] + p[3] + p[6] + p[4],  # 1010
    p[0] + p[1] + p[5] + p[8] + p[6] + p[3],             # 1011
    p[2] + p[3] + p[7] + p[5],                    # 1100
    p[0] + p[4] + p[8] + p[5] + p[2] + p[3],             # 1101
    p[1] + p[2] + p[3] + p[7] + p[8] + p[4],             # 1110
    p[0] + p[1] + p[2] + p[3],                           # 1111
]

PATTERNS = {
    "normal": NORMAL_PATTERN,
    "grid": GRID_PATTERN,
}

