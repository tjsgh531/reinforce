from Agent import Agent
from gridworld import GridWorld

def main():
    env = GridWorld()
    agent = Agent()
    data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    gamma = 1.0
    alpha = 0.01

    for k in range(50000):
        done = False
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            
            # 한번 움직이고 바로 업데이트(수학적 계산 여기서 해유)
            data[x][y] = data[x][y] + alpha * (reward + gamma * data[x_prime][y_prime] - data[x][y])
        env.reset()

    # 출력
    for row in data:
        print(row)

main()
