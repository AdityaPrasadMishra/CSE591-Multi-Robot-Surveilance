import sys
from ast import literal_eval

is3D = False

def main(fname, budget):
    f = open(fname,'r')
    alpha_a = 0.5
    alpha_d = 0.5
    pos = []
    util = []
    for l in f:
        if 'alpha(A)' in l:
            alpha_a = float(l.split(':')[1].strip())
        elif 'alpha(D)' in l:
            alpha_d = float(l.split(':')[1].strip())
        elif 'Co-ordinates' in l:
            x = list(literal_eval(l.split(':')[1].strip()))
            pos.append(x)
        elif 'Utility' in l:
            u = float(l.split(':')[1].strip())
            util.append(u)
    f.close()
    
    perimeter = []
    for building in pos:
        x_cords = [i[0] for i in building]
        y_cords = [i[1] for i in building]
        if is3D: howz_cords = [i[2] for i in building]

        l = max(x_cords) - min(x_cords)
        b = max(y_cords) - min(y_cords)
        if is3D: h = max(z_cords) - min(z_cords)

        if is3D: perimeter.append(4*(l+b+h))
        else: perimeter.append(2*(l+b))

    norm_perimeter_cost = [i/max(perimeter) for i in perimeter]
    norm_util = [i/max(util) for i in util]

    num_areas = len(util)
    s = ''
    s += '{}\n'.format(num_areas)
    s += '{}\n'.format(budget)

    #print defender's utility
    for i in range(num_areas):
        u_c = alpha_d * norm_util[i] - (1-alpha_d) * norm_perimeter_cost[i]
        u_u = -1 * alpha_d * norm_util[i]
        s += '{} {}\n'.format(u_c, u_u)

    #print attacker's utility
    for i in range(num_areas):
        u_c = -1 * alpha_a * norm_util[i] - (1-alpha_d) * norm_perimeter_cost[i]
        u_u = alpha_d * norm_util[i] - (1-alpha_d) * norm_perimeter_cost[i]
        s += '{} {}\n'.format(u_c, u_u)
    
    f = open('BSSG_input.txt','w') 
    f.write(s.strip())
    f.close()

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))