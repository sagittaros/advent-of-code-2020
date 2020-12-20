import re

from .policies import Policies

# RULES
# =====
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def test_byr():
    for y in range(0, 1920):
        assert not bool(re.match(Policies["byr"], str(y))), f"{y} failed"
    for y in range(1920, 2003):
        assert bool(re.match(Policies["byr"], str(y))), f"{y} failed"
    for y in range(2003, 10000, 100):
        assert not bool(re.match(Policies["byr"], str(y))), f"{y} failed"


def test_iyr():
    for y in range(0, 2010):
        assert not bool(re.match(Policies["iyr"], str(y))), f"{y} failed"
    for y in range(2010, 2021):
        assert bool(re.match(Policies["iyr"], str(y))), f"{y} failed"
    for y in range(2021, 10000, 100):
        assert not bool(re.match(Policies["iyr"], str(y))), f"{y} failed"


def test_eyr():
    for y in range(0, 2020):
        assert not bool(re.match(Policies["eyr"], str(y))), f"{y} failed"
    for y in range(2020, 2031):
        assert bool(re.match(Policies["eyr"], str(y))), f"{y} failed"
    for y in range(2031, 10000, 100):
        assert not bool(re.match(Policies["eyr"], str(y))), f"{y} failed"


def test_hgt():
    for cm in range(150, 194):
        assert bool(re.match(Policies["hgt"], f"{cm}cm")), f"{cm}cm failed"
    for inch in range(59, 76):
        assert bool(re.match(Policies["hgt"], f"{inch}in")), f"{inch}in failed"
