from tkinter import Button, Label, Entry, Tk, IntVar, StringVar, messagebox, ttk


class View:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x450")
        self.window.title("User Management")
        self.var_dic = {}

    def mainloop(self):
        self.window.mainloop()

    def draw_int_input(self, text: str = "default", x: int = 20, y: int = 20, ex: int = 0, ey: int = 0):
        var_label = IntVar()
        Label(self.window, text=str(text)).place(x=x, y=y)
        Entry(self.window, textvariable=var_label).place(x=x + 100, y=y)
        self.var_dic[text] = var_label

    def draw_str_input(self, text: str = "default", x: int = 20, y: int = 20):
        var_label = StringVar()
        Label(self.window, text=str(text)).place(x=x, y=y)
        Entry(self.window, textvariable=var_label).place(x=x + 100, y=y)
        self.var_dic[text] = var_label

    def draw_button(self, command, text="default", width: int = 7, x: int = 20, y: int = 20):
        Button(self.window, text=str(text), width=width, command=command).place(x=x, y=y)

    def get_res_dic(self):
        return {key: value.get() for key, value in self.var_dic.items()}

    def draw_table(self, x: int, y: int, columns: int, show: str = "headings"):
        table = ttk.Treeview(self.window, columns=tuple(range(1, columns + 1)), show="headings")
        table.place(x=x, y=y)
        return table

    def show_message_box(self, success: bool, response: str):
        if success:
            messagebox.showinfo("INFO", response)
        else:
            messagebox.showerror("ERROR", response)

    def reset_form(self):
        for key, value in self.var_dic.items():
            self.var_dic[key].set("")
        # self.var_dic = {key : value.set("") for key, value in self.var_dic.items()}
        # new_dic = dict(map(lambda item: (item[0],item[1].set("")),self.var_dic.items()))
        # self.var_dic = new_dic

    def set_selected_values(self, selected_item):
        edited_item = list(self.var_dic.keys()).copy()
        edited_item.remove("password")
        for key, value in zip(edited_item, selected_item):
            self.var_dic[key].set(value)
