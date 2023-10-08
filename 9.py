with open('input.txt') as file:
    steps = file.read().splitlines()
steps = list(map(int, steps))

recs = len(steps)
per_month = [
    sum(steps[:31]) / 31,                     # Jan
    sum(steps[31:recs-306]) / (recs - 337),   # Fab
    sum(steps[recs-306:recs-275]) / 31,       # Mar
    sum(steps[recs-275:recs-245]) / 30,       # Apr
    sum(steps[recs-245:recs-214]) / 31,       # May
    sum(steps[recs-214:recs-184]) / 30,       # Jun
    sum(steps[recs-184:recs-153]) / 31,       # Jul
    sum(steps[recs-153:recs-122]) / 31,       # Aug
    sum(steps[recs-122:recs-92]) / 30,        # Sep
    sum(steps[recs-92:recs-61]) / 31,         # Oct
    sum(steps[recs-61:recs-31]) / 30,         # Nov
    sum(steps[recs-31:]) / 31,                # Dec
]

for m in per_month:
    print(m)
