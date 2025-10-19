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
    return operations.get_entry(selected_item)

def secret_window(operations: Operations, secrets_list: Listbox):
    secret = open_secret(operations=operations, secrets_list=secrets_list)

    window = tkinter.Toplevel()
    center_window(window=window)

    frame = Frame(window)
    frame.pack(fill="both", padx=5, pady=5)

    name_label = Label(frame, text=secret.name)
    name_label.pack(padx="2", pady="5")

    value_entry = Entry(frame)
    value_entry.insert(0, secret.value)
    value_entry.pack(padx="2", pady="5")

    bottom_frame = Frame(frame)
    bottom_frame.pack(fill="x", side="bottom", pady="5")

    def update_secret(current: Secret, new_value: str):
        new_secret = Secret(name = current.name, value = new_value)
        operations.add_entry(new_secret)
        window.destroy()

    update_secret_btn = Button(
        bottom_frame,
        text="Update",
        command=lambda: update_secret(current = secret, new_value = value_entry.get())
    )
    update_secret_btn.pack(side="left")

    def delete_secret(name: str):
        operations.remove_entry(secret.name)
        window.destroy()

    delete_secret_btn = Button(bottom_frame, text="Delete", command=lambda: delete_secret(secret.name))
    delete_secret_btn.pack(side="right")

    window.wait_window()

def add_secret_window(operations: Operations):
    window = tkinter.Toplevel()
    center_window(window=window)

    frame = Frame(window)
    frame.pack(fill="both", padx=5, pady=5)

    key_entry = Entry(frame)
    key_entry.insert(0, "Secret Name")
    key_entry.pack(padx=3, pady=2)

    value_entry = Entry(frame, show="*")
    value_entry.pack()

    result = {}
    def on_secret_add():
        result["key"] = key_entry.get()
        result["value"] = value_entry.get()
        window.destroy()

    create_secret_btn = Button(frame, text="Add", command=on_secret_add)
    window.bind("<Return>", lambda e: on_secret_add())
    create_secret_btn.pack(pady=2)

    window.wait_window()

    operations.add_entry(Secret(name=result["key"], value=result["value"]))

def main_window(operations):
    root = tkinter.Tk()
    root.title("Anubis")
    root.wm_iconname("Anubis")

    center_window(window=root)

    frame = Frame(root)
    frame.pack(fill="both", padx=15, pady=15)

    title_label = Label(frame, text="Anubis Password Manager")
    title_label.pack(side="top", pady=5)

    secrets_list = Listbox(frame)
    secrets_list.bind("<Double-Button>", lambda event: secret_window(operations, secrets_list))

    # TODO: Refresh list when a secrets is added/deleted
    secrets = operations.list_entries()
    for idx, secret in enumerate(secrets):
        secrets_list.insert(idx, secret)
    secrets_list.pack(pady=5, fill="x")

    add_secret_btn = Button(frame, text="Add Secret", command=lambda: add_secret_window(operations))
    add_secret_btn.pack(side="bottom")

    root.mainloop()

def password_window():
    window = tkinter.Toplevel()
    center_window(window=window)

    frame = Frame(window)
    frame.pack()

    password_entry = Entry(frame, show="*")
    password_entry.pack(padx=3, pady=2)

    result = {}
    def submit_password():
        result["password"] = password_entry.get()
        window.destroy()

    submit_button = Button(frame, text="Submit", command=submit_password)
    submit_button.pack(pady=2)

    window.wait_window()

    return result["password"]

def center_window(window):
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()

    x_coordinate = int((window_width / 2) - (window.winfo_reqwidth() / 2))
    y_coordinate = int((window_height / 2) - (window.winfo_reqheight() / 2))

    window.geometry(f'+{x_coordinate}+{y_coordinate}')

def launch_gui():
    main_window(
        operations=Operations(
            repository=repository_provider(),
            password_provider=PasswordProvider(password_repository_provider(), lambda: password_window()),
            encryption_engine=EncryptionEngine()
        )
    )

