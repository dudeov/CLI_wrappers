import argparse
import executor

def parse_args(cmdline: str = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Netauto device configuration tool"
    )
    subparsers = parser.add_subparsers(
        help="this is a set of positional sub-arguments"
    )

    # Subparser will call function `list_python_files`
    list_sub_parser = subparsers.add_parser(
        "list_python_files",
        help="calls list_python_files",
    )
    list_sub_parser.set_defaults(
        func=executor.list_python_files
    )
    # Subparser will call function `list_abs_python_files`
    abs_list_sub_parser = subparsers.add_parser(
        "list_abs_python_files",
        help="calls list_abs_python_files",
    )
    abs_list_sub_parser.set_defaults(
        func=executor.list_abs_python_files
    )

    ## this option to be used for unit-testing
    if cmdline:
        args = parser.parse_args(cmdline.split())
    ## fallback to sys.argv[1:]
    else:
        args = parser.parse_args()
    return args

def main(cmdline: str = None) -> None:
    args = parse_args(cmdline)
    args.func()


if __name__ == "__main__":
    main()
