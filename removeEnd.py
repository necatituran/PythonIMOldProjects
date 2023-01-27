import glob
import os

folder_path = 'C:\\Users\\nhtur\\Downloads\\endsubs'

# for file_path in glob.glob(folder_path + '/*.srt'):
#     with open(file_path, 'r') as file:
#         file_name = os.path.basename(file_path)
#         start_index = file_name.index('(')
#         new_file_name = file_name[:start_index] + '.srt'
#         new_file_path = os.path.join(folder_path, new_file_name)
#         os.rename(file_path, new_file_path)


# for file_path in glob.glob(folder_path + '/*.srt'):
#     with open(file_path, 'r') as file:
#         data = file.read()
#         start_index = data.index('(')
#         end_index = data.index(')') + 1
#         new_data = data[:start_index] + data[end_index:]
#     with open(file_path, 'w') as file:
#         file.write(new_data)

# for file_path in glob.glob(folder_path + '/*.srt'):
#     file_name = os.path.basename(file_path)
#     start_index = file_name.index(' (')
#     new_file_name = file_name[:start_index] + '.srt'
#     new_file_path = os.path.join(folder_path, new_file_name)
#     os.rename(file_path, new_file_path)
