from customtkinter import *
from random import *
from play_arena import *


#creating main widget
root=CTk()
w=root.winfo_screenwidth()
#setting title
root.title("Let's date")
#gets width and height of the screen
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()
#sets the size of main window to width and height of the screen  
root.geometry("%dx%d" %(width,height))
#default theme is set to dark
set_appearance_mode('dark')
#widget themes are set to green
set_default_color_theme('green')
#main windows icon
icon = ".\icons8-statue-of-liberty-100.ico"
root.iconbitmap(icon)


#fucnctions to be displayed on a blank page
def create_blank_page():

    #functions to be displayed after pressing randomised button
    def random():

        #function to reset randomised date and month
        def back2():
            randomize.place(relx=0.445, rely=0.05)
            month_date_disp.place_forget()
            reset_button.place_forget()
            back_button1.place(relx=0.45, rely=0.92)
            show_content.place_forget() 


        #function to display the text regarding the events
        def context():
            events_display_frame=CTkScrollableFrame(t1, width=w, height=560, label_anchor='e')
            events_display_frame.pack()
            a=web_scrap(month,date)
            text_context=CTkLabel(events_display_frame,text=a, font=('Helvetica', 20), justify=LEFT, wraplength=w-50)
            text_context.pack()
        
        
        
        randomize.place_forget()
        #randomised month and date displayed
        values=["January", "February","March","April","May","June","July",
                "August","September","October","November","December"]
        month=choice(values)
        if month==values[0] or month==values[2] or month==values[4] or month==values[6] or month==values[7] or month==values[9] or month==values[11]:
            date=randrange(1,32)
        elif month==values[1]:
            date=randrange(1,29)
        else:
            date=randrange(1,30)
        #label displayed randomised month and date
        month_date_disp=CTkLabel(t1, text=f'{month} , {date}', font=('pacifico',40))
        month_date_disp.place(relx=0.5, rely=0.1, anchor='center')
        #button to reset the displayed randomised month and date
        reset_button=CTkButton(t1, text=('🔄'), command=back2, font=('pacifico',15), corner_radius=130, width=8)
        reset_button.place(relx=0.6, rely=0.08)
        #button to show content regarding events
        show_content=CTkButton(t1, text="Show Content",font=('pacifico',15), corner_radius=130, width=8, command=context)
        show_content.place(relx=0.45,rely=0.18)


    #funtion to go back from tabs page to title page
    def back():
        
        title_label.pack()
        description_label.pack()
        new.place(relx=0.44, rely=0.7)
        exit.place(relx=0.4605, rely=0.8)
        back_button1.place_forget()
        tabview.pack_forget()

    #funtions to display calender
    def calender_disp():
        nonlocal months_list
        selected_month=months_list.get()
        


        #funtion to display the selecred month and date
        def date(d):
            nonlocal selected_month

            #function to show text regarding selected month and date
            def context():
                events_display_frame=CTkScrollableFrame(t2, width=w, height=950, label_anchor='e')
                events_display_frame.pack()
                a=web_scrap(selected_month,selected_date)
                text_context=CTkLabel(events_display_frame,text=a, font=('Helvetica', 20), justify=LEFT, wraplength=w-50)
                text_context.pack()
            

            #assigning a variable to the selected date
            selected_date=d
            month_disp.place_forget()
            date_disp_frame.place_forget()



            #dislpaying date selected by user
            date=CTkLabel(t2, text=f'{selected_month} , {selected_date}', font=('pacifico',40))
            date.place(relx=0.5, rely=0.1, anchor='center')
            reset_button_3.place_forget()

            #button to display text regarding events 
            show_content=CTkButton(t2, text="Show Content",font=('pacifico',15), corner_radius=130, width=8, command=context)
            show_content.place(relx=0.45,rely=0.18)

            #function to go back to month selection page
            def back3():
                month_disp.place(relx=0.435, rely=0.05)
                date_disp_frame.place(relx=0.255, rely=0.2)
                date.place_forget()
                reset_button_2.place_forget()
                reset_button_3.place(relx=0.635, rely=0.125)
                show_content.place_forget()
            #button to go back to month selection page
            reset_button_2=CTkButton(t2, text=('🔄'), command=back3, font=('pacifico',15), corner_radius=130, width=8)
            reset_button_2.place(relx=0.60, rely=0.079)


        #function to go back to month selection page
        def back4():
                month_disp.place_forget()
                date_disp_frame.place_forget()
                months_list.place(relx=0.425, rely=0.3)
                submit_button.place(relx=0.450, rely=0.45)
                reset_button_3.place_forget()


        if selected_month=='':
            pass
        else:
            submit_button.place_forget()
            months_list.place_forget()
            #displaying selected month
            month_disp=CTkLabel(t2, text=selected_month, font=('pacifico', 40), padx=15)
            month_disp.place(relx=0.435, rely=0.05)
            #button to go back to month selection page
            reset_button_3=CTkButton(t2, text=('🔄'), command=back4, font=('pacifico',15), corner_radius=130, width=8)
            reset_button_3.place(relx=0.635, rely=0.110)
            #dates displaying page
            date_disp_frame=CTkFrame(t2, width=600, height=450)
            date_disp_frame.place(relx=0.255, rely=0.2)
            #creating buttons with each date
            date1=CTkButton(date_disp_frame, text='01', font=('pacifico',25), width=15, height=7,
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('1'))
            date1.place(relx=0.17, rely=0.05)
            date2=CTkButton(date_disp_frame, text='02', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('2'))
            date2.place(relx=0.27, rely=0.05)
            date3=CTkButton(date_disp_frame, text='03', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('3'))
            date3.place(relx=0.37, rely=0.05)
            date4=CTkButton(date_disp_frame, text='04', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('4'))
            date4.place(relx=0.47, rely=0.05)
            date5=CTkButton(date_disp_frame, text='05', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('5'))
            date5.place(relx=0.57, rely=0.05)
            date6=CTkButton(date_disp_frame, text='06', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('6'))
            date6.place(relx=0.67, rely=0.05)
            date7=CTkButton(date_disp_frame, text='07', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('7'))
            date7.place(relx=0.77, rely=0.05)
            date8=CTkButton(date_disp_frame, text='08', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('8'))
            date8.place(relx=0.17, rely=0.15)
            date9=CTkButton(date_disp_frame, text='09', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('9'))
            date9.place(relx=0.27, rely=0.15)
            date10=CTkButton(date_disp_frame, text='10', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('10'))
            date10.place(relx=0.37, rely=0.15)
            date11=CTkButton(date_disp_frame, text='11', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('11'))
            date11.place(relx=0.47, rely=0.15)
            date12=CTkButton(date_disp_frame, text='12', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('12'))
            date12.place(relx=0.57, rely=0.15)
            date13=CTkButton(date_disp_frame, text='13', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('13'))
            date13.place(relx=0.67, rely=0.15)
            date14=CTkButton(date_disp_frame, text='14', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('14'))
            date14.place(relx=0.77, rely=0.15)
            date15=CTkButton(date_disp_frame, text='15', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('15'))
            date15.place(relx=0.17, rely=0.25)
            date16=CTkButton(date_disp_frame, text='16', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('16'))
            date16.place(relx=0.27, rely=0.25)
            date17=CTkButton(date_disp_frame, text='17', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('17'))
            date17.place(relx=0.37, rely=0.25)
            date18=CTkButton(date_disp_frame, text='18', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('18'))
            date18.place(relx=0.47, rely=0.25)
            date19=CTkButton(date_disp_frame, text='19', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('19'))
            date19.place(relx=0.57, rely=0.25)
            date20=CTkButton(date_disp_frame, text='20', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('20'))
            date20.place(relx=0.67, rely=0.25)
            date21=CTkButton(date_disp_frame, text='21', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('21'))
            date21.place(relx=0.77, rely=0.25)
            date22=CTkButton(date_disp_frame, text='22', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('22'))
            date22.place(relx=0.17, rely=0.35)
            date23=CTkButton(date_disp_frame, text='23', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('23'))
            date23.place(relx=0.27, rely=0.35)
            date24=CTkButton(date_disp_frame, text='24', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('24'))
            date24.place(relx=0.37, rely=0.35)
            date25=CTkButton(date_disp_frame, text='25', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('25'))
            date25.place(relx=0.47, rely=0.35)
            date26=CTkButton(date_disp_frame, text='26', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('26'))
            date26.place(relx=0.57, rely=0.35)
            date27=CTkButton(date_disp_frame, text='27', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('27'))
            date27.place(relx=0.67, rely=0.35)
            date28=CTkButton(date_disp_frame, text='28', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('28'))
            date28.place(relx=0.77, rely=0.35)
            date29=CTkButton(date_disp_frame, text='29', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('29'))
            date29.place(relx=0.17, rely=0.45)
            date30=CTkButton(date_disp_frame, text='30', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('30'))
            date30.place(relx=0.27, rely=0.45)
            date31=CTkButton(date_disp_frame, text='31', font=('pacifico',25), width=15, height=7, 
                            corner_radius=70, fg_color='transparent', hover=False, command=lambda:date('31'))
            date31.place(relx=0.37, rely=0.45)
            #specifying which month should have 31 days, 30 days, 29 days
            if selected_month not in ['January','March','May','July','August','October','December']:
                date31.place_forget()
                if selected_month == 'February':
                    date30.place_forget()



    #removing widgets placed in title window
    title_label.pack_forget()
    description_label.pack_forget()
    new.place_forget()
    exit.place_forget()

    #create tabs
    tabview=CTkTabview(root, width=w, height=855)
    tabview.pack()
    t1=tabview.add('Randomize')
    t2=tabview.add('Select date')
    #setting default tab to 'Randomize'
    tabview.set('Randomize')
    



    #creating a dropdown menu with all the months in tab 2
    months_list_var=StringVar(value='')
    months_list=CTkComboBox(t2, variable=months_list_var, values=["January", "February","March","April","May","June","July",
                                    "August","September","October","November","December"], corner_radius=50,
                                    justify='left', dropdown_font=('pacifico',15), font=('pacifico',20), width=200, height=40)
    months_list.place(relx=0.425, rely=0.3)
    submit_button=CTkButton(t2, text='Submit', font=('pacifico',20), command=calender_disp, corner_radius=100)
    submit_button.place(relx=0.450, rely=0.45)


    #creating a button to display a randomised date and month
    randomize=CTkButton(t1, text='Roll the die!', command=random,font=('pacifico',20), corner_radius=100)
    randomize.place(relx=0.445, rely=0.05)


    #button to go back to main page
    back_button1=CTkButton(root, text=('Back'), command=back, font=('pacifico',20), corner_radius=130)
    back_button1.place(relx=0.45, rely=0.92)


#theme toggling switch's function
def theme():
    if switch_var.get() == 'on':
        set_appearance_mode('light')
        mode=CTkLabel(root, text='Turn off the light💡',font=('pacifico', 15))
        mode.place(relx=0.864, rely=0.005)
    else:
        set_appearance_mode('dark')
        mode=CTkLabel(root, text='Turn on the light💡',font=('pacifico', 15))
        mode.place(relx=0.865, rely=0.005)





#create a widget to display title
title_label=CTkLabel(root, text="Let's Date", font=('whisper',160),padx=15)
title_label.pack()
#create a widget to display description
description_label=CTkLabel(root, text='Embark on a captivating journey through time with our app! Enter any date,\nand instantly unlock a treasure trove of fascinating historical events that shaped the world.', font=('pacifico',20),anchor='center')
description_label.pack()
#create a button to open a blank page
new=CTkButton(root, text="Discover History!", command=create_blank_page, height=40, border_spacing=5,
               font=('pacifico',20), corner_radius=100, hover=True, hover_color='dark green')
new.place(relx=0.44, rely=0.7)
#create a button to destry main window(Exit the app)
exit=CTkButton(root, text="Time's up!", command=root.destroy, height=40, border_spacing=5,
               font=('pacifico',20), corner_radius=100, hover=True, hover_color='dark green')
exit.place(relx=0.4605, rely=0.8)
#a togglable switch to change theme
switch_var=StringVar(value='off')
toggle_theme=CTkSwitch(root, text=' ', command=theme, variable=switch_var, onvalue='on', offvalue='off')
toggle_theme.place(relx=0.97, rely=0.01)
#text for the switch
mode=CTkLabel(root, text='Turn on the light💡', font=('pacifico', 15))
mode.place(relx=0.865, rely=0.005)


#set the state of the main window to zoomed(maximized)
root.state('zoomed')


#mainloop for the app
root.mainloop()
