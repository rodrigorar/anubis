import tkinter
from getpass import getpass
from tkinter import Listbox, Button, Frame, Label, Entry

from anubis.adapters.password import password_repository_provider
from anubis.adapters.secrets import repository_provider
from anubis.core.encryption import EncryptionEngine
from anubis.core.operations import Operations
from anubis.core.password import PasswordProvider


def input_password_window(secretsList: Listbox, event):
    # TODO: Launch window for password input and copy to clipboard afterwords
    selected_index = secretsList.curselection()[0]
    selected_item = secretsList.get(selected_index)
    print(f'Item {selected_item} Selected')

def add_secret_window(operations):
    secret_window = tkinter.Tk()

    frame = Frame(secret_window)
    frame.pack(fill="both", padx=5, pady=5)

    key_entry = Entry(frame)
    key_entry.insert(0, "Secret Name")
    key_entry.pack()

    secret_entry = Entry(frame, show="*")
    secret_entry.pack()

    def on_secret_add():
        print(key_entry.get())
        print(secret_entry.get())
        secret_window.destroy()

    create_secret_btn = Button(frame, text="Add", command=on_secret_add)
    secret_window.bind("<Return>", lambda e: on_secret_add())
    create_secret_btn.pack()

    secret_window.mainloop()

def main_window(operations):
    root = tkinter.Tk()

    frame = Frame(root)
    frame.pack(fill="both", padx=15, pady=15)

    titleLabel = Label(frame, text="Anubis Password Manager")
    titleLabel.pack(side="top", pady=5)

    secretsList = Listbox(frame)
    secretsList.bind("<Double-Button>", lambda event: get_secret(secretsList, event))

    secrets = operations.list_entries()
    for idx, secret in enumerate(secrets):
        secretsList.insert(idx, secret)
    secretsList.pack(pady=5, fill="x")

    add_secret_btn = Button(frame, text="Add Secret", command=lambda: add_secret_window(operations))
    add_secret_btn.pack(side="bottom")

    root.mainloop()

def launch_gui():
    main_window(
        operations=Operations(
            repository=repository_provider(),
            password_provider=PasswordProvider(password_repository_provider(),
                                               lambda: getpass("Password >>> ")),
            encryption_engine=EncryptionEngine()
        )
    )

