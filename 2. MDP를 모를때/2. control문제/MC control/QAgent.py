import random
import numpy as np

class QAgent():
    def __init__(self):
        self.q_table = np.zeros((5, 7, 4)) # q 밸류를 저장 -> prediction 문제에서는 data[[0,0,0,0] ...] 했던 부분을 np로 구현한 듯
        self.eps = 0.9
        self.alpha = 0.01
        self.gamma = 1.0

    def select_action(self, s):
        # eps-greedy로 액션 선택
        x, y = s
        coin = random.random()
        if coin < self.eps: # 탐색을한다.
            action = random.randint(0,3)
        else: # 실행을 q-value greedy 하게 실행
            action_val = self.q_table[x,y,:] # x행 y열에 있는 
            action = np.argmax(action_val)
        return action
    
    def update_table(self, history):
        # q table을 업데이트
        cum_reward = 0
        for transition in history[::-1]:
            s, a, r, s_prime = transition
            x, y = s
            # 몬테 카를로 방식으로 업데이트
            self.q_table[x, y, a] = self.q_table[x, y, a] + self.alpha * (cum_reward - self.q_table[x, y, a])
            cum_reward = self.gamma * cum_reward + r
    
    # esp value 진행 할 수록 낮춰 주어 탐색 비율보다 실행 비율을 높이는 것
    def anneal_esp(self):
        self.eps -= 0.03
        self.eps = max(self.eps, 0.1) # 0.1보다는 작아지지 않게 만드는 코드

    #결과는 특정 상태에서 어떤 action을 하는지를 나타냄 => 0, 1, 2, 3 숫자로 결과 나옴
    def show_table(self):
        q_lst = self.q_table.tolist()
        data = [["","","b","","","",""],["","","b","","","",""],["","","b","","b","",""],["","","","","b","",""],["","","","","b","",""]]
        for row_idx in range(len(q_lst)):
            row = q_lst[row_idx]
            for col_idx in range(len(row)):
                col = row[col_idx]
                action = np.argmax(col)
                if action == 0:
                    arrow = "←"
                elif action == 1 :
                    arrow = "↑"
                elif action == 2:
                    arrow = "→"
                elif action == 3:
                    arrow ="↓"

                data[row_idx][col_idx] = arrow
        
        for row in data:
            print(row)

