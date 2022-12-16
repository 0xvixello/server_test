import math
import colorama
from datetime import datetime

start_time = datetime.now()
def progress_bar(progress, total, color=colorama.Fore.RED):
    percent = 100 * (progress / float(total))
    bar = '¥' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")


numbers = [x * 5 for x in range (20000, 50000)]
result = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

end_time = datetime.now()

print(f"\n\nTime Taken: {end_time - start_time}")
