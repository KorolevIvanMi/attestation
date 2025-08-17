
import pandas as pd
import random
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

prof_head = ["Муравьева Алина Алексеевна","Кириллова Наталья Романовна","Ворожцов Андрей Ильич",
             "Фишков Максим Романович","Королев Иван Михайлович","Хвастунов Александр Алексеевич",
             "Дементьева Виктория Евгеньевна","Томский Алексей Андреевич","Стогова Александра Алексеевна"]

proj_leader = ["Хвастунов Александр Алексеевич", "Томский Алексей Андреевич", 
               "Попова Алёна Романовна", "Стогова Александра Алексеевна"]

prof_head_rev = 16

df_itog = pd.read_excel("D:/other_Projects/for_Attestation/Data/Help_table/Patern_for_itog_table.xlsx")

for act_name in df_itog["ФИО"]:
    #аттестация соновы пб
    if act_name in prof_head:
        df_itog.loc[df_itog["ФИО"] == act_name, "Должность (занимаемая должность в структуре пб3)"] = 16
    #аттестация лидиров проектов
    if act_name in proj_leader:
        df_itog.loc[df_itog["ФИО"] == act_name,"Руководство в проекте (занимаение должности руководителя в проекте профкома)"] = 16

df_itog.to_excel("D:/other_Projects/for_Attestation/Data/Results/itog.xlsx")
    

        