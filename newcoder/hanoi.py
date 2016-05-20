#! /usr/bin/env ptyhon3
# -*- coding:utf-8 -*-


def hanoi(n, wfrom, mid, to):
    '''
    tower of hanoi problem.
    :param n: int, numbers of tower floors
    :param wfrom: string, source pillar
    :param mid: string, help pillar
    :param to: string, target pillar
    :return:
    '''
    if n == 0:
        return None
    elif n == 1:
        print("from %s to %s" % (wfrom, to))
    else:
        hanoi(n-1, wfrom, to, mid)
        hanoi(1, wfrom, mid, to)
        hanoi(n-1, mid, wfrom, to)

hanoi(6, 'left', 'mid', 'right')


# -----------------------extended problem----------------------------

def whichStepinHanoi(arr, i, wfrom, mid, to):
    '''
    given a int array represent the status now of the hanoi plates, which '1'-> right, '2'->mid ,3->right.
    find which step the array represents in the hanoi solution. if not in ,return -1.
    :param arr: represents the status
    :param i: int, how many plates in hanoi tower
    :param wfrom: int,
    :param mid: int,
    :param to: int,
    :return:
    '''
    if i == -1:
        return 0
    if arr[i] != wfrom and arr[i] != to:
        return -1
    if arr[i] == wfrom:
        return whichStepinHanoi(arr, i-1, wfrom, to, mid)
    else:
        rest = whichStepinHanoi(arr, i-1, mid, wfrom, to)
        if rest == -1:
            return -1
        return pow(2, i) + rest
