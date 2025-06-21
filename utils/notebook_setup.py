import os

def set_project_root_dir(project_folder_name="heritage-housing-issues"):
    """Set working directory to the specified project root folder if not already there."""
    current_path = os.getcwd()

    if project_folder_name in current_path:
        while not os.path.basename(os.getcwd()) == project_folder_name:
            os.chdir(os.path.dirname(os.getcwd()))
        print(f"Working directory set to: {os.getcwd()}")
    else:
        raise FileNotFoundError(
            f"You're running the notebook outside the '{project_folder_name}' directory.\n"
            f"Current path: {current_path}"
        )