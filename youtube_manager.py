      
import json
# import os

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            # print(type(test))
            return test
            # return json.load(file)
    except FileNotFoundError:
        return []
    finally:
        pass

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
   print("\n")
   print('*'*70)
   for index,vid in  enumerate(videos, start=1):
       print(f"{index}. Name of video: {vid['Name']}, Duration : {vid['Time']}")
   print("\n")
   print('*'*70)
    

def add_video(videos):
   video_name = input("Enter Video Name:  ")
   video_time = input("Enter Video Time: ")

   empty_dict = {}
   empty_dict['Name'] = video_name
   empty_dict['Time'] = video_time
   
   videos.append(empty_dict)
   #videos.append({'Name': video_name, 'Time':video_time})
   save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to update: '))

    if 1<= index <=len(videos):
        new_video_name = input("Enter The new Video Name: ")
        new_video_time = input("Enter The new Video Time: ")
        videos[index-1] = {'Name': new_video_name,'Time':new_video_time}
        save_data_helper(videos)
    else:
        print('Invalid Index selected!')


def delete_video(videos):
    list_all_videos(videos)
    index =  int(input('\n Enter the video number to be deleted: '))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        
    else:
        print("Invalid Video Index selected!")


def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | Choose an option")
        print("1. List All Youtube Video")
        print("2. Add a Youtube Video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video ")
        print("5. Exit App ")

        choice = input("Enter Your Choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case "2" :
                add_video(videos)
            case "3" :
                update_video(videos)
            case "4" :
                delete_video(videos)
            case "5" :
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main()