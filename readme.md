<h1 align="center">OpenClassrooms Project 4</h1>
<h3 align="center">Develop a Software Program Using Python</h3>

<p align="left">This is my fourth project for OpenClassrooms where I had to develop a tournament software 
that is able to manage chess tournaments and can produce reports.

- I learned to create classes that will serve as models for tournament, players, matches, and rounds.
- I wrote controllers to accept input from the user, produce match results, start new tournaments, etc.
- I created views to display the standings and pairings and other statistics.
- I used the "Swiss" tournament system algorithm.
- I followed the PEP 8 code styling guidelines and used the MVC design pattern.
</p>

## Prerequisite

- [Python3](https://www.python.org/ "Python") is installed

## Installation Steps

1. Clone the repository

```Bash
git clone https://github.com/aschickhoff/OCproject04.git
```

2. Change the working directory

```Bash
cd OCproject04
```

3. Add needed packages to run the scripts

```Bash
pip install -r requirements.txt
```

4. To create a flake8 report use the following command:

```Bash
flake8 --format=html --htmldir=flake8_report --exclude=venv
```

5. Run the script using terminal

```Bash
python main.py
```
