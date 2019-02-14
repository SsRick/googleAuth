# simple code for revoking the token 
import requests

requests.post('https://oauth2.googleapis.com/revoke',
    params={'token': 'ya29.GluwBq5RbCPmXhLroHKE1b61OHyXZuVEXZcvxFcaGvssFBjLrZeVvzqyENBDnTanq5uTjL3np0kVESUoxgJOYX_7eFOJjt-XVP9LcUzbwEjl64qVnpqqQUGDyPxU'},
    headers = {'content-type': 'application/x-www-form-urlencoded'})