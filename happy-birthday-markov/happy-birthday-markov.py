import random

# happy birthday
with open('happy-birthday-input.txt') as f:
    input = f.read()

# parse input
lines = input.split('\n')
notes = []
for i, line in enumerate(lines):
    if i % 2 == 0:
        note_num = line[line.index('[') + 1:line.index('[')+3]
        notes.append(int(note_num))
print(notes)

# create dictionary for markov chain
d = dict()
for i, note in enumerate(notes[:-1]):
    if note in d.keys():
        d[note].append(notes[i+1])
    else:
        d[note] = [notes[i+1]]

d[notes[-1]] = [notes[0]]
print(d)

# generate output code
current_note = 55
s_out = ''
for i in range(100):
    next_note = random.choice(d[current_note])
    s_out = s_out + f"""play {current_note}\nsleep 0.5\n"""
    current_note = next_note

# write to out file
with open('out.txt', 'w') as f:
    f.write(s_out)





