import pandas as pd
import numpy as np
import time

N_STATES = 6 #state number
ACTIONS = ['left','right']
EPSILON = 0.9
GAMMA = 0.9
ALPHA = 0.1
MAX_EPISODES = 13
FRESH_TIME = 0.3

def build_q_table(n_states,actions):
	table = pd.DataFrame(np.zeros((n_states,len(actions))),columns=actions)
	return table

def choose_action(state,qtable):
	state_actions = qtable.iloc[state,:]
	if np.random.uniform() > EPSILON or state_actions.all() == 0:
		action = np.random.choice(ACTIONS)
	else:
		action = state_actions.argmax()
	return action

def get_env_feedback(S,A):
	if  A == 'right':
		if S == N_STATES-2:
			S_ = 'terminal'
			R = 1
		else:
			S_ = S + 1
			R = 0
	else:
		R = 0
		if S == 0:
			S_ = 0
		else:
			S_ = S - 1
	return S_, R

def update_env(S,episode,step_counter):
	env_list = ['-']*(N_STATES - 1) + ['T']
	if S == 'terminal':
		interaction = 'Episode %s:total_steps=%d'%(episode+1,step_counter)
		print('\r{}'.format(interaction),end='')
		time.sleep(0.2)
		print('\r                       ',end='')
	else:
		env_list[S] = 'O'
		interaction = ''.join(env_list)
		print('\r{}'.format(interaction),end='')
		time.sleep(FRESH_TIME)

def rl():
	q_table = build_q_table(N_STATES,ACTIONS)
	for episode in range(MAX_EPISODES):
		step_counter = 0
		S = 0
		is_terminal = False
		update_env(S,episode,step_counter)
		while not is_terminal:
			A = choose_action(S,q_table)
			S_,R = get_env_feedback(S,A)
			q_predict = q_table.loc[S,A]
			if S_ != 'terminal':
				q_target = R + GAMMA*q_table.iloc[S_,:].max()
			else:
				q_target = R
				is_terminal = True
			q_table.loc[S,A] += ALPHA*(q_target-q_predict)
			S = S_
			update_env(S,episode,step_counter+1)
			step_counter += 1
	return q_table

if __name__ == '__main__':
	q_table = rl()
	print('q_table:{}'.format(q_table))

