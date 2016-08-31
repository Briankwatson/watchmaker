import argparse

from watchmaker import Prepare


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--noreboot', dest='noreboot', action='store_true',
                        help='No reboot after provisioning.')
    parser.add_argument('--sourceiss3bucket', dest='sourceiss3bucket',
                        action='store_true',
                        help=(
                            'Use S3 buckets instead of internet locations for '
                            'files.'
                        ))
    parser.add_argument('--config', dest='config', default=None,
                        help='Path or URL to the config.yaml file.')
    parser.add_argument('--saltstates', dest='saltstates', default=None,
                        help=(
                            'Define the saltstates to use.  Must be None, '
                            'Highstate, or comma-seperated-string'
                        ))
    log_path_group = parser.add_mutually_exclusive_group(required=False)
    log_path_group.add_argument(
        '--log-dir', dest='log_dir', default=None,
        help='Path to the log directory for stream logging.'
    )
    log_path_group.add_argument(
        '--log-file', dest='log_file', default=None,
        help='Path to the log file for stream logging.'
    )

    if parser.parse_args().saltstates:
        if parser.parse_args().saltstates.lower() not in [
            'none',
            'highstate',
            'comma-separated-string'
        ]:
            # Invalid saltstates
            parser.print_help()

    systemprep = Prepare(parser.parse_args())
    systemprep.install_system()
