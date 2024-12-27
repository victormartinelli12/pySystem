import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import matplotlib


class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.dash_page()

    def dash_page(self) -> None:
        self.title('Página de Relatórios')
        self.geometry('1200x600')
        self.maxsize(1200, 600)
        self.minsize(1200, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        frame = ctk.CTkFrame(master=self, width=210, height=605,
                             fg_color='#0B1B32', corner_radius=20)
        frame.place(relx=0.07, rely=0.498, anchor='center')

        icon = ctk.CTkLabel(master=self, text='🎯', font=('Poppins', 50),
                            text_color='#f6f6f6', fg_color='#0B1B32')
        icon.place(relx=0.04, rely=0.04)

        item_name = ctk.CTkLabel(master=self, text='Dashboards', font=('Poppins', 28, 'bold'),
                                 text_color='#0D1E4C')
        item_name.place(relx=0.25, rely=0.07, anchor='center')

        back_init = ctk.CTkButton(master=self, text='⬅️', text_color='#f6f6f6',
                                  fg_color='#0B1B32', hover_color='#83A6CE', corner_radius=12,
                                  bg_color='#0B1B32', height=40, width=120,
                                  font=('Poppins', 30, 'bold'))
        back_init.place(relx=0.076, rely=0.9, anchor='center')

        revenue_frame = ctk.CTkFrame(master=self, width=250, height=75, fg_color='#26415E',
                                     corner_radius=12)
        revenue_frame.place(relx=0.29, rely=0.23, anchor='center')

        title_revenue = ctk.CTkLabel(master=revenue_frame, text='💸  Receitas', text_color='#f6f6f6',
                                     font=('Poppins', 16, 'bold'))
        title_revenue.place(relx=0.25, rely=0.22, anchor='center')

        clients_frame = ctk.CTkFrame(master=self, width=250, height=75, fg_color='#26415E',
                                     corner_radius=12)
        clients_frame.place(relx=0.575, rely=0.23, anchor='center')

        title_clients = ctk.CTkLabel(master=clients_frame, text='👤  Clientes', text_color='#f6f6f6',
                                     font=('Poppins', 16, 'bold'))
        title_clients.place(relx=0.25, rely=0.22, anchor='center')

        sale_frame = ctk.CTkFrame(master=self, width=250, height=75, fg_color='#26415E',
                                  corner_radius=12)
        sale_frame.place(relx=0.87, rely=0.23, anchor='center')

        title_sale = ctk.CTkLabel(master=sale_frame, text='🤝  Vendas', text_color='#f6f6f6',
                                  font=('Poppins', 16, 'bold'))
        title_sale.place(relx=0.25, rely=0.22, anchor='center')

        revenue_dash = ctk.CTkFrame(master=self, width=250, height=340, fg_color='#26415E',
                                    corner_radius=12, border_width=3,
                                    border_color='#0B1B32')
        revenue_dash.place(relx=0.29, rely=0.65, anchor='center')

        clients_dash = ctk.CTkFrame(master=self, width=250, height=340, fg_color='#26415E',
                                    corner_radius=12, border_width=3,
                                    border_color='#0B1B32')
        clients_dash.place(relx=0.575, rely=0.65, anchor='center')

        sale_dash = ctk.CTkFrame(master=self, width=250, height=340, fg_color='#26415E',
                                 corner_radius=12, border_width=3,
                                 border_color='#0B1B32')
        sale_dash.place(relx=0.87, rely=0.65, anchor='center')


if __name__ == '__main__':
    dashboard: Dashboard = Dashboard()
    dashboard.mainloop()
