from anubis.adapters.ui.cli import launch_cli
from anubis.adapters.configurations import AnubisConfigs, ExecutionMode
from anubis.adapters.ui.gui import launch_gui


def main():
    execution_mode = AnubisConfigs().get_execution_mode()

    if execution_mode == ExecutionMode.CLI:
        print("Executing in CLI Mode")
        launch_cli()
    elif execution_mode == ExecutionMode.GUI:
        print("Execution in GUI Mode")
        launch_gui()

if __name__ == "__main__":
    main()