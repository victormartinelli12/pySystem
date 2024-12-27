import customtkinter as ctk
import requests
from CTkTable import CTkTable
from addsup import AddSupply
from dashboard import Dashboard
from sale import Sale


class Page(ctk.CTk):
    def __init__(self, status_login: bool = False):
        super().__init__()
        self.status_login = status_login
        if self.status_login:
            self.open_adm_page()

    def open_adm_page(self) -> None:
        self.title('Sistema Gerencial')
        self.geometry('1200x600')
        self.maxsize(1200, 600)
        self.minsize(1200, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        frame = ctk.CTkFrame(master=self, width=210, height=605,
                             fg_color='#0B1B32', corner_radius=20)
        frame.place(relx=0.07, rely=0.498, anchor='center')

        icon = ctk.CTkLabel(master=self, text='📦', font=('Poppins', 50),
                            text_color='#f6f6f6', fg_color='#0B1B32')
        icon.place(relx=0.04, rely=0.04)

        item_name = ctk.CTkLabel(master=self, text='Fornecedores', font=('Poppins', 28, 'bold'),
                                 text_color='#0D1E4C')
        item_name.place(relx=0.27, rely=0.07, anchor='center')

        open_add_supply = ctk.CTkButton(master=self, text='+  Novo Forncedor', text_color='#f6f6f6',
                                        fg_color='#26415E', hover_color='#83A6CE', corner_radius=12,
                                        bg_color='transparent', height=40, width=120,
                                        font=('Poppins', 15, 'bold'), command=self.open_new_supply)
        open_add_supply.place(relx=0.86, rely=0.07, anchor='center')

        count_supply = ctk.CTkFrame(master=self, width=250, height=75, fg_color='#26415E',
                                    bg_color='transparent', corner_radius=12)
        count_supply.place(relx=0.295, rely=0.23, anchor='center')

        name_supply = ctk.CTkLabel(master=count_supply, font=('Poppins', 16, 'bold'),
                                   text='Forncedores', text_color='#f6f6f6')
        name_supply.place(relx=0.25, rely=0.18, anchor='center')

        count_item = ctk.CTkFrame(master=self, width=250, height=75, fg_color='#26415E',
                                  bg_color='transparent', corner_radius=12)
        count_item.place(relx=0.47, rely=0.17)

        item_stock = ctk.CTkLabel(master=count_item, font=('Poppins', 16, 'bold'),
                                  text='Disponível', text_color='#f6f6f6')
        item_stock.place(relx=0.23, rely=0.18, anchor='center')

        count_minus = ctk.CTkFrame(master=self, width=250, height=75, fg_color='#26415E',
                                   bg_color='transparent', corner_radius=12)
        count_minus.place(relx=0.72, rely=0.17)

        item_minus = ctk.CTkLabel(master=count_minus, font=('Poppins', 16, 'bold'),
                                  text='Faltante', text_color='#f6f6f6')
        item_minus.place(relx=0.21, rely=0.18, anchor='center')

        main_frame = ctk.CTkFrame(master=self, width=880, height=60,
                                  fg_color='#d0d0d0')
        main_frame.place(relx=0.19, rely=0.35)

        self.find_order = ctk.CTkEntry(master=main_frame, placeholder_text='Pesquisar Fornecedor',
                                       placeholder_text_color='#26415E', font=('Poppins', 15),
                                       width=460, border_color='#26415E', border_width=2,
                                       text_color='#26415E')
        self.find_order.place(relx=0.28, rely=0.5, anchor='center')

        self.date = self.status_supply = ctk.CTkComboBox(
            master=main_frame, width=160, height=30, font=('Poppins', 15),
            dropdown_fg_color='#26415E', justify='left', values=['Data'],
            text_color='#0D1E4C', dropdown_hover_color='#83A6CE', button_color='#26415E',
            text_color_disabled='#83A6CE', dropdown_text_color='#f6f6f6',
            button_hover_color='#26415E', border_width=2, border_color='#26415E')
        self.date.place(relx=0.66, rely=0.5, anchor='center')

        self.status = self.status_supply = ctk.CTkComboBox(
            master=main_frame, width=160, height=30, font=('Poppins', 15),
            dropdown_fg_color='#26415E', justify='left', values=['Status', 'Ativo', 'Inativo'],
            text_color='#0D1E4C', dropdown_hover_color='#83A6CE', button_color='#26415E',
            text_color_disabled='#83A6CE', dropdown_text_color='#f6f6f6',
            button_hover_color='#26415E', border_width=2, border_color='#26415E')
        self.status.place(relx=0.88, rely=0.5, anchor='center')

        open_dashboard = ctk.CTkButton(master=self, text='📈 Dashboards', text_color='#f6f6f6',
                                       fg_color='#0B1B32', hover_color='#83A6CE', corner_radius=12,
                                       bg_color='#0B1B32', height=40, width=120,
                                       font=('Poppins', 14, 'bold'), command=self.open_dash_btn)
        open_dashboard.place(relx=0.076, rely=0.4, anchor='center')

        open_sales_info = ctk.CTkButton(master=self, text='🛒 Vendas', text_color='#f6f6f6',
                                       fg_color='#0B1B32', hover_color='#83A6CE', corner_radius=12,
                                       bg_color='#0B1B32', height=40, width=140,
                                       font=('Poppins', 14, 'bold'), command=self.open_sale)
        open_sales_info.place(relx=0.076, rely=0.5, anchor='center')


        table_data = self.show_all_orders() 
        all_orders = ctk.CTkScrollableFrame(master=self, fg_color='#d0d0d0', width=855,
                                           height=220, corner_radius=10,
                                           scrollbar_button_color='#0B1B32',
                                           scrollbar_button_hover_color='#26415E',
                                           label_text='Tabela de Fornecedores', label_anchor='center',
                                           label_text_color='#f6f6f6', label_font=('Poppins', 15, 'bold'),
                                           label_fg_color='#0B1B32', orientation='vertical')
        all_orders.place(relx=0.556, rely=0.73, anchor='center')

        text_orders = CTkTable(master=all_orders, column=5, values=table_data,
                                   font=('Poppins', 15), text_color='#FFFFF0',
                                   header_color='#26415E', colors=['#B3D4E0', '#9BBFD3'])
        text_orders.pack(expand=True)
        
    def show_all_orders(self) -> list:
        url = 'https://firestore.googleapis.com/v1/projects/sistema-bb725/databases/(default)/documents/fornecedores'
        params = {
            'mask.fieldPaths': ['name', 'category', 'address', 'product', 'status']
        }
        response = requests.get(
            url, params=params
        )
        response_data = response.json()

        table_data = [['Nome', 'Categoria', 'Endereço', 'Produto', 'Status']]

        if 'documents' not in response_data:
            print("Nenhum documento encontrado na coleção.")
            return table_data
        for document in response_data['documents']:
            fields = document.get('fields', {})
            row = [
                fields.get('name', {}).get('stringValue', 'N/A'),
                fields.get('category', {}).get('stringValue', 'N/A'),
                fields.get('address', {}).get('stringValue', 'N/A'),
                fields.get('product', {}).get('stringValue', 'N/A'),
                fields.get('status', {}).get('stringValue', 'N/A'),
            ]
            table_data.append(row)
        
        return table_data

    def open_dash_btn(self) -> None:
        show_dash: Dashboard = Dashboard()
        show_dash.mainloop()

    def open_new_supply(self) -> None:
        add_sup: AddSupply = AddSupply(status_login=self.status_login)
        add_sup.mainloop()
        
    def open_sale(self) -> None:
        sale: Sale = Sale()
        sale.mainloop()

if __name__ == '__main__':
    page: Page = Page(status_login=True)
    page.mainloop()