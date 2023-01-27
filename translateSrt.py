import os
import glob
from google.cloud import translate_v2 as translate

# Set up the Google Translate API client
client = translate.Client()

# Define the input and output folders
input_folder = 'M:\\18-01-2023\\U\\[FreeCoursesOnline.Me] PacktPub - Full Stack Web Development Bootcamp with React and Python [Video]'
output_folder = 'M:\\18-01-2023\\U\\[FreeCoursesOnline.Me] PacktPub - Full Stack Web Development Bootcamp with React and Python [Video]\\tr subs'

# Loop through all .srt files in the input folder
for file in glob.glob(os.path.join(input_folder, '*.srt')):
    with open(file, 'r') as f:
        # Read the file content
        content = f.read()

    # Translate the content
    result = client.translate(content, target_language='tr')

    # Get the translated text
    translated_text = result['translatedText']

    # Get the original file name and create the output file name
    input_file_name = os.path.basename(file)
    output_file_name = os.path.splitext(input_file_name)[0] + '_translated.srt'
    output_file_path = os.path.join(output_folder, output_file_name)

    # Write the translated text to the output file
    with open(output_file_path, 'w') as f:
        f.write(translated_text)
