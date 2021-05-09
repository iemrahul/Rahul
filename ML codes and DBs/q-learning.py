import numpy as np
gamma = 0.75
alpha = 0.9

location_to_state = {
    'L1' : 0,
    'L2' : 1,
    'L3' : 2,
    'L4' : 3,
    'L5' : 4,
    'L6' : 5,
    'L7' : 6,
    'L8' : 7,
    'L9' : 8
}
actions= [0,1,2,3,4,5,6,7,8]
rewards = np.array([[0,1,0,0,0,0,0,0,0],
                   [1,0,1,0,0,0,0,0,0],
                   [0,1,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,1,0,0],
                   [0,1,0,0,0,0,0,1,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,1,0],
                   [0,0,0,0,1,0,1,0,1],
                   [0,0,0,0,0,0,0,1,0]])

state_to_location = dict((state ,location) for location,state in location_to_state.items())
def get_optimal_route(start_location,end_location):
    rewards_new = np.copy(rewards)
    ending_state = location_to_state[end_location]
    rewards_new[ending_state,ending_state] = 999
    # ---This is Q-learning ALgorithm---
    Q = np.array(np.zeros([9,9]))
    for i in range(1000):
        current_state = np.random.randint(0,9)
        playable_actions = []
        for j in range(9):
            if rewards_new[current_state,j]>0:
                playable_actions.append(j)
        next_state = np.random.choice(playable_actions)
        TD = rewards_new[current_state,next_state] + gamma*Q[next_state,np.argmax(Q[next_state ,])] - Q[current_state,next_state]
        Q[current_state ,next_state] += alpha * TD
    route = [start_location]
    next_location = start_location
    while next_location != end_location:
        starting_state = location_to_state[start_location]
        next_state = np.argmax(Q[starting_state, ])
        next_location = state_to_location[next_state]
        route.append(next_location)
        start_location = next_location
    return route
print(get_optimal_route('L9','L6'
                             ''))