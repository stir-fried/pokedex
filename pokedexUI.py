from customtkinter import *

set_appearance_mode("dark")
app = CTk()
app.title("Pokedex")
app.geometry("800x500")
app.grid_rowconfigure((0,1), weight=1)
app.grid_columnconfigure((0,1,2), weight=1)

list_frame = CTkFrame(app,fg_color='blue')
list_frame.grid(row=0, column=0, rowspan=2, padx=(20,0), pady=20, sticky='nsew')

sprite_frame = CTkFrame(app, fg_color='red')
sprite_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

details_frame = CTkFrame(app, fg_color='purple')
details_frame.grid(row=0, column=2, padx=(0,20), pady=20, sticky='nsew')

stats_frame = CTkFrame(app, fg_color='orange')
stats_frame.grid(row=1, column=1, columnspan=2, padx=20, pady=(0,20), sticky='nsew')



app.mainloop()
