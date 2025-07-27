
import pandas as pd
import random
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

df = pd.read_excel('D:/other_Projects/for_Attestation/TestData.xlsx')
print(df)
