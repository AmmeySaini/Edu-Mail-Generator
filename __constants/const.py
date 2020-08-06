from faker import Faker
import random

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Github Repo - https://git.io/JJisT/ ########

start_url = 'https://www.opencccapply.net/gateway/apply?cccMisCode='

clg_ids = ['941', '311', '361', '233']

allColleges = ['MSJC College', 'Contra Costa College', 'City College', 'Sacramento College']

country_codes = ['855', '561', '800', '325', '330', '229']

fake = Faker('en_US')

ex = fake.name().split(' ')

firstName = ex[0]
LastName = ex[1]
studentAddress = fake.address()
randomMonth = random.randint(1, 12)
randomDay = random.randint(1, 27)
randomYear = random.randint(1996, 1999)
randomEduMonth = random.randint(1, 12)
randomEduDay = random.randint(1, 27)
eduYears = [2019, 2020]
randomEduYear = random.choice(eduYears)