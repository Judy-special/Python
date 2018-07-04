# coding=utf8
"""
使用方法：
1. python transform.py input_file_name output_file_name
"""

label_sep = "%sep%"

l_name_list = ["is_app_loan_num_2","is_app_loan_num_5","is_app_loan_num_10",
            "is_bank_num_2","is_bank_num_3","is_bank_num_4",
            "is_app_p2p_num_1m_2","is_app_p2p_num_1m_4","is_app_p2p_num_1m_6",
            "is_app_p2p_num_1m_10","is_app_p2p_num_3m_5","is_app_p2p_num_3m_10",
            "is_app_p2p_num_3m_20","is_app_p2p_num_6m_10","is_app_p2p_num_6m_20",
            "is_app_platform_num_1m_5","is_app_platform_num_1m_10",
            "is_app_platform_num_1m_20","is_app_platform_num_3m_10","is_app_platform_num_3m_20",
            "is_app_platform_num_3m_25","is_app_platform_num_6m_10",
            "is_app_platform_num_6m_20","is_app_platform_num_6m_30","is_app_platform_num_6m_40"]


def transform(input_file, output_file):
    records = read_records(input_file)
    with open(output_file, "w") as output_data:
        for record in records:
            processed_records = process_record(record)
            if processed_records is not None:
                for processed_record in processed_records:
                    output_line = processed_record
                    output_data.write(output_line + "\n")


def read_records(input_file):
    is_header = True
    with open(input_file) as input_data:
        for line in input_data:
            if is_header:
                is_header = False
            else:
                yield line.strip("\n")


def process_record(record):
    fileds = record.split(",")
    if len(fileds) < 34:
        return None
    forepart = ",".join(fileds[:9])
    label_list = fileds[9:]
    encoded_num_arr = encode_list(label_list)
    result = []
    for elem in encoded_num_arr:
        result.append(forepart + "," + elem)
    return result


def encode_list(list_label):
    result = []
    for i in range(len(list_label)):
        for j in range(i+1, len(list_label)):
            if list_label[i] > list_label[j]:
                result.append(label_sep.join([l_name_list[i], l_name_list[j]]))
            elif list_label[i] < list_label[j]:
                result.append(label_sep.join([l_name_list[j], l_name_list[i]]))
    return result


if __name__ == '__main__':
    import sys
    input_data_file = sys.argv[1]
    output_data_file = sys.argv[2]
    transform(input_data_file, output_data_file)


