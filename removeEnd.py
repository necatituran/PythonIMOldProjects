import glob
import os
import shutil
import re

folder_path = 'C:\\Users\\nhtur\\Downloads\\endsubs'
destination_folder = 'C:\\Users\\nhtur\\Downloads\\endsubs\\output'
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

# for file_path in glob.glob(folder_path + '/*.srt'):
#     file_name = os.path.basename(file_path)
#     if '(' in file_name:
#         start_index = file_name.index(' (')
#         new_file_name = file_name[:start_index] + '.srt'
#         if new_file_name != file_name:
#             new_file_path = os.path.join(destination_folder, new_file_name)
#             os.rename(file_path, new_file_path)
#             shutil.copy2(new_file_path, destination_folder)
#     else:
#         shutil.copy2(file_path, destination_folder)

for filename in os.listdir(folder_path):
    if filename.endswith('.srt'):
        new_filename = re.sub(r'\s+\(Transcribed.*\)', '', filename)
        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_filename))
