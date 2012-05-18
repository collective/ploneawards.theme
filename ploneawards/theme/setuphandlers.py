def import_various(context):
    """Import step for configuration that is not
     handled in xml files.
    """
    # Only run step if a flag file is present
    if context.readDataFile('ploneawards.theme-default.txt') is None:
        return
