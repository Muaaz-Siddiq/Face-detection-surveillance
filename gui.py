from tkinter import *
import tkinter.font as font
import pymongo
from PIL import ImageTk, Image
import project

# This file is for GUI and futher logics after getting search results
# connecting with database
database_connection = pymongo.MongoClient('mongodb://localhost:27017/') #change to you DB settings
mydb =database_connection['project_database']
get_data = mydb['project _data']

# creating get detail function
def Get():
    if project.s_id == "No s_id":
        no_sid1 = Label(text="Un-Identified person -->> Can't trace", bg='#4b3c4f', fg='white')
        no_sid1['font'] = myFont
        no_sid1.place(x=350, y=400)
        print("Un-Identified person -->> Can't trace")
    else:
        records = get_data.find({'s_id': project.s_id}) # Get the s_id from project.py file
        record_list = []
        for record in records:
            #print(i['name'])
            record_list.append(record['s_id'])
            record_list.append(record['name'])
            record_list.append(record['age'])
            record_list.append(record['sex'])
            record_list.append(record['nationality'])
        id_lab1 = Label(text=record_list[0], bg='#4b3c4f', fg='white', width = 10)
        id_lab1['font'] = myFont
        id_lab1.place(x=300, y=100)
        name_lab1= Label(text =record_list[1], bg = '#4b3c4f', fg= 'white', width = 15)
        name_lab1['font'] = myFont
        name_lab1.place(x= 300, y=150)
        age_lab1 = Label(text=record_list[2], bg='#4b3c4f', fg='white', width = 10)
        age_lab1['font'] = myFont
        age_lab1.place(x=300, y=200)
        gen_lab1 = Label(text=record_list[3], bg='#4b3c4f', fg='white', width = 10)
        gen_lab1['font'] = myFont
        gen_lab1.place(x=300, y=250)
        nation_lab1 = Label(text=record_list[4], bg='#4b3c4f', fg='white', width = 10)
        nation_lab1['font'] = myFont
        nation_lab1.place(x=300, y=300)
        path_id_img = f'F:/py programs/Surveillance project/images/{project.s_id}.jpeg' # to get image to gui stored in our folder as data.
        id_image = Image.open(path_id_img)
        id_image = id_image.resize((250,250), Image.ANTIALIAS)
        id_image1 = ImageTk.PhotoImage(id_image)
        id_img = Label(image=id_image1)
        id_img.image = id_image1
        id_img.place(x= 520 , y=100, height = 250, width =250)
        if not record_list:
            nodata_lab = Label(text="No Data Found", bg='#4b3c4f', fg='white')
            nodata_lab['font'] = myFont
            nodata_lab.place(x=400, y=400)


# Second window For Gui
def secwind():
    root1.destroy()
    root = Tk()
    root.title("MS Security")
    root.geometry('800x800+740+0')
    root.minsize(800,800)
    #root.maxsize(800,800)
    root['bg'] = '#4b3c4f'

    myFont = font.Font(family='Arial', size=15, weight='bold')
    start_btn = Button(root, fg="black", text="Start ", relief=RAISED, width=10, height=1,command = project.Start)
    start_btn['font'] = myFont
    start_btn.place(x=250, y=670)
    detail_btn = Button(root, fg="black", text="Get Details", relief=RAISED, width=10, height=1, command = Get)
    detail_btn['font'] = myFont
    detail_btn.place(x=425, y=670)
    exit_btn = Button(root, fg="black", text="Exit", relief=RAISED, width=10, height=1)
    exit_btn['font'] = myFont
    exit_btn.place(x=600, y=670)
    exit_btn.bind('<Button-1>', quit)
    id_lab = Label(text="NIC no : ", bg='#4b3c4f', fg='white')
    id_lab['font'] = myFont
    id_lab.place(x=50, y=100)
    name_lab = Label(text="Name : ", bg='#4b3c4f', fg='white')
    name_lab['font'] = myFont
    name_lab.place(x=50, y=150)
    age_lab = Label(text="Age : ", bg='#4b3c4f', fg='white')
    age_lab['font'] = myFont
    age_lab.place(x=50, y=200)
    gen_lab = Label(text="Gender : ", bg='#4b3c4f', fg='white')
    gen_lab['font'] = myFont
    gen_lab.place(x=50, y=250)
    nation_lab = Label(text="Nationality : ", bg='#4b3c4f', fg='white')
    nation_lab['font'] = myFont
    nation_lab.place(x=50, y=300)
    # crime_lab= Label(text = "Criminal Record : ", bg = '#4b3c4f', fg= 'white')
    # crime_lab['font'] = myFont
    # crime_lab.place(x= 50, y=350)
    # crime_lab1= Label(text = "None", bg = '#4b3c4f', fg= 'white')
    # crime_lab1['font'] = myFont
    # crime_lab1.place(x= 300, y=350)
    inst_lab = Label(text="Instructions:\n- Start/Restart Surveillance by clicking on Start Button\n- After finding Suspicious person press 'q'\n- Click on Detail Button to get detail of that person\n- Click Exit to exit",bg='#4b3c4f', fg='white')
    inst_lab['font'] = myFont
    inst_lab.place(x=200, y=500)
    root.mainloop()


# Welcome window
root1 = Tk()
root1.title("MS Security")
root1.geometry('800x800+740+0')
root1.minsize(800,800)
root1.maxsize(800,800)
main_win_image = ImageTk.PhotoImage(Image.open('F:/py programs/Surveillance project/gui-image/project-gui1.JPEG')) # Gui image in change as you need
main_win_img = Label(root1, image=main_win_image)
main_win_img .pack(fill ='both')
myFont = font.Font(family='Arial', size=15, weight='bold')
ok_btn = Button(root1,fg="black", text="Next", relief=RAISED, width=10, command = secwind)
ok_btn['font'] = myFont
ok_btn.place(x=600, y=690)
root1.mainloop()
