# Patient Instruction Tracker

## Problem Statement
Patients forget or misunderstand doctor instructions after a visit, and no system checks whether they are following them.

## What This System Does
- Allows doctors to upload instructions
- Allows patients to view instructions
- Tracks whether patients acknowledge instructions

## What This System Does NOT Do
- It does not diagnose or treat patients
- It does not replace doctors

## Tech Stack
- Backend: Python (FastAPI)
- Database: PostgreSQL
- Deployment: Docker

## How to Run
1. docker-compose up
2. Open browser at localhost

## Assumptions
- Patients have internet access
- Instructions are text-based

## Known Limitations
- No reminders yet
- No caregiver roles yet
