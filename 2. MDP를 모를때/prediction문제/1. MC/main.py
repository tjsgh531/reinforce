from Agent import Agent
from gridworld import GridWorld

def main():
    env = GridWorld()
    agent = Agent()
    data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    gamma = 1.0
    alpha = 0.0001

    for k in range(50000):
        done = False
        history = []
        while not done:
            action = agent.select_action()
            (x, y), reward, done = env.step(action)
            history.append((x, y, reward))
        env.reset()

        # 여기서 부터 수학적 계산이 들어가구만
        cum_reward = 0
        for transition in history[::-1]:
            x, y, reward = transition
            data[x][y] = data[x][y] + alpha * (cum_reward - data[x][y])
            cum_reward = reward + gamma * cum_reward
        
    # 출력
    for row in data:
        print(row)

main()
