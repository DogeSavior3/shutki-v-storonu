n = open('stanza_gpu_greek.py', 'r').read()
# print(n[0:55])

for i in range(1, 33):
    task = ''.join([n[0:80], '_', str(i), n[80:]])
    with open(''.join(['stanza_gpu_greek_', str(i), '.py']), 'w') as output_file:
        output_file.write(task)
