import firebase_admin
from CTkMessagebox import CTkMessagebox
from firebase_admin import credentials, auth
import customtkinter as ctk

cred = credentials.Certificate(
    "C:\\Users\\Edu\\Downloads\\sistema-bb725-firebase-adminsdk-7d5jg-6132c1d40a.json")
firebase_admin.initialize_app(cred)


class NewUser(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.create_user()

    def create_user(self):
        self.title('Novo Usuário')
        self.geometry('350x350')
        self.maxsize(350, 350)
        self.minsize(350, 350)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.entry_login = ctk.CTkEntry(master=self, placeholder_text='Email',
                                        placeholder_text_color='#7F8087', corner_radius=10,
                                        fg_color='#d0d0d0',
                                        text_color='#7F8087', width=200, height=30,
                                        border_width=1.5, border_color='#26415E', font=('Poppins', 13))
        self.entry_login.place(relx=0.5, rely=0.45, anchor='center')

        self.entry_password = ctk.CTkEntry(master=self, placeholder_text='Password', placeholder_text_color='#7F8087',
                                           corner_radius=10,
                                           fg_color='#d0d0d0',
                                           text_color='#7F8087', width=200,
                                           border_width=1.5, border_color='#26415E', font=('Poppins', 13), show='•')
        self.entry_password.place(relx=0.5, rely=0.55, anchor='center')

        login_frame = ctk.CTkFrame(master=self, width=200, height=2.5,
                                   fg_color='#d0d0d0')
        login_frame.place(relx=0.21, rely=0.3)

        title_welcome = ctk.CTkLabel(master=self, text='Novo Usuário', font=('Poppins', 25, 'bold'),
                                     text_color='#26415E')
        title_welcome.place(relx=0.5, rely=0.23, anchor='center')

        self.btn_create_user = ctk.CTkButton(master=self, text='Cadastrar', text_color='#f6f6f6',
                                             corner_radius=10, hover_color='#0B1B32', width=100,
                                             fg_color='#26415E', font=('Poppins', 13),
                                             command=self.btn_new_user)
        self.btn_create_user.place(relx=0.5, rely=0.67, anchor='center')

    def btn_new_user(self) -> None:
        user = self.entry_login.get()
        password = self.entry_password.get()
        try:
            new_user = auth.create_user(
                email=user,
                password=password
            )
            CTkMessagebox(master=self, message='Usuário cadastrado com sucesso!', icon='check',
                          font=('Poppins', 13),
                          button_color='#0B1B32', button_hover_color='#26415E', text_color='#585858')
        except:
            CTkMessagebox(master=self, message='Algo deu errado! Sua senha precisa ter, no mínimo, 6 dígitos.', icon='cancel',
                          font=('Poppins', 13),
                          button_color='#0B1B32', button_hover_color='#26415E', text_color='#585858')


if __name__ == '__main__':
    new_user = NewUser()
    new_user.mainloop()
