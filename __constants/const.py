from faker import Faker
import random

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Github Repo - https://git.io/JJisT/ ########

start_url = 'https://www.opencccapply.net/gateway/apply?cccMisCode='

clg_ids = ['941', '311', '361', '233', '851', '431', '371', '091', '641', '231', '621', '521', '911', '345', '111', '411', '211', '811', '482', '373', '683']

allColleges = ['MSJC College', 'Contra Costa College', 'City College', 'Sacramento College', 'Mt San Antonio', 'Ohlone College', 'Cañada College', 'Southwestern College', 'Cuesta College', 'American River College', 'Antelope Valley College', 'Bakersfield College', 'Barstow Community College', 'Berkeley City College', 'Butte College', 'Cabrillo College', 'Calbright College', 'Cerritos College', 'Chabot College', 'Skyline College', 'Ventura College']

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
