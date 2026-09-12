# Speech-to-Text Prototype

A minimal Python experiment for speech-to-text processing. The repository is intentionally small and is retained as an early application prototype rather than a complete speech-recognition system.

## Run

Inspect the input/configuration expected by `main.py`, install its dependency, and execute:

```bash
python main.py
```

## Scope

For production use, this prototype would require explicit audio-format handling, model/version documentation, error handling, evaluation on a defined speech dataset, and reproducible dependency management.


## Goal

The script demonstrates the shortest path from a local audio file to a Whisper transcription, making it useful for checking model setup and audio decoding before integrating speech recognition into a larger application.

## Installation

The repository does not pin dependencies. Install Python, FFmpeg, and the Whisper package in an isolated environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install openai-whisper
```

## Working with the Repository

Set the input audio path in `main.py`, select an appropriate Whisper model for the available memory, and run `python main.py`. Record package and model versions before using results in an experiment, because the current repository has no lock file or evaluation protocol.
