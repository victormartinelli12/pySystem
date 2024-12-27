import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import requests


class AddSupply(ctk.CTk):
    def __init__(self, status_login: bool = False):
        super().__init__()
        self.status_login = status_login
        if self.status_login:
            self.open_adm_page()

    def open_adm_page(self) -> None:
        self.title('Base de Fornecedores')
        self.geometry('1200x600')
        self.maxsize(1200, 600)
        self.minsize(1200, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        frame = ctk.CTkFrame(master=self, width=210, height=605,
                             fg_color='#0B1B32', corner_radius=20)
        frame.place(relx=0.07, rely=0.498, anchor='center')

        icon = ctk.CTkLabel(master=self, text='🗂️', font=('Poppins', 50),
                            text_color='#f6f6f6', fg_color='#0B1B32')
        icon.place(relx=0.04, rely=0.04)

        item_name = ctk.CTkLabel(master=self, text='Criar Fornececedor', font=('Poppins', 28, 'bold'),
                                 text_color='#0D1E4C')
        item_name.place(relx=0.3, rely=0.07, anchor='center')

        order_name = ctk.CTkLabel(
            master=self, text='Nome', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        order_name.place(relx=0.215, rely=0.18, anchor='center')

        self.order = ctk.CTkEntry(master=self, width=870, height=40, fg_color='#d0d0d0',
                                  border_width=0, text_color='#0D1E4C', font=('Poppins', 18))
        self.order.place(relx=0.55, rely=0.24, anchor='center')

        category_name = ctk.CTkLabel(
            master=self, text='Categoria', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        category_name.place(relx=0.225, rely=0.33, anchor='center')

        self.category = self.status_supply = ctk.CTkComboBox(
            master=self, width=440, height=40, fg_color='#d0d0d0', font=('Poppins', 16, 'bold'),
            dropdown_fg_color='#26415E', justify='left', values=['Perecível', 'Não Perecível'],
            text_color='#0D1E4C', dropdown_hover_color='#83A6CE', button_color='#26415E',
            text_color_disabled='#83A6CE', dropdown_text_color='#f6f6f6',
            button_hover_color='#26415E', border_width=2, border_color='#26415E')
        self.category.place(relx=0.372, rely=0.4, anchor='center')

        address_name = ctk.CTkLabel(
            master=self, text='Endereço', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        address_name.place(relx=0.625, rely=0.33, anchor='center')

        self.address = ctk.CTkEntry(master=self, width=400, height=40, fg_color='#d0d0d0',
                                    border_width=0, text_color='#0D1E4C', font=('Poppins', 18))
        self.address.place(relx=0.75, rely=0.4, anchor='center')

        description_name = ctk.CTkLabel(
            master=self, text='Descrição', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        description_name.place(relx=0.625, rely=0.48, anchor='center')

        self.description = ctk.CTkTextbox(master=self, width=400, height=270,
                                          text_color='#0D1E4C', font=('Poppins', 15),
                                          fg_color='#d0d0d0')
        self.description.place(relx=0.75, rely=0.74, anchor='center')

        self.product_name = ctk.CTkLabel(
            master=self, text='Produto', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        self.product_name.place(relx=0.22, rely=0.483, anchor='center'
                           )
        
        self.product = ctk.CTkEntry(master=self, width=440, height=40, fg_color='#d0d0d0',
                                    border_width=0, text_color='#0D1E4C', font=('Poppins', 18))
        self.product.place(relx=0.374, rely=0.55, anchor='center')

        status_name = ctk.CTkLabel(
            master=self, text='Status', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        status_name.place(relx=0.215, rely=0.65, anchor='center')

        self.status_supply = ctk.CTkComboBox(
            master=self, width=120, height=40, fg_color='#d0d0d0', font=('Poppins', 16, 'bold'),
            dropdown_fg_color='#26415E', justify='left', values=['Ativo', 'Inativo'],
            text_color='#0D1E4C', dropdown_hover_color='#83A6CE', button_color='#26415E',
            text_color_disabled='#83A6CE', dropdown_text_color='#f6f6f6',
            button_hover_color='#26415E', border_width=2, border_color='#26415E')
        self.status_supply.place(relx=0.24, rely=0.71, anchor='center')

        add_supply = ctk.CTkButton(master=self, text='Adicionar', text_color='#d0d0d0', fg_color='#26415E',
                                   hover_color='#0B1B32', corner_radius=12, bg_color='transparent',
                                   height=40, width=120, font=('Poppins', 15, 'bold'), command=self.btn_add_supply)
        add_supply.place(relx=0.24, rely=0.9, anchor='center')

        clear_supply = ctk.CTkButton(master=self, text='Limpar', text_color='#d0d0d0', fg_color='#26415E',
                                     hover_color='#0B1B32', corner_radius=12, bg_color='transparent',
                                     height=40, width=120, font=('Poppins', 15, 'bold'), command=self.clear_supply)
        clear_supply.place(relx=0.4, rely=0.9, anchor='center')

    def btn_add_supply(self) -> None:
        url = 'https://firestore.googleapis.com/v1/projects/sistema-bb725/databases/(default)/documents/fornecedores'
        input_data = {
            'fields': {
                'address': {
                    'stringValue': self.address.get()
                },
                'category': {
                    'stringValue': self.category.get()
                },
                'name': {
                    'stringValue' : self.order.get()
                },
                'product': {
                    'stringValue': self.product.get()
                },
                'status': {
                    'stringValue': self.status_supply.get()
                }
            }
        }
        response = requests.post(
            url, json=input_data
        )
        response_data = response.json()

        if response.status_code == 200:
            CTkMessagebox(master=self, message='Fornecedor cadastrado!', icon='check',
                          button_color='#26415E', button_hover_color='#0B1B32', text_color='#585858')
        else:
            error_message = response_data['error']['message']
            CTkMessagebox(master=self, message=error_message,
                          icon='cancel', button_color='#26415E',
                          button_hover_color='#0B1B32', text_color='#585858')

    def clear_supply(self) -> None:
        self.order.delete(0, ctk.END)
        self.address.delete(0, ctk.END)
        self.description.delete('1.0', ctk.END)
        self.product.delete(0, ctk.END)


if __name__ == '__main__':
    adm: AddSupply = AddSupply(status_login=True)
    adm.mainloop()