# FlightDeck Forex Market Intelligence Platform

## Overview

FlightDeck is an automated market intelligence platform built using Python, PostgreSQL, MetaTrader 5, Telegram, Power BI, and a cloud-hosted Windows VPS.

The platform scans multiple forex markets every four hours, calculates technical indicators, scores trade setups using research-backed probabilities, stores results in PostgreSQL, and delivers automated alerts through Telegram.

---

## Technology Stack

- Python
- PostgreSQL
- MetaTrader 5
- Telegram Bot API
- Power BI
- Windows VPS
- GitHub

---

## System Architecture

```text
MetaTrader 5
    ↓
Python Scanner
    ↓
PostgreSQL Database
    ↓
Signal Scoring Engine
    ↓
Telegram Alerts
    ↓
Power BI Dashboard