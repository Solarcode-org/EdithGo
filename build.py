#!/usr/bin/python

from subprocess import run, PIPE

result = run(['go', 'tool', 'dist', 'list'], stdout=PIPE)

for line_ in result.stdout.split(b'\n'):
    if not line_:
        continue

    line = line_.decode('utf-8')

    print(f"Building for {line}")

    os, arch, *_ = line.split('/')

    run(['sh', '-c', f'GOOS={os} GOARCH={arch} go build -o bin/edith_{os}_{arch}'])
