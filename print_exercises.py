#!/usr/bin/python3

import collections
import argparse

_days_to_print = 7
_reps_before_change = 100
_exercises = ['Bicep curls', 'Shoulder press', 'French curls', 'Push ups', 'Sit ups', 'Pull ups']


def find_all_divisors(a):
    return [j for j in range(1, a + 1) if a // j == a / j]


def find_exercises_per_day(options):
    current = 1
    for o in options:
        if len(_exercises) >= o > current:
            current = o
    return current


def find_reps_per_exercise(reps_per_day, exercises_per_day):
    return reps_per_day // exercises_per_day


def print_day(reps_per_day, exercise_deque):
    exercises_per_day = find_exercises_per_day(find_all_divisors(reps_per_day))
    reps_per_exercise = find_reps_per_exercise(reps_per_day, exercises_per_day)
    strings = []
    for _ in range(exercises_per_day):
        e = exercise_deque.popleft()
        strings.append(f'{reps_per_exercise}x {e}')
    print(strings)
    return exercises_per_day * reps_per_exercise


def do_rotation(reps_per_day):
    exercise_deque = collections.deque(_exercises)
    exercises_per_day = find_exercises_per_day(find_all_divisors(reps_per_day))
    reps = print_day(reps_per_day, exercise_deque)
    while len(exercise_deque) > 0:
        if len(exercise_deque) < exercises_per_day:
            for e in _exercises:
                exercise_deque.append(e)
        reps += print_day(reps_per_day, exercise_deque)
    return reps


def make_schedule(reps_per_day):
    reps_remaining = _reps_before_change
    while reps_remaining > 0:
        reps_remaining -= do_rotation(reps_per_day)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('reps', metavar='reps', type=int, nargs=1,
                    help='reps per exercise per day')
    args = parser.parse_args()
    _reps_per_day = args.reps[0]
    for i in range(_reps_per_day, _reps_per_day + _days_to_print):
        make_schedule(i)
        print()
