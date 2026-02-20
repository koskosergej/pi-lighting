# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Raspberry Pi 3 LED control scripts using Python and `gpiozero`.

## Running scripts

```bash
python3 blink.py
```

Scripts must be run on the Raspberry Pi directly (GPIO is not available on other machines).

## GPIO pin convention

Use BCM (Broadcom) pin numbering — this is the default in `gpiozero`. Document the physical pin number in a comment next to each GPIO assignment, e.g.:

```python
led = LED(4)  # GPIO 4 (physical pin 7)
```

## Dependencies

`gpiozero` is pre-installed on Raspberry Pi OS. For other dependencies:

```bash
pip3 install gpiozero
```
