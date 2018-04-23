def _jupyter_server_extension_paths():
    return [{
        "module": "urlargs"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `urlargs` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="urlargs",
        # _also_ in the `nbextension/` namespace
        require="urlargs/index")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("urlargs module enabled!")

