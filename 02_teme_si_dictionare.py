
# lista1 = [1, 3, 4, 100, 300, 10, 3000]
#index:     0, 1, 2,   3,   4,  5,    6

# var1 = "      EU sunt  SLIM SHADY   Un Sir de caractere    e   cu cateva spatii   "
# var2 = var1.strip().lower()
#
# print(var1)
# print(var2)

# var1 = "error | lightning strike | system shutdown"
# var2 = var1.split("|")
#
# print(var2)

# lista1 = []
# print(lista1)
# lista1.append("error")
# lista1.append("error")
# lista1.append("error")
# lista1.append("warning")
#
# print(lista1.count("error"))


raw_logs = [
" ERROR | Voltage too LOW | code=E12 ",
" info | System started successfully ",
" WARNING | High temperature detected | code=W07 ",
" ERROR | Communication timeout | code=E99 ",
" info | System shutdown complete "
]


for i in range(len(raw_logs)):
    # for i -> creaza o variabila i
    # len(raw_logs) -> 5
    # range(len(raw_logs)) -> range(5) -> [0, 1, 2, 3, 4]
    # i -> index

    # 1.Clean each log line

    # raw_logs -> lista
    # raw_logs[i] -> un element din lista - > string
    # lista nu are strip()
    # string contine strip()
    raw_logs[i] = raw_logs[i].strip().lower()

    # 2.Split log fields
    # now instead of raw_logs being a list of strings, it's a list of lists of strings.
    raw_logs[i] = raw_logs[i].split("|")
    print(raw_logs[i])


print("Starting Identification:")
log_type_counts = []
error_codes_list = []
warning_codes_list = []

for i in range(len(raw_logs)):
    # raw_logs[i]    -> ['error ', ' voltage too low ', ' code=E12']
    # raw_logs[i][0] ->  'error '
    # raw_logs[i][0][0] ->  'e'

    if raw_logs[i][0].startswith("error"):
        # log_type_counts.append("error")
        log_type_counts.append(raw_logs[i][0].strip())
        print("Ce eroare avem?")
        print(raw_logs[i][2])

        # procesam eroarea din logul cu erori:
        # raw_logs[i][2] -> ' code=e12'
        # raw_logs[i][2].split("=") -> [' code', 'E12']
        # raw_logs[i][2].split("=")[1] -> 'E12'
        extracted_error_code = raw_logs[i][2].split("=")[1]
        error_codes_list.append(extracted_error_code)

    if raw_logs[i][0].startswith("info"):
        log_type_counts.append(raw_logs[i][0].strip())

    if raw_logs[i][0].startswith("warning"):
        log_type_counts.append(raw_logs[i][0].strip())
        print("Ce warning avem?")
        print(raw_logs[i][2])

        extracted_error_code = raw_logs[i][2].split("=")[1]
        warning_codes_list.append(extracted_error_code)


error_count = log_type_counts.count("error")
warnings_count = log_type_counts.count("warning")
info_count = log_type_counts.count("info")

output_string = f"""
OUTPUT
LOG SUMMARY
-----------
Errors      : {error_count}
Warnings    : {warnings_count}
Info        : {info_count}

Error Codes: {error_codes_list}
Warning Codes: {warning_codes_list}
"""

print(output_string)


# print("OUTPUT")
# print("LOG SUMMARY")
# print("-----------")
# print("Errors   :")
# print(log_type_counts.count("error"))
# print("Warnings :")
# print(log_type_counts.count("warning"))
# print("Info     :")
# print(log_type_counts.count("info"))

# print(log_type_counts)


# print("------F-Strings--------")
#
# string2 = [20, 40, 100]
# var3 = f"{string2} are 30 de mere in ghiozdan."
#
# print(var3)


# error_count2 = 0
# info_count2 = 0
# warning_count2 = 0
#
# for i in range(len(raw_logs)):
#
#     if raw_logs[i][0].startswith("error"):
#         error_count2 = error_count2 + 1
#
#     if raw_logs[i][0].startswith("info"):
#         info_count2 = info_count2 + 1
#
#     if raw_logs[i][0].startswith("warning"):
#         # warning_count2 += 1
#         warning_count2 = warning_count2 + 1

