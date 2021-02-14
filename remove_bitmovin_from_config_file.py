import os

path = '/hardcoded/path/to/config/files'
robot_tests_dir_list = os.listdir(path)
device_list = []
excluded_test_files = []
files_with_filters = []
files_with_bitmovin = []

for dir in robot_tests_dir_list:
    if dir in device_list:

        device_tests_dir_list = os.listdir(path + '/' + dir)

        for inner_dir in device_tests_dir_list:
            if 'master' in inner_dir or '4.21.0' in inner_dir:
                device_test_configs_list = os.listdir(path + '/' + dir + '/' + inner_dir)

                for file_name in device_test_configs_list:
                    if file_name in excluded_test_files: continue
                    file_path = path + '/' + dir + '/' + inner_dir + '/' + file_name
                    lines_list = []
                    edit_file = False
                    with open(file_path, 'r') as file:
                        lines_list = file.readlines()

                        for i in range(len(lines_list)):
                            if 'FILTERS' in lines_list[i] and not '-bitmovin' in lines_list[i]:
                                # print(file_name.upper(), '->', 'there is inside!')
                                files_with_filters.append(dir + '/' + inner_dir + '/' + file_name)
                                lines_list[i] = lines_list[i][:-1] + ',-bitmovin\n'
                                edit_file = True
                                # print(dir + '/' + inner_dir + '/' + file_name, lines_list[i])
                                break
                            elif 'FILTERS' in lines_list[i] and '-bitmovin' in lines_list[i]:
                                files_with_bitmovin.append(dir + '/' + inner_dir + '/' + file_name)

                    if edit_file:
                        with open(file_path, 'w') as file:
                            file.writelines(lines_list)

    else:
        continue

# for file in files_with_filters:
#     print(file)

print('Files with FILTERS attr but with not bitmovin exclusion:', len(files_with_filters))
print('Files with bitmovin filter:', len(files_with_bitmovin))
