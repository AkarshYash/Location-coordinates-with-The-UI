from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder, NumberParseException
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

# Initialize the main window
root = Tk()
root.title("c683e23dd4d642db8559f0256d9b6aec")
root.geometry("400x650+500+100")
root.resizable(False, False)
root.configure(bg='#96BFFF')

# Replace with your valid OpenCage API key
API_KEY = ("c683e23dd4d642db8559f0256d9b6aec")

# Function to track the phone number
def track():
    try:
        # Get the phone number from user input
        entered_number = entry.get()
        number = phonenumbers.parse(entered_number)

        # Get location and carrier information
        location = geocoder.description_for_number(number, 'en')
        service = carrier.name_for_number(number, 'en')

         # Update the labels with the fetched data
        country.config(text=f"Country: {location}")
        sim.config(text=f"SIM: {service}")

        # Use OpenCage to fetch latitude and longitude
        geocoder_api = OpenCageGeocode('c683e23dd4d642db8559f0256d9b6aec')
        results = geocoder_api.geocode(location)

        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']

            # Create and save the map
            my_map = folium.Map(location=[lat, lng], zoom_start=10)
            folium.Marker([lat, lng], popup=location).add_to(my_map)
            my_map.save("myLocation.html")
            messagebox.showinfo("Success", "Location map generated successfully!")

        else:
            messagebox.showwarning("Error", "Location not found.")
    except NumberParseException:
        messagebox.showerror("Invalid Input", "Please enter a valid phone number.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Function to open the generated map in a web browser
def open_map():
    try:
        webbrowser.open("myLocation.html")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open map: {e}")

# GUI Elements
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#96BFFF").place(x=135, y=40)

heading = Label(root, text="Track Number", font='Arial 20 bold', 
                fg="#39281E", bg="#96BFFF")
heading.place(x=90, y=190)

entry = StringVar()
enter_nb = Entry(root, textvariable=entry, width=17, justify='center', 
                 bd=0, font='Arial 20', bg="#2C3541", fg="white")
enter_nb.place(x=54, y=258)

search_icon = PhotoImage(file="search_icon.png")
btn = Button(root, image=search_icon, cursor='hand2', bg="#96BFFF", 
             bd=0, command=track, activebackground='#ED8051')
btn.place(x=155, y=308)

country = Label(root, text="Country: N/A", bg='#96BFFF', fg='black', 
                font='Arial 14 bold')
country.place(x=55, y=370)

sim = Label(root, text="SIM: N/A", bg='#96BFFF', fg='sky blue', 
            font='Arial 14 bold')
sim.place(x=55, y=410)

open_map_btn = Button(root, text="View Location", width=12, cursor='hand2', 
                      bg="#EE8C62", bd=0, command=open_map, 
                      activebackground='#ED8051', font='Arial 14 bold')
open_map_btn.place(x=120, y=470)

insta_page = Label(root, text="@Akarsh Chaturvedi", bg='#96BFFF', 
                   fg='black', font='Arial 10 bold italic')
insta_page.place(x=135, y=600)

# Run the application
root.mainloop()
