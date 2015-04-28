####### Example ########
# A123/234/B3456-456+457+-(DF345 + (U76/567) / -(PTYU+-990) -980)

__author__ = 'ags7kor'
import re

def main():
    data = "A123/234/B3456-456+457+-(DF345 + (U76/567) / -(PTYU+-990) -980)"
    all_variable = re.findall(r"[\w]+", data)
    unique_var = list(set(all_variable))
    print(unique_var)

if __name__ == '__main__':
    main()


