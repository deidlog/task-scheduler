# Job Scheduler

A lightweight, beginner-friendly job scheduler built in Python — ideal for automating scripts and recurring tasks using simple YAML configs.

## Features

- YAML-based job configuration
- Supports interval scheduling (e.g., every X seconds/minutes)
- Task execution logging
- Easy to extend and customize

## Structure
```
├── config/                     # Task configuration files (YAML)
│   └── config.yaml
│
├── logs/                       # Task execution logs
│   └── .gitkeep                # Keeps the folder tracked by Git (even when empty)
│
├── src/                        # Main source code
│   ├── __init__.py
│   ├── config_loader.py        # Loads and parses the YAML configuration files
│   └── scheduler.py            # Contains logic for scheduling and executing tasks
│
├── tests/                      # Unit tests
│   ├── test_config_loader.py   # Unit tests for config_loader.py
│   └── test_scheduler.py       # Unit tests for scheduler.py
│
├── .gitignore                  # Git ignore rules
├── README.md                   # Project description
├── requirements.txt            # Dependencies
└── main.py                     # Entry point
```

## Tech Stack

- Python 3.13+
- YAML (via `PyYAML`)
- Logging (built-in)
- `schedule` or custom event loop (TBD)

## Status

WIP (Work In Progress) - early prototype stage.

## MVP Plan

1. Parse YAML config file from `config/`
2. Schedule tasks based on interval
3. Run commands using `subprocess`
4. Log results to `logs/` with timestamped filenames
5. Support repeating jobs

Extra ideas:
- Email/Telegram alerts (future)
- Web interface (future)
- Crontab-style schedule (advanced)
