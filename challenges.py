#!/usr/bin/env python2.7

import argparse
import sys
import set1


def print_challenges(num, name, challenges):
    """ challenges is dict from {num -> (challenge_name, challenge_func)}
    """
    print 'Challenge %d - %s' % (num, name)
    for challenge_num in sorted(challenges.keys()):
        print '  %d. %s' % (challenge_num, challenges[challenge_num][0])


def print_sets(all_challenges):
    print 'Matasano Crypto Challenges'
    for num in sorted(all_challenges.keys()):
        print '%d. %s' % (num, all_challenges[num][0])


def challenge(num, name, challenges):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print('')
            print('---------------------' + '-' * len(name))
            print(' Begin challenge %d: %s' % (num, name))
            print('---------------------' + '-' * len(name))
            print('')
            f(*args, **kwargs)
        challenges[num] = (name, wrapper)
        return wrapper
    return decorator


def expect(actual, expected):
    if actual != expected:
        print('Failed.')
        print('  Expected: %r' % expected)
        print('  Actual: %r' % actual)
        return False
    print 'Success!'
    print '  Matched: %r' % actual
    return True


def parse_args():
    parser = argparse.ArgumentParser(description='Python implementations of the Matasano Crypto Challenges')
    parser.add_argument('-s', '--set', type=int, default=-1, help='Which set of challenges to run')
    parser.add_argument('-n', '--num', type=int, default=-1, help='Which number challenge to run in a set')
    parser.add_argument('-l', '--list', action='store_true', help='List all sets or challenges in a set')
    return parser.parse_args()


def print_usage():
    print 'Usage: ./challenges.py --set <set_num> (--num <chall_num>)'
    print '       ./challenges.py --list [--set <set_num>]'
    sys.exit(1)


if __name__ == '__main__':
    args = parse_args()
    all_challenges = {}

    # List of all challenge sets
    for s in [set1, ]:
        # all_challenges is dict from {set_num -> (set_name, {chall_num -> (chall_name, chall_func)})}
        all_challenges[s.num] = (s.name, s.challenges)

    if args.list:
        # Print list of challenges
        if args.set >= 0 and args.set in all_challenges:
            print_challenges(args.set, all_challenges[args.set][0], all_challenges[args.set][1])
        else:
            print_sets(all_challenges)
        sys.exit(0)

    # Try to run a challenge or set of challenges
    if args.set not in all_challenges:
        print 'Error: Set %d not found in list of sets!' % args.set
        print_sets(all_challenges)
        print ''
        print_usage()

    if args.num < 0:
        to_run = all_challenges[args.set][1].values()
    elif args.num in all_challenges[args.set][1]:
        to_run = [all_challenges[args.set][1][args.num]]
    else:
        print 'Error: Challenge %d not found in list of challenges for set %d!' % (args.num, args.set)
        print_challenges(args.set, all_challenges[args.set][0], all_challenges[args.set][1])
        print ''
        print_usage()

    # Run each challenge we've identified (either all from a set, or just one)
    for run in to_run:
        run[1]()