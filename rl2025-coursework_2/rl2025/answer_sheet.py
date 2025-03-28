
############################################################################################################
##########################            RL2023 Assignment Answer Sheet              ##########################
############################################################################################################

# **PROVIDE YOUR ANSWERS TO THE ASSIGNMENT QUESTIONS IN THE FUNCTIONS BELOW.**

############################################################################################################
# Question 2
############################################################################################################

def question2_1() -> str:
    """
    (Multiple choice question):
    For the Q-learning algorithm, which value of gamma leads to the best average evaluation return?
    a) 0.99
    b) 0.8
    return: (str): your answer as a string. accepted strings: "a" or "b"
    """
    answer = "a"  # TYPE YOUR ANSWER HERE "a" or "b"
    return answer


def question2_2() -> str:
    """
    (Multiple choice question):
    For the Every-visit Monte Carlo algorithm, which value of gamma leads to the best average evaluation return?
    a) 0.99
    b) 0.8
    return: (str): your answer as a string. accepted strings: "a" or "b"
    """
    answer = "a"  # TYPE YOUR ANSWER HERE "a" or "b"
    return answer


def question2_3() -> str:
    """
    (Multiple choice question):
    Between the two algorithms (Q-Learning and Every-Visit MC), whose average evaluation return is impacted by gamma in
    a greater way?
    a) Q-Learning
    b) Every-Visit Monte Carlo
    return: (str): your answer as a string. accepted strings: "a" or "b"
    """
    answer = "b"  # TYPE YOUR ANSWER HERE "a" or "b"
    return answer


def question2_4() -> str:
    """
    (Short answer question):
    Provide a short explanation (<100 words) as to why the value of gamma affects more the evaluation returns achieved
    by [Q-learning / Every-Visit Monte Carlo] when compared to the other algorithm.
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "In the MC agent, q(s,a) is updated with consideration for all future rewards using (gamma^i)*(ith future reward). "\
            "As i increases, if gamma = 0.8, gamma^i rapidly approaches zero, whereas when gamma = 0.99 this happens much slower. For eg gamma^10 = 0.1 and 0.8 for gamma = 0.8 and 0.99 respectively." \
            "In contrast, the QL method updates q(s,a) at each timestep with (gamma)*(the_max_q(s',a)."\
            "This means it doesn't experience the diminishing effect of a smaller gamma, how the MC algorithm does." \
            "In summary, the MC algorithm relies more heavily on learning that the current action is good based on the future consequences, so a lower gamma effects it's learning ability more."\


def question2_5() -> str:
    """
    (Short answer question):
    Provide a short explanation (<100 words) on the differences between the non-slippery and the slippery varian of the problem.
    by [Q-learning / Every-Visit Monte Carlo].
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "The evaluation returns across episodes are either 0 or 1 in the non-slippery variant. This makes sense since the agent is free to learn a deterministic policy that guarantees their success, (a return of 1). Until they learn such a policy they get a reward of 0." \
            "In contrast in the slippery variant, the returns are consistently numbers between 0 and 1 that tend to increase as the agent learns (with fluctuations)."\
            "The same set of actions made by the agent don't always lead to the same outcome in the slippery variant, making a deterministic policy less effective and the returns unpredictable."
    return answer


############################################################################################################
# Question 3
############################################################################################################

def question3_1() -> str:
    """
    (Multiple choice question):
    In the DiscreteRL algorithm, which learning rate achieves the highest mean returns at the end of training?
    a) 2e-2
    b) 2e-3
    c) 2e-4
    return: (str): your answer as a string. accepted strings: "a", "b" or "c"
    """
    answer = "a"  # TYPE YOUR ANSWER HERE "a", "b" or "c"
    return answer


def question3_2() -> str:
    """
    (Multiple choice question):
    When training DQN using a linear decay strategy for epsilon, which exploration fraction achieves the highest mean
    returns at the end of training?
    a) 0.99
    b) 0.75
    c) 0.01
    return: (str): your answer as a string. accepted strings: "a", "b" or "c"
    """
    answer = "c"  # TYPE YOUR ANSWER HERE "a", "b" or "c"
    return answer


def question3_3() -> str:
    """
    (Multiple choice question):
    When training DQN using an exponential decay strategy for epsilon, which epsilon decay achieves the highest
    mean returns at the end of training?
    a) 1.0
    b) 0.5
    c) 1e-5
    return: (str): your answer as a string. accepted strings: "a", "b" or "c"
    """
    answer = ""  # TYPE YOUR ANSWER HERE "a", "b" or "c"
    return answer


def question3_4() -> str:
    """
    (Multiple choice question):
    What would the value of epsilon be at the end of training when employing an exponential decay strategy
    with epsilon decay set to 1.0?
    a) 0.0
    b) 1.0
    c) epsilon_min
    d) approximately 0.0057
    e) it depends on the number of training timesteps
    return: (str): your answer as a string. accepted strings: "a", "b", "c", "d" or "e"
    """
    answer = "b"  # TYPE YOUR ANSWER HERE "a", "b", "c", "d" or "e"
    return answer


def question3_5() -> str:
    """
    (Multiple choice question):
    What would the value of epsilon be at the end of  training when employing an exponential decay strategy
    with epsilon decay set to 0.95?
    a) 0.95
    b) 1.0
    c) epsilon_min
    d) approximately 0.0014
    e) it depends on the number of training timesteps
    return: (str): your answer as a string. accepted strings: "a", "b", "c", "d" or "e"
    """
    answer = "e"  # TYPE YOUR ANSWER HERE "a", "b", "c", "d" or "e"
    return answer


def question3_6() -> str:
    """
    (Short answer question):
    Based on your answer to question3_5(), briefly  explain why a decay strategy based on an exploration fraction
    parameter (such as in the linear decay strategy you implemented) may be more generally applicable across
    different environments  than a decay strategy based on a decay rate parameter (such as in the exponential decay
    strategy you implemented).
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "With exponential decay, since epsilon_final = r*epsilon_start, if epsilon_start = 1 like above, then the value of epsilon_min that we want to decay towards is completely ignored - unless epsilon_min > r." \
            "In general the objective of scheuling epsilon is to reach a small probability to allow for proper exploitation." \
            "This means, to achieve different speeds of decay, we may need to compare numbers of different orders of magnitude eg 1e-5." \
            "This approach is less intuitive when compared to the exploration fraction approach, which the number of timesteps needed to reach the epsilon_min and thus the speed of decay."  # TYPE YOUR ANSWER HERE (100 words max)
    return answer


def question3_7() -> str:
    """
    (Short answer question):
    In DQN, explain why the loss is not behaving as in typical supervised learning approaches
    (where we usually see a fairly steady decrease of the loss throughout training)
    return: answer (str): your answer as a string (150 words max)
    """
    answer = "In DQN the loss is measured by the MSE between an estimate of the q-value function that is updated less frequently (the target) and an estimate that is updated more frequently (the value)." \
        "Fundamentally these are both estimates of the true function. The loss starting off small indicates that our two estimates are similar, not that we are close to predicting the true function. As the network learns, the loss increases dramatically because the target is updated closer to the true function, and the value network tries to fit this different estimate of the true function." \
        "For comparison, in supervised learning tasks the datapoints that we minimise the MSE for don't change position after a number of timesteps, so the loss tends to decrease." \
        "Lastly the somewhat stochastic behaviour that comes after aregular spike at later timesteps is due to the interconnectedness of the network - optimising for one batch of state-actions could harm another."  # TYPE YOUR ANSWER HERE (150 words max)
    return answer


def question3_8() -> str:
    """
    (Short answer question):
    Provide an explanation for the spikes which can be observed at regular intervals throughout
    the DQN training process.
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "The regular spikes very clearly occur every 2000 timesteps. This is because the target network is updated that frequently." \
    "In essence, the spikes are because the target q-values that the value network is learning are being changed - making them a moving target." \
    "The value network minimises the MSE with the previous target, but when this target is outdated, the value of the MSE dramatically increases and the value network has to start over - minimising the MSE between its output and the new target."  # TYPE YOUR ANSWER HERE (100 words max)
    return answer


############################################################################################################
# Question 5
############################################################################################################

def question5_1() -> str:
    """
    (Short answer question):
    Provide a short description (200 words max) describing your hyperparameter turning and scheduling process to get
    the best performance of your agents
    return: answer (str): your answer as a string (200 words max)
    """
    answer = ""  # TYPE YOUR ANSWER HERE (200 words max)
    return answer
