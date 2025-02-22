# from pathlib import Path

# import yaml


# def rotate(matrix):
#     n = len(matrix)
#     m = len(matrix[0])
#     # Transpose the matrix
#     transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
#     # Reverse each row
#     rotated_matrix = [
#         [row[i] for i in range(m - 1, -1, -1)] for row in transposed_matrix
#     ]
#     return rotated_matrix


# data = yaml.safe_load(Path("bitmaps/pacman.yaml").read_text())

# wide = data["right"]["wide"]
# as_list = [list(w) for w in wide]

# fixed = rotate(as_list)

# re_list = ["".join(x) for x in fixed]

# for line in re_list:
#     print(f'  - "{line}"')
