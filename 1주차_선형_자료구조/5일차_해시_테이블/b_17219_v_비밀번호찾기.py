N, site_num = input().split()

pw_dict = {}
for _ in range(int(N)):
    site_name, site_pw = input().split()
    pw_dict[site_name] = site_pw

for _ in range(int(site_num)):
    res_site_name = input()
    print(pw_dict[res_site_name])
