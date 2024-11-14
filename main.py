import sys

import numpy as np
import argparse


def entropy(distribution):
    """
    Calculates the entropy of a distribution, with log in base 2
    :param distribution: np array of a final distribution
    :return:
    """
    return -np.sum(distribution * np.log2(distribution))


def is_valid_distribution(distribution):
    total_sum = 0
    for i in distribution:
        if i < 0:
            return False
        total_sum += i
        # Short optimization
        if total_sum > 1:
            return False
    return total_sum == 1


def handle_invalid_distribution():
    print("Please enter a valid distribution: all elements are non-negative, and sums up to 1.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("distribution", nargs="+", type=float, help="Specify the distibution")
    args = parser.parse_args()
    if not is_valid_distribution(args.distribution):
        handle_invalid_distribution()
        sys.exit(1)
    else:
        distribution = args.distribution
        print(f"Distribution: {distribution}")
        print(f"Entropy: {entropy(distribution)}")

