import discord
import random
import pandas as pd

def read_sheet(mw_id):
    # readme
    print("INCOMPLETE")
    sheet = pd.DataFrame.read_url("https://www.myth-weavers.com/api/v1/sheets/sheets/" + mw_id)
    # wait on this


def diceroll(sides, mod = 0):
    result = random.randint(1,sides)
    result = int(result)
    result += mod
    result = int(result)
    return result