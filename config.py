"""
This file contains standard experiment parameters.
"""

WHICH_ACQ_FUNCS = [
    # 'predictive_entropy',
    'mutual_information',
    # 'variation_ratios',
    # 'mean_standard_deviation',
    'random'
]

# Experiment parameters
SEED = 1  # 1
N_RUNS = 2  # 3
TRAIN_SIZE = 20  # 20
VAL_SIZE = 100  # 1_000
DATA_PATH = '/Users/pascalpilz/Documents/Bsc Thesis/data/mnist/'
EXP_SAVE_PATH_BASE = './Experiment Results/'
MODEL_SAVE_PATH_BASE = '/Users/pascalpilz/Documents/Bsc Thesis/models/'

# Active learning parameters
N_ACQUISITION_STEPS = 25  # 100
N_SAMPLES_TO_ACQUIRE = 10  # 10
POOL_SUBSET_SIZE = 5_000  # 5_000
TEST_SUBSET_SIZE = 3_000  # 3_000
NUM_MC_SAMPLES = 32  # 64

# Training parameters
N_EPOCHS = 200  # 200
EARLY_STOPPING = -1  # 50
