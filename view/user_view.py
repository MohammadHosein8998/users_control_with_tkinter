from tkinter import END
from controller.user_controller import UserControl
from model.view import View


def run():
    my_input_list = ["name", "family", "national code", "birth date", "phone number", "user name", "password", "role",
                     "locked"]
    win = View()

    controller = UserControl()



    #  show data on the table

    def show_data_on_the_table():
        success, user_list = controller.get_all_user()

        if success:
            for item in users_table.get_children():
                users_table.delete(item)
            for user in user_list:
                users_table.insert("", END, values=user.to_tuple())


    # select_user on the table

    def select_user(event_info):
        row_id = users_table.focus()
        selected_item = users_table.item(row_id, "values")
        win.set_selected_values(selected_item)


    # resetting the form after events calls
    def reset_form():
        win.reset_form()
        show_data_on_the_table()


    #  my functions
    def save_product() -> None:
        print("saving product")
        user = win.get_res_dic()
        success, response = controller.save_user(user)
        if success:
            users_table.insert("", END, values=tuple(user.values()))
            reset_form()
        win.show_message_box(success, response)


    def edit_product() -> None:
        print("editing product")
        user = win.get_res_dic()
        success, response = controller.edite_user(user)
        if success:
            reset_form()
        win.show_message_box(success, response)


    def delete_product() -> None:
        print("deleting product")
        user = win.get_res_dic()
        success, response = controller.delete_user(user["national code"])
        if success:
            reset_form()
        win.show_message_box(success, response)



    #  mt Label drawing
    for component in list(enumerate(my_input_list)):
        win.draw_str_input(text=component[1], x=20, y=(component[0] + 1) * 30)

    # my users table headings

    headings_list = ["name", "family", "national code", "birth date", "phone number", "user name", "role", "locked"]
    users_table = win.draw_table(x=290, y=20, columns=len(headings_list))

    for i in range(0, len(headings_list)):
        users_table.heading(i + 1, text=headings_list[i])
        users_table.column(i + 1, width=100)

    users_table.bind("<ButtonRelease>", select_user)

    # my Button drawing
    my_button_list = [("save", save_product), ("edite", edit_product),
                      ("delete", delete_product)]

    for component in list(enumerate(my_button_list)):
        win.draw_button(text=component[1][0], x=(component[0] + 1) * 70, y=300, command=component[1][1])

    reset_form()
    win.mainloop()
