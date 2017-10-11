#!/bin/bash
python3 emails/register.py emails_web / emails.econo.unlp.edu.ar:5025 &
python3 emails/register.py emails_rest /emails/api emails.econo.unlp.edu.ar:5026
