import csv
from video_to_transcript import youtube_video_transcript

'''
    :key - topic
    :value - filename
'''
topics = {'Algebra Expression' : 'grade_8 algebraic expression.csv',
          'Angles' : 'grqade_8 angles.csv',
          'Symmetry' : 'grade_7 Symmetry.csv',
          'Directed Numbers' : 'grade_8 direct numbers.csv',
          'Factors and Multiplication' : 'grade_7 factors and multiples.csv',
          'Indices' : 'grade_7 Indices.csv',
          'Number Patterns' : 'grade 8 number_pattens.csv',
          'Operations of Whole Number' : 'Ograde_7 peraation on hole numbers.csv',
          'Perimeter' : 'grade 8 perimeter.csv',
          'Sets' : 'grade_7 sets.csv'
          }

'''
    :name - filename
'''
def function(directory,name,topic,writer):
    with open(f'{directory}/{name}') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                try:
                    if len(row) >= 5:
                        # video id
                        #video_id = row[2]
                        video_title = row[4]
                        # if len(video_id) > 0:
                        #     transcript = youtube_video_transcript(video_id)
                        #     if transcript is not None:
                        #         transcript = transcript.replace('\n', ' ')
                        writer.writerow({"Title" : video_title, "Topic" : topic})
                except:
                    print('An exception occurred.')
                    continue
            print(f'File : {name} | Processed {line_count} lines')


#function('../SearchEngine Dataset','grade 8 number_pattens.csv')

directory = '../SearchEngine Dataset'

with open('../TopicClasification_Data set/video titles dataset.csv', mode='a+') as csv_file:
    fieldnames = ['Title', 'Topic']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for topic,file in topics.items():
        function(directory,file,topic,writer)
