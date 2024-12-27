import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Sale(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.open_sale()

    def open_sale(self):
        self.title('Página de Vendas')
        self.geometry('1200x600')
        self.maxsize(1200, 600)
        self.minsize(1200, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        frame = ctk.CTkFrame(master=self, width=210, height=605,
                             fg_color='#0B1B32', corner_radius=20)
        frame.place(relx=0.07, rely=0.498, anchor='center')

        icon = ctk.CTkLabel(master=self, text='💰', font=('Poppins', 50),
                            text_color='#f6f6f6', fg_color='#0B1B32')
        icon.place(relx=0.045, rely=0.04)

        item_name = ctk.CTkLabel(master=self, text='Vendas', font=('Poppins', 28, 'bold'),
                                 text_color='#0D1E4C')
        item_name.place(relx=0.23, rely=0.07, anchor='center')

        order_name = ctk.CTkLabel(
            master=self, text='Código', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        order_name.place(relx=0.215, rely=0.18, anchor='center')

        self.codig = ctk.CTkEntry(master=self, width=870, height=40, fg_color='#d0d0d0',
                                  border_width=0, text_color='#0D1E4C', font=('Poppins', 18))
        self.codig.place(relx=0.55, rely=0.24, anchor='center')

        category_name = ctk.CTkLabel(
            master=self, text='Forma de Pagamento', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        category_name.place(relx=0.27, rely=0.33, anchor='center')

        self.pay_mode = self.status_supply = ctk.CTkComboBox(
            master=self, width=440, height=40, fg_color='#d0d0d0', font=('Poppins', 16, 'bold'),
            dropdown_fg_color='#26415E', justify='left', values=['Dinheiro', 'Débito', 'Crédito', 'Pix', 'À Prazo'],
            text_color='#0D1E4C', dropdown_hover_color='#83A6CE', button_color='#26415E',
            text_color_disabled='#83A6CE', dropdown_text_color='#f6f6f6',
            button_hover_color='#26415E', border_width=2, border_color='#26415E')
        self.pay_mode.place(relx=0.372, rely=0.4, anchor='center')

        address_name = ctk.CTkLabel(
            master=self, text='Quantidade', text_color='#0D1E4C', font=('Poppins', 18, 'bold'))
        address_name.place(relx=0.625, rely=0.33, anchor='center')

        self.qtd = ctk.CTkEntry(master=self, width=400, height=40, fg_color='#d0d0d0',
                                    border_width=0, text_color='#0D1E4C', font=('Poppins', 18))
        self.qtd.place(relx=0.75, rely=0.4, anchor='center')

        sale_frame = ctk.CTkFrame(master=self, width=400, height=120,
                                  corner_radius=12,  fg_color='#d0d0d0')
        sale_frame.place(relx=0.75, rely=0.63, anchor='center')

        total_item = ctk.CTkLabel(master=self, text='Total', font=('Poppins', 18, 'bold'),
                                  text_color='#0D1E4C')
        total_item.place(relx=0.605, rely=0.49, anchor='center')

        add_sale = ctk.CTkButton(master=self, text='Adicionar', text_color='#d0d0d0', fg_color='#26415E',
                                   hover_color='#0B1B32', corner_radius=12, bg_color='transparent',
                                   height=40, width=120, font=('Poppins', 15, 'bold'),
                                   command=self.add_btn)
        add_sale.place(relx=0.24, rely=0.9, anchor='center')

        clear_sale = ctk.CTkButton(master=self, text='Limpar', text_color='#d0d0d0', fg_color='#26415E',
                                     hover_color='#0B1B32', corner_radius=12, bg_color='transparent',
                                     height=40, width=120, font=('Poppins', 15, 'bold'),
                                     command=self.clear_btn)
        clear_sale.place(relx=0.4, rely=0.9, anchor='center')

    def clear_btn(self) -> None:
        self.codig.delete(0, ctk.END)
        self.qtd.delete(0, ctk.END)

    def add_btn(self) -> None:
        codig = self.codig.get()
        qtd = self.qtd.get()
        pay_mode = self.pay_mode.get()

        if codig and qtd and pay_mode:
            CTkMessagebox(master=self, message='Compra registrada com sucesso!', icon='check',
                          button_color='#26415E', button_hover_color='#0B1B32', text_color='#585858')
        else:
            CTkMessagebox(master=self, message='Insira corretamente todos os campos.', icon='cancel',
                          button_color='#26415E', button_hover_color='#0B1B32', text_color='#585858')




if __name__ == '__main__':
    sale: Sale = Sale()
    sale.mainloop()
