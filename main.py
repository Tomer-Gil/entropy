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


def get_supported_choices():
    return ["coin", "cube", "2cubes", "sum2cubes"]


def get_distribution_by_name(distribution_name):
    if distribution_name == "coin":
        return np.ones(2) / 2
    if distribution_name == "cube":
        return np.ones(6) / 6
    if distribution_name == "2cubes":
        return np.ones(36) / 36
    if distribution_name == "sum2cubes":
        return np.concatenate((np.arange(1, 7), np.arange(5, 0, -1))) / 36


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--distribution", "--dist", "-d", nargs="+", type=float, help="Specify the distribution")
    group.add_argument("--name", "-n", help="Specify a well-known distribution", choices=get_supported_choices())
    args = parser.parse_args()
    if args.distribution:
        if not is_valid_distribution(args.distribution):
            handle_invalid_distribution()
            sys.exit(1)
        else:
            distribution = args.distribution
    else:
        distribution_name = args.name
        distribution = get_distribution_by_name(distribution_name)
    print(f"Distribution: {distribution}")
    print(f"Entropy: {entropy(distribution)}")
