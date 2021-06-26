def det(matrice: list):
    a_mat = [
        matrice[1][1:],
        matrice[2][1:]
    ]
    b_mat = [
        matrice[0][1:],
        matrice[2][1:]
    ]
    c_mat = [
        matrice[0][1:],
        matrice[1][1:]
    ]

    a_mul = a_mat[0][0] * a_mat[1][1] - a_mat[0][1] * a_mat[1][0]
    b_mul = b_mat[0][0] * b_mat[1][1] - b_mat[0][1] * b_mat[1][0]
    c_mul = c_mat[0][0] * c_mat[1][1] - c_mat[0][1] * c_mat[1][0]

    a, b, c = [matrice[i][0] for i in range(3)]

    return a*a_mul - b*b_mul + c*c_mul
