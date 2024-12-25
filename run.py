import sys
import os
import argparse

from acrobot_dql.run import run_acrobot_dql
from acrobot_ppo_a2c.run import run_acrobot_a2c, run_acrobot_ppo
from car_racing_dql_a2c.run import run_car_a2c, run_car_dql
from car_racing_ppo.run import run_car_ppo

# Clear the tensorflow errors
os.system('clear')
sys.stdout.flush()

def validate_model(model):
    valid_models = ["DQL", "PPO", "A2C"]
    if model not in valid_models:
        raise argparse.ArgumentTypeError(f"Invalid model '{model}'. Choose from {valid_models}.")
    return model

def validate_environment(env):
    valid_envs = ["Acrobot", "Car"]
    if env not in valid_envs:
        raise argparse.ArgumentTypeError(f"Invalid environment '{env}'. Choose from {valid_envs}.")
    return env

def main():
    parser = argparse.ArgumentParser(description="Check model and environment inputs.")
    parser.add_argument(
        "--model", 
        type=validate_model, 
        required=True, 
        help="Specify the model type. Options: DQL, PPO, A2C."
    )
    parser.add_argument(
        "--env", 
        type=validate_environment, 
        required=True, 
        help="Specify the environment. Options: Acrobot, Car."
    )

    parser.add_argument(
        "--train", 
        action="store_true", 
        help="Enable evaluation mode."
    )
    parser.add_argument(
        "--test", 
        action="store_true", 
        help="Enable test mode."
    )
    parser.add_argument(
        "--visualize", 
        action="store_true", 
        help="Enable visualization mode."
    )
    
    parser.add_argument(
        "--folder",
        type=str,
        default=None,  # You can change this default path
        help="Specify the folder path where the results (models/logs) will be saved."
    )

    args = parser.parse_args()
    
    func_args = {
        
    }

    if args.folder:
        func_args['folder'] = args.folder
        
    modes = []

    if args.train == True:
        modes.append('train')
    if args.test == True:
        modes.append('test')
    if args.visualize == True:
        modes.append('visualize')

    print(modes)
    
    print(args)

    if args.env == "Acrobot":
        if args.model == "DQL":
            for mode in modes:
                run_acrobot_dql(mode=mode, **func_args)
        elif args.model == "PPO":
            for mode in modes:
                run_acrobot_ppo(mode=mode, **func_args)
        elif args.model == "A2C":
            for mode in modes:
                run_acrobot_a2c(mode=mode, **func_args)
    elif args.env == "Car":
        if args.model == "DQL":
            for mode in modes:
                run_car_dql(mode=mode, **func_args)
        # Done, mostly
        elif args.model == "PPO":
            for mode in modes:
                run_car_ppo(mode=mode, **func_args)
        elif args.model == "A2C":
            for mode in modes:
                run_car_a2c(mode=mode, **func_args)
    
    
if __name__ == '__main__':
    main()