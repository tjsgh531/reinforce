from gridworld import GridWorld
from QAgent import QAgent

def main():
    env = GridWorld()
    agent = QAgent()

    for n_epi in range(1000): # episode 1000개로 학습
        done = False
        history = []

        s = env.reset()

        print("start episode ", n_epi)
        while not done:
            a = agent.select_action(s)
            s_prime, r, done = env.step(a)
            history.append((s, a, r, s_prime))
            s = s_prime
        agent.update_table(history)
        agent.anneal_esp()

    agent.show_table()

main()