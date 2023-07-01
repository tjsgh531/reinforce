import copy
from gridword import GridWorld

def main():
    env = GridWorld()
    data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    data_prime = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    pi = 0.25
    gamma = 1.0
    transitionP = 1.0
    reward = -1

    for k in range(50000):
        for x in range(4):
            for y in range(4):
                if x == 3 and y == 3:
                    continue

                move_result = env.move(x, y)

                v_prime_sum = 0
                for x_prime, y_prime in move_result:
                    v_prime_sum += pi * (reward + gamma * transitionP * data[x_prime][y_prime])
                
                data_prime[x][y] = v_prime_sum
        
        data = copy.deepcopy(data_prime)
    
    # 출력
    for row in data:
        print(row)

main()