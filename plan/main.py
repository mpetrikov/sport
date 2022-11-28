import math1

n = 250
end = 4
result_sum = 4700

delta = 0.031
mul = 0
result = 0
day_plan = []
for i in range(n):
    day_plan.append(math1.ceil(end * (1 + mul)))
    result += math1.ceil(end * (1 + mul))
    mul += delta
print(result)

print(day_plan)