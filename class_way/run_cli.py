import argparse
import executor

def parse_args(cmdline: str = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Netauto device configuration tool"
    )
    parser.add_argument(
        '-p', '--path-str',
        dest="path_str",
        default="/Users/aleksei.chuvakov/workplace/CLI_wrappers"
    )

    subparsers = parser.add_subparsers(
        help="this is a set of positional sub-arguments",
        dest="function_name"
    )

    # Subparser will call function `list_python_files`
    list_sub_parser = subparsers.add_parser(
        "list_python_files",
        help="calls list_python_files",
    )
    # Subparser will call function `list_abs_python_files`

    abs_list_sub_parser = subparsers.add_parser(
        "list_abs_python_files",
        help="calls list_abs_python_files",
    )

    ## this option to be used for unit-testing
    if cmdline:
        args = parser.parse_args(cmdline.split())
    ## fallback to sys.argv[1:]
    else:
        args = parser.parse_args()
    return args

def main(args: argparse.Namespace) -> None:
    runner = executor.ListFiles(args)
    runner.run()

if __name__ == "__main__":
    main(parse_args())
