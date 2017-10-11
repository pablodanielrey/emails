#!/bin/bash
python3 emails/registrar.py emails_web / emails.econo.unlp.edu.ar:5025 &
python3 emails/registrar.py emails_rest /emails/api emails.econo.unlp.edu.ar:5026
