import customtkinter as ctk
from tkinter import ttk
import ttkbootstrap as tb


ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Pharmacy Inventory")
root.geometry('1024x720')
root.resizable(width=True, height=True)

# CREATING A HEADER FOR THE APPLICATION
header = ctk.CTkLabel(root, text="PHARMACY INVENTORY MANAGEMENT", font=("Arial", 20, "bold"), fg_color="#00FFFF", text_color="black", height=50)
header.pack(fill="x")


# CREATING MAIN CONTENT FRAME
content_frame = ctk.CTkFrame(root)  # This frame will change dynamically
content_frame.pack(expand=True, fill='both')


nav_frame = ctk.CTkFrame(content_frame, fg_color="white")
dbheader = ctk.CTkLabel(nav_frame, text='DASHBOARD', font=("Arial", 30, 'bold'), text_color='black')
dbheader.pack(fill='x')
nav_frame.pack(fill="x", pady=10)


# FUNCTION TO CLEAR AND LOAD NEW PAGE
def show_page(page_function):
    for widget in content_frame.winfo_children():
        widget.destroy()
    page_function()

# INVENTORY PAGE
def inventory_page():
    inv_frame=ctk.CTkFrame(content_frame)
    inv_frame.pack(expand=True, fill='both', pady=10)

    #HEADER = 'INVENTORY MANAGEMENT'
    inv_headerframe=ctk.CTkFrame(inv_frame, fg_color='white')
    inv_headerframe.pack(fill='x')
    inv_back=ctk.CTkButton(inv_headerframe, text='BACK TO DASHBOARD', font=('Arial', 20,'italic'), corner_radius=30, fg_color='#dbdbdb', text_color='black', hover_color='#E7CD78')
    inv_back.grid(row=0, column=0, padx=10, sticky='w')

    label = ctk.CTkLabel(inv_headerframe, text="Inventory Management", font=("Arial", 30, 'bold'), bg_color='white')
    label.grid(row=0, column=1, padx=10, sticky='ew')
      
    inv_nextbtn= ctk.CTkButton(inv_headerframe, text='MEDICINE INFORMATION', font=('Arial', 20, 'italic'), corner_radius=30, fg_color='#dbdbdb', text_color='black', hover_color='#E7CD78')
    inv_nextbtn.grid(row=0, column=2, padx=10, sticky='e')
    
    inv_headerframe.grid_columnconfigure(0, weight=1)  
    inv_headerframe.grid_columnconfigure(1, weight=2)
    inv_headerframe.grid_columnconfigure(2, weight=1)
   
    def treeviewtable():
        table_frame = ctk.CTkFrame(inv_frame)
        table_frame.pack(fill="x", padx=20, pady=10)

        # Creating the table view
        columns = ("ID", "Name", "Batch No", "Form","Manufactured date", "Expiry Date", "Price", "Quantity", "Days remaining")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings") 

        # Define Column Headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120)

        tree.pack(fill="both", padx=10, pady=10) 

    treeviewtable()
    
    #4 frames for the CRUD operations
    
    add_frame=ctk.CTkFrame(inv_frame)
    update_frame=ctk.CTkFrame(inv_frame, corner_radius=10)
    delete_frame=ctk.CTkFrame(inv_frame, corner_radius=10)
    search_frame=ctk.CTkFrame(inv_frame, corner_radius=10)
    
    add_frame.pack(side='left', fill='both', expand=True, padx=20)
    update_frame.pack(side='left', fill='both', expand=True, padx=20)
    delete_frame.pack(side='right', fill='both', expand=True, padx=20)
    search_frame.pack(side='right', fill='both', expand=True, padx=20)
    
     #CREATING Action tabs
    AB1=ctk.CTkLabel(add_frame, text=' ADD MED ', bg_color='#00FFFF', font= ('Arial', 20, 'bold'))
    AB2=ctk.CTkLabel(update_frame, text='UPDATE MED', bg_color='#00FFFF', font= ('Arial', 20, 'bold'))
    AB3=ctk.CTkLabel(delete_frame, text='DELETE MED', bg_color='#00FFFF', font= ('Arial', 20, 'bold'))
    AB4=ctk.CTkLabel(search_frame, text='SEARCH MED', bg_color='#00FFFF', font= ('Arial', 20, 'bold'))
    #PROCESSING THE BUTTONS
    AB1.pack(side='top', fill='x')
    AB2.pack(side='top', fill='x')
    AB3.pack(side='top', fill='x')
    AB4.pack(side='top', fill='x')
    
    # ADD FRAME FIELDS:
    add_fields = [
        ("ID", "Enter Medicine ID"),
        ("Name", "Enter Medicine Name"),
        ("Batch No", "Enter Batch Number"),
        ("Form of Medicine", "Enter Form of Med"),
        ("Manufactured Date", "Enter Manufactured Date"),
        ("Expiry Date", "Enter Expiry Date"),
        ("Price", "Enter Price"),
        ("Quantity", "Enter Quantity")
    ]

    for field, placeholder in add_fields:
        
        frame = ctk.CTkFrame(add_frame)
        frame.pack(fill='x', padx=10, pady=5)   

        label = ctk.CTkLabel(frame, text=field, font=("Arial", 14))
        label.pack(side='left', padx=5)
        if field =='Form':
            combobox=ctk.CTkComboBox(frame, values=["Tablet", "Capsule", "Syrup", "Injection", "Cream", "Ointment", "Gel", "Inhaler", "Patch", "Drops", "Suppository", "IV Fluid"]  
, state='readonly')
            combobox.pack(side='right', fill='x', expand=True, padx=5)
        
        elif field in ['Manufactured Date', 'Expiry Date']:
            mydate = tb.DateEntry(frame, bootstyle='danger', dateformat='%d-%m-%Y')
            mydate.pack(side='right', fill='x', expand=True, padx=5)
        else:
            entry = ctk.CTkEntry(frame, placeholder_text=placeholder, font=("Arial", 14))
            entry.pack(side='right', fill='x', expand=True, padx=5)
    submit_add_button = ctk.CTkButton(add_frame, text="Submit", font=("Arial", 16), fg_color="green")
    submit_add_button.pack(fill='x', padx=10, pady=10)
    
    ######################################################################################

    #UPDATE OPERATION

    ctk.CTkLabel(update_frame, text='Search by Name or ID', font=('Arial',15,'bold')).pack(pady=(10,0))
    search_entry=ctk.CTkEntry(update_frame)
    search_entry.pack(pady=(10,0))
    
    ctk.CTkLabel(update_frame, text='UPDATE DETAILS', font=('Courier',20,'bold'), bg_color='cyan').pack(pady=(10,0))
    ctk.CTkLabel(update_frame, text="Name").pack(pady=(10, 0))
    name_entry = ctk.CTkEntry(update_frame)
    name_entry.pack(pady=(0, 10))
    
    ctk.CTkLabel(update_frame, text="Batch No").pack(pady=(10, 0))
    batch_entry = ctk.CTkEntry(update_frame)
    batch_entry.pack(pady=(0, 10))

    ctk.CTkLabel(update_frame, text="Price").pack(pady=(10, 0))
    price_entry = ctk.CTkEntry(update_frame)
    price_entry.pack(pady=(0, 10))

    ctk.CTkLabel(update_frame, text="Quantity").pack(pady=(10, 0))
    quantity_entry = ctk.CTkEntry(update_frame)
    quantity_entry.pack(pady=(0, 10))

    # Update Button
    update_button = ctk.CTkButton(update_frame, text="Update", command=lambda: None)  # Placeholder for update functionality
    update_button.pack(pady=(20, 10))


####################################################################################
    #SEARCH OPERATION
    ctk.CTkLabel(search_frame, text='Search by Name or ID', font=('Arial',15,'bold')).pack(pady=(10,0))
    search_entry=ctk.CTkEntry(search_frame)
    search_entry.pack(pady=(10,0))
    

# MEDICINE INFORMATION PAGE
def medicine_info_page():
    label = ctk.CTkLabel(content_frame, text="Medicine Information", font=("Arial", 20, "bold"))
    label.pack(pady=20)
    # Add Medicine Information UI elements here

# ABOUT US PAGE
def about_us_page():
    label = ctk.CTkLabel(content_frame, text="About Us", font=("Arial", 20, "bold"))
    label.pack(pady=20)
    text = ctk.CTkLabel(content_frame, text="This system helps pharmacies manage inventory efficiently.", font=("Arial", 16))
    text.pack(pady=10)
    contact = ctk.CTkLabel(content_frame, text="Contact: pharmacy@example.com | Phone: +91 XXXXX XXXXX", font=("Arial", 14))
    contact.pack(pady=5)

# CREATING DASHBOARD FRAME
dbf = ctk.CTkFrame(content_frame, corner_radius=10)
dbf.pack(expand=True, fill='both')

# LEFT & RIGHT FRAMES
db_Lframe = ctk.CTkFrame(dbf, corner_radius=15)
db_Lframe.pack(side='left', fill='both', expand=True)

db_Rframe = ctk.CTkFrame(dbf, corner_radius=15)
db_Rframe.pack(side='right', fill='both', expand=True)

# RIGHT FRAME BUTTONS
btnframe = ctk.CTkFrame(db_Rframe, height=400, width=300, fg_color='#dbdbdb')
btnframe.pack(expand=True)

buttons = [
    ("Inventory Management & Search", inventory_page),
    ("Medicine Information", medicine_info_page),
    ("About Us", about_us_page)
]

for btn_text, command in buttons:
    btn = ctk.CTkButton(btnframe, text=btn_text, fg_color='white', text_color='black',
                        font=("Arial", 18, "bold"), height=50, width=250, corner_radius=80,
                        command=lambda cmd=command: show_page(cmd), hover_color='#E7CD78')  # Calls respective function
    btn.pack(padx=10, pady=10, fill='both')

root.mainloop()
