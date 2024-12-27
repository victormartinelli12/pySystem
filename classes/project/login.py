import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import requests
from adm import Page
from newuser import NewUser


class App(ctk.CTk):
    def __init__(self, status_login: bool = False) -> None:
        super().__init__()
        self.title('Sistema de Login') 
        self.geometry('350x350')
        self.maxsize(350, 350)
        self.minsize(350, 350)
        self.status_login = status_login

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

        self.button_login = ctk.CTkButton(master=self, text='Entrar', text_color='#f6f6f6',
                                          corner_radius=10, hover_color='#0B1B32', width=100,
                                          fg_color='#26415E', font=('Poppins', 13), command=self.btn_login)
        self.button_login.place(relx=0.5, rely=0.67, anchor='center')

        login_frame = ctk.CTkFrame(master=self, width=200, height=2.5,
                                   fg_color='#d0d0d0')
        login_frame.place(relx=0.21, rely=0.3)

        title_welcome = ctk.CTkLabel(master=self, text='Login', font=('Poppins', 25, 'bold'),
                                     text_color='#26415E')
        title_welcome.place(relx=0.5, rely=0.23, anchor='center')

        self.add_user = ctk.CTkButton(master=self, text='Cadastrar usuário',
                                      font=('Poppins', 10, 'bold'), bg_color='transparent',
                                      text_color='#26415E', fg_color='transparent',
                                      hover_color='#ebebeb', command=self.open_new_user)
        self.add_user.place(relx=0.5, rely=0.94, anchor='center')

    def btn_login(self) -> bool:
        input_data = {
            'email': self.entry_login.get(),
            'password': self.entry_password.get(),
            "returnSecureToken": True
        }

        response = requests.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDNO6UuAqERU6qSwIq5Xd4C3-e4wdOspsc",
            json=input_data
        )

        response_data = response.json()

        if response.status_code == 200: 
            self.token = response_data["idToken"]
            self.status_login = True
            CTkMessagebox(master=self, message='Login realizado com sucesso!', icon='check',
                          font=('Poppins', 13),
                          button_color='#0B1B32', button_hover_color='#26415E', text_color='#585858')
            page = Page(status_login=self.status_login)
            page.mainloop()
        else:
            CTkMessagebox(master=self, message='Tente novamente, email ou senha inválidos.', icon='cancel',
                          font=('Poppins', 13),
                          button_color='#0B1B32', button_hover_color='#26415E', text_color='#585858')
            self.entry_login.delete(0, ctk.END)
            self.entry_password.delete(0, ctk.END)

    def open_new_user(self) -> None:
        new_user: NewUser = NewUser()
        new_user.mainloop()


if __name__ == '__main__':
    app = App()
    app.mainloop()