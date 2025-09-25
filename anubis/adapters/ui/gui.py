import tkinter
from tkinter import Listbox, Button, Frame, Label, Entry, Menu, Tk

from anubis.adapters.password import password_repository_provider
from anubis.adapters.secrets import repository_provider
from anubis.core.encryption import EncryptionEngine
from anubis.core.operations import Operations
from anubis.core.password import PasswordProvider
from anubis.core.secrets import Secret


def open_secret(operations: Operations, secrets_list: Listbox):
    selected_index = secrets_list.curselection()[0]
    selected_item = secrets_list.get(selected_index)

    secret = operations.get_entry(selected_item)

    # Create a window to show and delete the secret

def add_secret_window(operations: Operations):
    window = tkinter.Toplevel()

    frame = Frame(window)
    frame.pack(fill="both", padx=5, pady=5)

    key_entry = Entry(frame)
    key_entry.insert(0, "Secret Name")
    key_entry.pack()

    value_entry = Entry(frame, show="*")
    value_entry.pack()

    result = {}
    def on_secret_add():
        result["key"] = key_entry.get()
        result["value"] = value_entry.get()
        window.destroy()

    create_secret_btn = Button(frame, text="Add", command=on_secret_add)
    window.bind("<Return>", lambda e: on_secret_add())
    create_secret_btn.pack()

    window.wait_window()

    print(f'Key: {result["key"]} - Value: {result["value"]}')
    operations.add_entry(Secret(name=result["key"], value=result["value"]))

def main_window(operations):
    root = tkinter.Tk()

    frame = Frame(root)
    frame.pack(fill="both", padx=15, pady=15)

    title_label = Label(frame, text="Anubis Password Manager")
    title_label.pack(side="top", pady=5)

    secrets_list = Listbox(frame)
    secrets_list.bind("<Double-Button>", lambda event: open_secret(operations, secrets_list))

    secrets = operations.list_entries()
    for idx, secret in enumerate(secrets):
        secrets_list.insert(idx, secret)
    secrets_list.pack(pady=5, fill="x")

    add_secret_btn = Button(frame, text="Add Secret", command=lambda: add_secret_window(operations))
    add_secret_btn.pack(side="bottom")

    root.mainloop()

def password_window():
    window = tkinter.Toplevel()

    frame = Frame(window)
    frame.pack()

    password_entry = Entry(frame, show="*")
    password_entry.pack()

    result = {}
    def submit_password():
        result["password"] = password_entry.get()
        window.destroy()

    submit_button = Button(frame, text="Submit", command=submit_password)
    submit_button.pack()

    window.wait_window()

    return result["password"]

def launch_gui():
    main_window(
        operations=Operations(
            repository=repository_provider(),
            password_provider=PasswordProvider(password_repository_provider(), lambda: password_window()),
            encryption_engine=EncryptionEngine()
        )
    )

