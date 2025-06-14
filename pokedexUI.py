from customtkinter import *
from CTkListbox import *
from main import get_names, format_stats, format_details,get_info


pokemonNames = get_names('pokemon.txt')

def info(selected_option):
    name = selected_option[1]
    pokemonLabel.configure(text=name)
    print(name)

set_appearance_mode("dark")
app = CTk()
app.title("Pokedex")
app.geometry("800x500")
app.grid_rowconfigure((0,1), weight=1)
app.grid_columnconfigure((0,1,2), weight=1)

#holds sort button and listbox
list_frame = CTkFrame(app,fg_color='blue')
list_frame.grid(row=0, column=0, rowspan=2, padx=(20,0), pady=20, sticky='nsew')

#holds sprite
spriteFrame = CTkFrame(app, fg_color='red')
spriteFrame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

#holds name and details
detailsFrame = CTkFrame(app, fg_color='purple')
detailsFrame.grid(row=0, column=2, padx=(0,20), pady=20, sticky='nsew')

#holds dex entry and stats
statsFrame = CTkFrame(app, fg_color='orange')
statsFrame.grid(row=1, column=1, columnspan=2, padx=20, pady=(0,20), sticky='nsew')

#listframe widgets
list_frame.grid_columnconfigure(0, weight=1)
list_frame.grid_rowconfigure(0,weight=0)
list_frame.grid_rowconfigure(1,weight=1)

sortButton = CTkSegmentedButton(list_frame, values=['ID#', 'Name', 'Type'])
sortButton.grid(row=0, column=0, sticky='new')

selectPokemon = CTkListbox(list_frame, command=info)
selectPokemon.grid(row=1, column=0,sticky='nsew')
i = 0
for pokemon in pokemonNames:
    selectPokemon.insert(i,(i+1,pokemon))
    i +=1 


#detailsFrame widgets
detailsFrame.grid_columnconfigure(0, weight=1)
detailsFrame.grid_rowconfigure(0, weight=1)
pokemonLabel = CTkLabel(detailsFrame, text='Pokemon', font=('Arial', 20, 'bold'))
pokemonLabel.grid(row=0, column=0, sticky='new')
detailsText = CTkTextbox(
    detailsFrame, 
    wrap='word', 
    font=('Arial', 12), 
    fg_color='white', 
    state='disabled'
    )
detailsText.grid(row=1, column=0, sticky='nsew')



app.mainloop()


