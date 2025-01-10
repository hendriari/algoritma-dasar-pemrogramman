from proyek_controller import ProyekController

if __name__ == "__main__":
    controller = ProyekController()
    menu = controller.menu()
    if menu == 1:
        proyek_list = controller.show_proyek()
    elif menu == 2:
        data = controller.get_data()
        update = controller.update_proyek(data)
