import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  source = "The Zen of Python, by Tim Peters"
  print(quotes[rnd]+source )

if __name__== "__main__":
  primary()
