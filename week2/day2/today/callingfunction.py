from RetunFunction import get_pct,compute_pct

mark = float(input('Enter Your Mark:'))
fullmark = int(input('Enter Your Full Mark:'))

pct = compute_pct(mark,fullmark)
grade = get_pct(pct)

print(pct)
print(grade)
