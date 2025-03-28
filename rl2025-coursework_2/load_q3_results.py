import pickle

LIN_SWEEP_RESULTS_FILE = "DQN-MountainCar-sweep-decay-linear-results.pkl"
with open(LIN_SWEEP_RESULTS_FILE, 'rb') as f:
    results_linear = pickle.load(f)

print("LINEAR DECAY RESULTS")
for run in results_linear:
    print(f"Run Name: {run.run_name}")
    print(f"Mean Final Return: {run.final_return_mean}+- {run.final_return_ste}")
    print(f"Final Epsilon: {run.run_data[-1]['final_epsilon']}")
    print("\n")

EXP_SWEEP_RESULTS_FILE = "DQN-MountainCar-sweep-decay-exponential-results.pkl"
with open(EXP_SWEEP_RESULTS_FILE, 'rb') as f:
    results_exponential = pickle.load(f)

print("EXPONENTIAL DECAY RESULTS")
for run in results_exponential:
    print(f"Run Name: {run.run_name}")
    print(f"Mean Final Return: {run.final_return_mean}+- {run.final_return_ste}")
    print(f"Final Epsilon: {run.run_data[-1]['final_epsilon']}")
    print("\n")