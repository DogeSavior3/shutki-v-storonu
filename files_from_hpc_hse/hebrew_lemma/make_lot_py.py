n = open('stanza_gpu.py', 'r').read()

for i in range(1, 129):
    task = ''.join([n[0:80], '_', str(i), n[80:]])
    with open(''.join(['stanza_gpu_', str(i), '.py']), 'w') as output_file:
        output_file.write(task)