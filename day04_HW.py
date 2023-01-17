#prob 7.8
surprise = ["Groucho", "Chico", "Harpo"]

#prob 7.9
surprise[-1] = surprise[-1].lower()
harpo = list(surprise[-1])
rv_harpo = ''.join(harpo[::-1])
surprise[-1] = rv_harpo.title()
print(surprise)