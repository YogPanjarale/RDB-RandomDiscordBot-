import json
import requests
from dataclasses import dataclass


@dataclass()
class CovResponse():
    updated: int
    cases:int
    active: int
    recovered: int
    deaths: int
    todayCases: int
    todayRecovered: int
    todayDeaths: int
    critical: int
    casesPerOneMillion: int
    deathsPerOneMillion: int
    tests: int
    testsPerOneMillion: int
    population: int
    oneCasePerPeople: int
    oneDeathPerPeople: int
    oneTestPerPeople: int
    undefined: int
    activePerOneMillion: int
    recoveredPerOneMillion: int
    criticalPerOneMillion: int
    affectedCountries: int


def getCovidData(mode="world") -> CovResponse:
    if mode == "world":
        r = requests.get("https://disease.sh/v3/covid-19/all")
        r_json = r.json()
        # print(r_json)
        rs = CovResponse(**r_json)
        # print(r_json)
        return rs
    elif mode =="india":
        return
    pass
