from customtkinter import *
from CTkListbox import *

def info(selected_option):
    print(selected_option)


set_appearance_mode("dark")
app = CTk()
app.title("Pokedex")
app.geometry("800x500")
app.grid_rowconfigure((0,1), weight=1)
app.grid_columnconfigure((0,1,2), weight=1)

list_frame = CTkFrame(app,fg_color='blue')
list_frame.grid(row=0, column=0, rowspan=2, padx=(20,0), pady=20, sticky='nsew')
list_frame.grid_columnconfigure(0, weight=1)
# list_frame.grid_rowconfigure(0,weight=1)

spriteFrame = CTkFrame(app, fg_color='red')
spriteFrame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

detailsFrame = CTkFrame(app, fg_color='purple')
detailsFrame.grid(row=0, column=2, padx=(0,20), pady=20, sticky='nsew')

statsFrame = CTkFrame(app, fg_color='orange')
statsFrame.grid(row=1, column=1, columnspan=2, padx=20, pady=(0,20), sticky='nsew')

sortButton = CTkSegmentedButton(list_frame, values=['ID#', 'Name', 'Type'])
sortButton.grid(row=0, column=0, stick='new')

selectPokemon = CTkListbox(list_frame, command=info)
selectPokemon.grid(row=1, column=0, sticky='nsew')
selectPokemon.insert(0,'dlsnd')



app.mainloop()


