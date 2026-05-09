
# Project Euler 
This repository contains my solutions to Project Euler problems, along with some associated notes, writeups, and
performance explorations. The goal is primarily to solve puzzles, but a nice bonus is the cultivation of a toolbox (of
sorts) for mathematics and algorithmic design.

## Repository Structure
Each problem lives in its own self-contained directory under `/problems/some_problem_number`. Each problem directory may
include: 
    - `solution.__` -> Final executable solution(s) written in one or more languages. 
    - `writeup.pdf/tex` -> A LaTeX-based mathematical exploration 
    - `notes.md`    -> Scratch notes or alternative approaches 
    - `README.md`   -> Summary or special instructions

## Installation 
This project uses [`uv`](https://github.com/astral-sh/uv) for environment / package management. Installing dependencies
is as straightforward as: 

```bash
uv sync --group dev
```
