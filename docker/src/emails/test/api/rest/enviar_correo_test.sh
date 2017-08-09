#!/bin/bash
curl -H "Content-Type: application/json" -X POST -d '{"de":"pablo.rey@econo.unlp.edu.ar", "para":"pablodanielrey@gmail.com", "asunto":"prueba de correo", "cuerpo":"cHJ1ZWJhIGRlIGNvcnJlbyBjdWVycG8K"}' http://127.0.0.1:8001/emails/api/v1.0/enviar_correo
