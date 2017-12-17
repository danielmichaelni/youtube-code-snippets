"""
Introduction to Dynamic Programming

A method for solving a complex problem by breaking it down into simpler
subproblems. We solve these subproblems once and store the solutions for the
next time we run into the same subproblem, so we can retrieve the stored
solution rather than re-computing the subproblem. This technique of storing
solutions for later use is called memoization. There is a tradeoff where we use
extra space for a usually much faster runtime.

Dynamic Programming Problem (Climbing Stairs):
You are climbing a stair case. It takes n steps to reach the top. Each time you
can either climb 1 or 2 steps. In how many distinct ways can you climb to the
top?

Example:
When n = 3, there are three ways to climb to the top:
1) 1 step + 1 step + 1 step
2) 1 step + 2 steps
3) 2 steps + 1 step

Problem provided by: https://leetcode.com/problems/climbing-stairs/
"""

def climb_stairs(n):
  if n == 0:
    return 1
  if n < 0:
    return 0
  return climb_stairs(n - 1) + climb_stairs(n - 2)

"""
climb_stairs(5) = climb_stairs(4) + climb_stairs(3)
                = climb_stairs(3) + climb_stiars(2) + climb_stairs(3)
                = ...
"""

def climb_stairs_top_down(n):
  memo = {}
  return climb_stairs_helper(n, memo)

def climb_stairs_helper(n, memo):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if n in memo:
    return memo[n]
  memo[n] = climb_stairs_helper(n - 1, memo) + climb_stairs_helper(n - 2, memo)
  return memo[n]

def climb_stairs_bottom_up(n):
  if n < 0:
    return 0
  memo = [1, 1]
  for i in range(2, n + 1):
    memo.append(memo[i - 1] + memo[i - 2])
  return memo[n]

# Test cases
print(climb_stairs_bottom_up(3) == 3)
print(climb_stairs_bottom_up(0) == 1)
print(climb_stairs_bottom_up(-1) == 0)
print(climb_stairs_bottom_up(20) == 10946)
