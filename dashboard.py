import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#394d55", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"]
)

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

# Chart 2: Horizontal bar chart of inventory data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")

# Chart 3: Pie chart of product data
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title("Product \nBreakdown")

# Chart 4: Line chart of sales by year
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")

# Chart 5: Area chart of inventory by month
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")

# Create a window and add charts
root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')

# Sidebar
side_frame = tk.Frame(root, bg="#394d55")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#394d55", fg="#FFF", font=("Arial", 20, "bold"))
label.pack(pady=50, padx=20)

# Admin options
options = [
    "Manage Users",
    "View Reports",
    "Add Products",
    "Update Inventory",
    "Logout",
]

for option in options:
    btn = tk.Button(
        side_frame,
        text=option,
        bg="#394d55",
        fg="white",
        font=("Arial", 14),
        relief="flat",
        padx=10,
        pady=10,
        command=lambda opt=option: print(f"{opt} clicked")  # Placeholder for actual functionality
    )
    btn.pack(fill="x", padx=20, pady=5)

# Charts frame
charts_frame = tk.Frame(root)
charts_frame.pack()

# Upper frame for the first three charts
upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

# Lower frame for the remaining two charts
lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()
