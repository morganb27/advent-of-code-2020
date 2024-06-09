import fileinput

def validate_height(hgt):
    if hgt.endswith('cm'):
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith('in'):
        return 59 <= int(hgt[:-2]) <= 76

validation_rules= {
    'byr': lambda x: 1920 <= int(x) <= 2022,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': validate_height,
    'hcl': lambda x: x.startswith('#') and len(x) == 7 and all(c in '0123456789abcdef' for c in x[1:]),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(str(x)) == 9 and all(num.isdigit() for num in str(x))
}


def parse_input():
    passports = []
    passport = {}
    for line in fileinput.input():
        line = line.strip()
        if not line:
            passports.append(passport)
            passport = {}
        else:
            parts = [part.split(':') for part in line.split(' ')]
            for a, b in parts:
                if a != 'cid':
                    passport[a] = b
    passports.append(passport)
    return passports

def valid_passports(passport):
    if len(passport) == 7:
        return True
    elif len(passport) < 7:
        return False

def valid_passports_part_2(passport):
    return all(validation_rules[k](v) == True for k, v in passport.items()) and len(passport) == 7

PASSPORTS = parse_input()
print(f"Total valid passwords: {sum(valid_passports(p) for p in PASSPORTS)}")
print(f"Total valid passports part 2: {sum(valid_passports_part_2(p) for p in PASSPORTS)}")
