from config_parser import Config


def get_file_base(selection, break_cond, cross, mutation, parent_selection):
    return f"{selection}_{break_cond}_{cross}_{mutation}_{parent_selection}"