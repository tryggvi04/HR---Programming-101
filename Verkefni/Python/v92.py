def country_suffix(str_suffix):
    countries_file = open("countries.txt", "r")
    count_int = 0
    for country in countries_file:
        if country.strip('\n').endswith(str_suffix):
            print(country.strip('\n'))
            count_int += 1
    print(f"{count_int} countries with suffix {str_suffix} in total.")
country_suffix(input())